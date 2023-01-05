from os import error
from pathlib import Path
import requests
from datetime import datetime
from jinja2 import Template
import logging
import re
import os
import sys
import config

logger = logging.getLogger(__name__)

headers = {}
env = dict(os.environ)
if "GITHUB_TOKEN" in env:
  headers["Authorization"] = " ".join(["Bearer", os.environ["GITHUB_TOKEN"]])
else:
  logger.warn("No GITHUB_TOKEN found in env")

def from_gh(response, external = False) -> dict:
  data = {
    "title": response["name"],
    "url": response["html_url"],
    "description": response["description"],
    "readme": "https://raw.githubusercontent.com/{path}/{branch}/README.md".format(
      path = response["full_name"],
      branch = response["default_branch"]
    ),
    "tags": response["tags_url"],
    "external": external
  }
  if response["archived"]:
    data["maturity"] = "Deprecated"
  return data

def get_sources() -> list:
  data = []

  try:
    logger.info(f"Reading list of repositories")
    with requests.get("https://api.github.com/users/stac-extensions/repos?per_page=1000", headers=headers) as site:
      repos = site.json()
      for repo in repos:
        if not isinstance(repo, dict):
          logger.error(f"response invalid")
          continue
        if repo["is_template"] or repo["name"] in config.IGNORE_REPOS:
          continue
        data.append(from_gh(repo, False))
  except error as e:
      logger.error(f"stac-extensions not available: {e}")

  for r in config.COMMUNITY_REPOS:
    try:
      logger.info(f"Reading community repos individually")
      with requests.get(f"https://api.github.com/repos/{r[0]}/{r[1]}", headers=headers) as repo:
        data.append(from_gh(repo.json(), True))
    except error as e:
        logger.error(f"community repo not available: {e}")

  for r in config.EXTERNAL_EXTENSIONS:
    r["external"] = True
    data.append(r)

  return data

def get_extensions() -> list:
  unknown = "*Unknown*"
  wip = "*WIP*"
  data = get_sources()
  for src in data:
    # Get tags
    if "version" not in src:
      src["version"] = unknown
    if "tags" in src:
      try:
        with requests.get(src["tags"], headers=headers) as tags:
          tags = tags.json()
          if len(tags) > 0:
            src["version"] = re.sub(r"^v", "", tags[0]["name"])
          else:
            src["version"] = "**Unreleased**"
            if "maturity" not in src:
              src["maturity"] = wip
      except error as e:
        logger.error(f"tags not available: {e}")
    
    # Parse README
    if "readme" in src:
      try:
        logger.info("Reading readme for" + src["title"])
        with requests.get(src["readme"]) as readme:
          # Parse title
          title = re.search(r"[\-\*]\s+[\*\_]*Title[\*\_]*:[\*\_]*\s*(.+)", readme.text, re.I)
          if title:
            title_str = title.group(1).strip()
            if "template" not in title_str.lower():
              src["title"] = title_str
        
          # Parse scope
          scope = re.search(r"[\-\*]\s+[\*\_]*Scope[\*\_]*:[\*\_]*\s*([\w\s,]+)", readme.text, re.I)
          if scope:
            scopes = scope.group(1).split(",")
            scopes = [s.strip() for s in scopes]
            scopes.sort()
            src["scope"] = ", ".join(scopes)

          # Parse prefix
          prefix = re.search(r"[\-\*]\s+[\*\_]*(?:Field\s+Name\s+)?Prefix[\*\_]*:[\*\_]*\s*`?(.{1,20})`?", readme.text, re.I)
          if prefix:
            prefix_str = prefix.group(1).strip()
            if "template" not in prefix_str.lower():
              src["prefix"] = prefix_str

          # Parse maturity
          maturity = re.search(r"[\-\*]\s+[\*\_]*Extension\s+(?:(?:Maturity\s+)?Classification|\[Maturity Classification\]\([^\)]+\))[\*\_]*:[\*\_]*\s*(.+)", readme.text, re.I)
          if maturity and "maturity" not in src:
            maturity_str = maturity.group(1).strip()
            maturity_lc = maturity_str.lower()
            if "wip" in maturity_lc or "work in progress" in maturity_lc:
              src["maturity"] = wip
            elif maturity_lc in ["proposal", "pilot", "candidate", "stable", "deprecated"]:
              src["maturity"] = maturity_str
      except error as e:
          logger.error(f"readme not available: {e}")

    if "prefix" not in src:
      src["prefix"] = unknown
    if "maturity" not in src:
      src["maturity"] = unknown
    if "scope" not in src:
      src["scope"] = unknown

  return data

def group_by_maturity(extensions) -> dict:
  levels = {
    "Stable": [],
    "Candidate": [],
    "Pilot": [],
    "Proposal": [],
    "WIP": [],
    "Deprecated": [],
  }
  for extension in extensions:
    found = [l for l in levels.keys() if l.lower() in extension["maturity"].lower()]
    if len(found) == 0:
      continue

    levels[found[0]].append(extension)
    
  return levels

def main() -> bool:
  data = get_extensions()
  data.sort(key = lambda x: x["title"])
  maturities = group_by_maturity(data)
  count = len(data)

  if count < 45:
    logger.error("Something likely went wrong as there are not enough repos listed, don't overrride README")
    sys.exit(1)
  
  now = datetime.utcnow().strftime("%b %d %Y, %H:%M %Z")
  template = Template(Path("./python/README_TEMPLATE.md.jinja").read_text())

  with Path("./README.md") as f:
    f.write_text(template.render(extensions=data, maturities=maturities, updated=now, count=count))

  sys.exit(0)


if __name__ == "__main__":
  main()
