# Names of GitHub repositories not in stac-extensions org
COMMUNITY_REPOS = [
  # org, repo name
  ['crim-ca', 'dlm-extension'],
  ['Terradue', 'stac-extensions-disaster'],
  ['openrsgis', 'trainingdml-ai-extension'],
  ['stacchain', 'merkle-tree'],
  ['IFRCGo', 'monty-stac-extension'],
  ['cityjson', 'stac-city3d']
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
  },
  {
    "title": "Landsat",
    "url": "https://landsat.usgs.gov/stac/landsat-extension/v1.1.1/schema.json",
    "version": "1.1.1",
    "prefix": "landsat",
    "description": "*JSON Schema only!*"
  },
  {
    "title": "Landsat ARD Tile",
    "url": "https://landsat.usgs.gov/stac/landsat-ard-extension/v1.0.0/schema.json",
    "version": "1.0.0",
    "prefix": "landsat",
    "description": "*JSON Schema only!*"
  }
]

# Names of repositories in the stac-extensions org to skip
IGNORE_REPOS = [
  "remote-data",
  "stac-extensions.github.io",
  "template"
]
