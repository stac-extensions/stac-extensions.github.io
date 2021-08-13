from os import error
from pathlib import Path
import requests
from datetime import datetime
from jinja2 import Template
import logging
import marko
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def get_repos() -> list:
    """Get a list of repositories from Github

    Returns:
        extensions: List of dictionaries containing extension repositories.
    """
    try:
        with requests.get("https://api.github.com/users/stac-extensions/repos") as site:
            extensions = site.json()
    except error as e:
        logger.error(f"Requests could not complete. {e}")

    return extensions


class stac_extension:
    def __init__(self, id: str) -> None:
        """Repository information for stac extensions.

        Args:
            id (str): A stac extenstion id.
        """
        self.id = id

    def parse_markdown(self, markdown_doc: str) -> dict:
        """Parses a Markdown document for STAC extension information.

        Args:
            markdown_doc (str): Markdown string to parse.

        Returns:
            dict: Dict of metadata from GitHub and repository readme's.
        """

        stac_attributes = [
            "title",
            "identifier",
            "field name prefix",
            "scope",
            "extension maturity classification",
        ]
        stac_info = {}
        stac_info["stac_md_extras"] = {attribute: "" for attribute in stac_attributes}

        html_doc = marko.convert(markdown_doc)
        soup = BeautifulSoup(html_doc, "html.parser")
        listing = soup.find("ul")

        for li in listing.findAll("li"):
            if li.find("ul"):
                break
            attribute = li.text.split(":", 1)
            asset_to_map = attribute[0].strip().lower()
            try:
                stac_info["stac_md_extras"][asset_to_map] = attribute[1].strip()
            except IndexError as e:
                continue
                # Readme doesn't conform to expected format.

        # underscore for spaces in keys
        clean_stac_info = {}
        clean_stac_info["stac_md_extras"] = {
            k.replace(" ", "-"): v for k, v in stac_info["stac_md_extras"].items()
        }

        return clean_stac_info

    def get_extension_readme(self) -> dict:
        """Gets the stac extension readme.md and parses it.

        Returns:
            dict: Dict of metadata from GitHub and repository readme's.
        """
        with requests.get(
            f"https://raw.githubusercontent.com/stac-extensions/{self.id}/main/README.md"
        ) as site:
            extension_attributes = self.parse_markdown(site.text)

        return extension_attributes


def get_stac_info(extensions: list) -> list:
    """Gets all extra STAC info from all STAC extensions.

    Args:
        extensions (list): list of repositories returned from GitHub API.

    Returns:
        list: list of repositories returned from GitHub API with an added nested dict.
    """

    extension_extras = {}

    for extension in extensions:
        repo_name = extension.get("name")
        extras = stac_extension(repo_name).get_extension_readme()
        extension_extras.update(extras)
        extension.update(**extras)

    return extensions


def main() -> bool:
    """Create a readme markdown document and populate the repository table
    from the stac-extensions Github Organization.

    Returns:
        bool: True if it worked
    """
    data = get_repos()
    repo_info = get_stac_info(data)
    now = datetime.utcnow().strftime("%b %d %H:%M %Z %Y")
    template = Template(Path("./README_TEMPLATE.md.jinja").read_text())

    with Path("./README.md") as f:
        f.write_text(template.render(extensions=repo_info, updated_time=now))

    return True


if __name__ == "__main__":
    main()
