# Names of GitHub repositories not in stac-extensions org
COMMUNITY_REPOS = [
  # org, repo name
  ['thareUSGS', 'ssys'], 
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
  },
  {
    "title": "CF",
    "url": "https://github.com/Fred-Leclercq/stac-CF-extention",
    "readme": "https://raw.githubusercontent.com/Fred-Leclercq/stac-CF-extention/main/README.md",
    "description": "CF conventions define metadata that provide a definitive description of what the data in each variable represents, and the spatial and temporal properties of the data. Especially useful for NetCDF assets."
  },
  {
    "title": "Disasters Charter",
    "url": "https://github.com/Terradue/stac-extensions-disaster",
    "version": "1.0.0",
    "readme": "https://raw.githubusercontent.com/Terradue/stac-extensions-disaster/main/README.md",
    "description": "The International Charter Space and Major Disasters related metadata to describe disaster events and satelitte acquisitions."
  },
]

# Names of repositories in the stac-extensions org to skip
IGNORE_REPOS = [
  "remote-data",
  "stac-extensions.github.io",
  "template"
]
