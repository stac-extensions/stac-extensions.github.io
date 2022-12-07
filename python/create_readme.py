from os import error
from pathlib import Path
import requests
from datetime import datetime
from jinja2 import Template
import logging
import re
import os
import sys

logger = logging.getLogger(__name__)

# Names of repositories to skip
IGNORE_REPOS = [
  "remote-data",
  "stac-extensions.github.io",
  "template"
]

# Names of GitHub repositories not in stac-extensions org
COMMUNITY_REPOS = [
  # Example (org, repo name):
  # ['stac-extensions', 'card4l'], 
]

# Other extensions that are not on GitHub
EXTERNAL_EXTENSIONS = [
  {
    "title": "Aerial Photo",
    "url": "https://github.com/linz/stac/tree/master/extensions/aerial-photo",
    "readme": "https://raw.githubusercontent.com/linz/stac/master/extensions/aerial-photo/README.md",
    "description": "Aerial photography related metadata, such as run, sequence number, altitude and scale."
  },
  {
    "title": "Camera",
    "url": "https://github.com/linz/stac/tree/master/extensions/camera",
    "readme": "https://raw.githubusercontent.com/linz/stac/master/extensions/camera/README.md",
    "description": "Camera related metadata, such as focal length and sequence number. Especially useful for aerial imagery surveys."
  },
  {
    "title": "Film",
    "url": "https://github.com/linz/stac/tree/master/extensions/film",
    "readme": "https://raw.githubusercontent.com/linz/stac/master/extensions/film/README.md",
    "description": "Film related metadata, such as roll, negative sequence and other physical attributes. Especially useful for digitised historic aerial imagery surveys."
  },
  {
    "title": "Quality",
    "url": "https://github.com/linz/stac/tree/master/extensions/quality",
    "readme": "https://raw.githubusercontent.com/linz/stac/master/extensions/quality/README.md",
    "description": "Geospatial quality and accuracy of collections, such as horizontal and vertical accuracy."
  },
  {
    "title": "Scanning",
    "url": "https://github.com/linz/stac/tree/master/extensions/scanning",
    "readme": "https://raw.githubusercontent.com/linz/stac/master/extensions/scanning/README.md",
    "description": "Scanning related metadata, such as the scan date and time. Especially useful for digitised images."
  }
]

headers = {}
env = dict(os.environ)
if "github-token" in env:
  headers["Authorization"] = " ".join(["token", os.environ["github-token"]])

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
    data["maturity"] = "**Deprecated**"
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
        if repo["is_template"] or repo["name"] in IGNORE_REPOS:
          continue
        data.append(from_gh(repo, False))
  except error as e:
      logger.error(f"stac-extensions not available: {e}")

  for r in COMMUNITY_REPOS:
    try:
      logger.info(f"Reading community repos individually")
      with requests.get(f"https://api.github.com/repos/{r[0]}/{r[1]}", headers=headers) as repo:
        data.append(from_gh(repo.json(), True))
    except error as e:
        logger.error(f"community repo not available: {e}")

  for r in EXTERNAL_EXTENSIONS:
    r["external"] = True
    data.append(r)

  return data

def get_extensions() -> list:
  unknown = "*Unknown*"
  wip = "*WIP*"
  data = get_sources()
  for src in data:
    # Get tags
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
        else:
          src["scope"] = unknown

        # Parse prefix
        prefix = re.search(r"[\-\*]\s+[\*\_]*(?:Field\s+Name\s+)?Prefix[\*\_]*:[\*\_]*\s*`?(.{1,20})`?", readme.text, re.I)
        if prefix:
          prefix_str = prefix.group(1).strip()
          if "template" not in prefix_str.lower():
            src["prefix"] = prefix_str
        if "prefix" not in src:
          src["prefix"] = unknown

        # Parse maturity
        maturity = re.search(r"[\-\*]\s+[\*\_]*Extension\s+(?:(?:Maturity\s+)?Classification|\[Maturity Classification\]\([^\)]+\))[\*\_]*:[\*\_]*\s*(.+)", readme.text, re.I)
        if maturity and "maturity" not in src:
          maturity_str = maturity.group(1).strip()
          maturity_lc = maturity_str.lower()
          if "wip" in maturity_lc or "work in progress" in maturity_lc:
            src["maturity"] = wip
          elif maturity_lc in ["proposal", "pilot", "candidate", "stable"]:
            src["maturity"] = maturity_str
        if "maturity" not in src:
          src["maturity"] = unknown
    except error as e:
        logger.error(f"readme not available: {e}")

  return data
    

def main() -> bool:
  data = get_extensions()
  data.sort(key = lambda x: x["title"])

  if len(data) < 45:
    logger.error("Something likely went wrong as there are not enough repos listed, don't overrride README")
    sys.exit(1)
  
  now = datetime.utcnow().strftime("%b %d %Y, %H:%M %Z")
  template = Template(Path("./python/README_TEMPLATE.md.jinja").read_text())

  with Path("./README.md") as f:
    f.write_text(template.render(extensions=data, updated=now))

  sys.exit(0)


if __name__ == "__main__":
  main()
