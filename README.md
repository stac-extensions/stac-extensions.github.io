# STAC Extensions

The [stac-extensions](https://github.com/stac-extensions/) GitHub organization is a home for extensions to the
[SpatioTemporal Asset Catalog](https://github.com/radiantearth/stac-spec) specification.

To learn about STAC and Extensions start with the [extensions](https://github.com/radiantearth/stac-spec/tree/master/extensions)
section of the core specification. It explains how extensions work, lists all the known extensions, and has
instructions for how to go about '[extending STAC](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md#extending-stac)'.

The [stac-extensions](https://github.com/stac-extensions/) GitHub organization is a home for many of the leading 'community extensions',
providing a neutral home for collaboration. Many of these used to be in the core
[stac-spec repository](https://github.com/radiantearth/stac-spec), but were removed for 1.0.0 so they could evolve at their
own pace, instead of having to follow the core STAC release cycle.

## List of STAC Extensions

This is meant to be the definitive list of STAC Extensions, but not all of them may be part of this GitHub organization.

An asterisk (*) indicates a community extension that is hosted externally.
As such is not part of the stac-extensions GitHub organization and may not follow the normal procedure or classification for STAC extensions, e.g. regarding the maturity.

Below you can also find a list of extensions grouped by [maturity](#grouped-by-maturity).

### Alphabetical list

| Title | Field Name Prefix | Scope | [Maturity](https://github.com/radiantearth/stac-spec/tree/master/extensions#extension-maturity) | Version | Description |
| ----- | ----------------- | ----- | ----------------------------------------------------------------------------------------------- | ------- | ----------- |
| [Accuracy](https://github.com/stac-extensions/accuracy) | accuracy | Collection, Item | *WIP* | **Unreleased** | Fields to provide estimates of accuracy, both geometric and measurement (e.g., radiometric) accuracy. |
| [Aerial Photography](https://github.com/linz/stac/tree/master/extensions/aerial-photo)* | aerial-photo | Collection, Item | *WIP* | *Unknown* | Aerial photography related metadata, such as run, sequence number, altitude and scale. |
| [Alternate Assets](https://github.com/stac-extensions/alternate-assets) | - | Asset | Pilot | 1.1.0 | Describes alternate locations and mirrors of assets |
| [Anonymized Location](https://github.com/stac-extensions/anonymized-location) | anon | Collection, Item | Pilot | 1.0.0 | Provides a way to anonymize location data |
| [CARD4L (Optical and SAR)](https://github.com/stac-extensions/card4l) | card4l | Item | Pilot | 0.1.0 | Describes how to comply to the CEOS CARD4L specifications (SAR and Optical) with STAC |
| [CF](https://github.com/Fred-Leclercq/stac-CF-extention)* | cf | Collection, Item | Proposal | *Unknown* | CF conventions define metadata that provide a definitive description of what the data in each variable represents, and the spatial and temporal properties of the data. Especially useful for NetCDF assets. |
| [Camera](https://github.com/linz/stac/tree/master/extensions/camera)* | camera | Collection, Item | *WIP* | *Unknown* | Camera related metadata, such as focal length and sequence number. Especially useful for aerial imagery surveys. |
| [Classification](https://github.com/stac-extensions/classification) | classification | Collection, Item | Pilot | 1.1.0 | Describes categorical values and bitfields to give values in a file a certain meaning (classification). |
| [Composite](https://github.com/stac-extensions/composite) | composite | Item | *WIP* | **Unreleased** | Defines how virtual assets can be composed from existing assets in STAC |
| [Datacube](https://github.com/stac-extensions/datacube) | cube | Collection, Item | Candidate | 2.1.0 | Datacube related metadata to describe their dimensions and variables. |
| [Electro-Optical](https://github.com/stac-extensions/eo) | eo | Collection, Item | Stable | 1.0.0 | Covers electro-optical data that represents a snapshot of the Earth. It could consist of cloud cover and multiple spectral bands, for example visible bands, infrared bands, red edge bands and panchromatic bands. |
| [File Info](https://github.com/stac-extensions/file) | file | Catalog, Collection, Item | Stable | 2.1.0 | Specifies file-related details such as size, data type and checksum for assets and links in STAC. |
| [Film](https://github.com/linz/stac/tree/master/extensions/film)* | film | Collection, Item | *WIP* | *Unknown* | Film related metadata, such as roll, negative sequence and other physical attributes. Especially useful for digitised historic aerial imagery surveys. |
| [Forecast](https://github.com/stac-extensions/forecast) | forecast | Collection, Item | Proposal | 0.1.0 | Common fields for (meteorological/weather) forecast data. |
| [Grid](https://github.com/stac-extensions/grid) | grid | Item | Pilot | 1.1.0 | Describes gridded data products, especially the grid code. |
| [Hyperspectral Imagery](https://github.com/stac-extensions/hsi) | hsi | Collection, Item | *WIP* | **Unreleased** | Extension for Hyperspectral Imagery, to preserve the wavelength information for Items. |
| [InSAR](https://github.com/stac-extensions/insar) | insar | Item | *WIP* | **Unreleased** | STAC extension for InSAR (Interferometric Synthetic Aperture Radar) |
| [Item Assets Definition](https://github.com/stac-extensions/item-assets) | - | Collection | Stable | 1.0.0 | Provides a way to specify details about what assets may be found in Items belonging to a Collection. |
| [Label](https://github.com/stac-extensions/label) | label | Collection, Item | Pilot | 1.0.1 | Items that relate labeled AOIs with source imagery. |
| [Landsat](https://landsat.usgs.gov/stac/landsat-extension/v1.1.1/schema.json)* | landsat | *Unknown* | *Unknown* | 1.1.1 | *JSON Schema only!* |
| [Landsat ARD Tile](https://landsat.usgs.gov/stac/landsat-ard-extension/v1.0.0/schema.json)* | landsat | *Unknown* | *Unknown* | 1.0.0 | *JSON Schema only!* |
| [Language (I18N)](https://github.com/stac-extensions/language) | - | Catalog, Collection, Item | *WIP* | **Unreleased** | Fields and recommendations around making multi-lingual STAC catalogs available.  |
| [ML AOI](https://github.com/stac-extensions/ml-aoi) | ml-aoi | Collection, Item | *WIP* | **Unreleased** | An Item and Collection extension to provide labeled training data for machine learning models. |
| [ML Model](https://github.com/stac-extensions/ml-model) | ml-model | Collection, Item | Proposal | 1.0.0 | An Item and Collection extension to describe machine learning (ML) models that operate on Earth observation data. |
| [Military Grid Reference System](https://github.com/stac-extensions/mgrs) | mgrs | Item | Pilot | 1.0.0 | MGRS extension that provides information about the latitude band, grid square and UTM zone. |
| [NOAA Geostationary Operational Environmental Satellite (GOES)](https://github.com/stac-extensions/goes) | goes | Collection, Item | Pilot | 1.0.0 | STAC Extension for NOAA GOES (Geostationary Operational Environmental Satellite) products |
| [NOAA MRMS QPE](https://github.com/stac-extensions/noaa-mrms-qpe) | noaa_mrms_qpe | Collection, Item | Pilot | 1.0.0 | STAC Extension for NOAA MRMS QPE (Multi-Radar Multi-Sensor Quantitative Precipitation Estimation) products |
| [Order](https://github.com/stac-extensions/order) | order | Collection, Item | Pilot | 1.1.0 | Allows assets ordering management within STAC specification. |
| [Perspective Imagery](https://github.com/stac-extensions/perspective-imagery) | pers | Collection, Item | *WIP* | **Unreleased** | Describes perspective imagery collected by photogrammetric or non-photogrammetric cameras |
| [Point Cloud](https://github.com/stac-extensions/pointcloud) | pc | Collection, Item | Pilot | 1.0.0 | Provides a way to describe point cloud datasets. The point clouds can come from either active or passive sensors, and data is frequently acquired using tools such as LiDAR or coincidence-matched imagery. |
| [Processing](https://github.com/stac-extensions/processing) | processing | Collection, Item | Candidate | 1.1.0 | Indicates from which processing chain data originates and how the data itself has been produced. |
| [Projection](https://github.com/stac-extensions/projection) | proj | Collection, Item | Stable | 1.0.0 | Provides a way to describe Items whose assets are in a geospatial projection. |
| [Quality](https://github.com/linz/stac/tree/master/extensions/quality)* | quality | Collection | Proposal | *Unknown* | Geospatial quality and accuracy of collections, such as horizontal and vertical accuracy. |
| [Raster](https://github.com/stac-extensions/raster) | raster | Collection, Item | Candidate | 1.1.0 | Describes raster assets at band level (one or multiple) with specific information such as data type, unit, number of bits used, nodata. |
| [SAR](https://github.com/stac-extensions/sar) | sar | Collection, Item | Candidate | 1.0.0 | Covers synthetic-aperture radar data that represents a snapshot of the earth for a single date and time. |
| [Satellite](https://github.com/stac-extensions/sat) | sat | Collection, Item | Candidate | 1.0.0 | Satellite related metadata for data collected from satellites. |
| [Scanning](https://github.com/linz/stac/tree/master/extensions/scanning)* | scan | Collection, Item | *WIP* | *Unknown* | Scanning related metadata, such as the scan date and time. Especially useful for digitised images. |
| [Scientific Citation](https://github.com/stac-extensions/scientific) | sci | Collection, Item | Stable | 1.0.0 | Metadata that indicate from which publication data originates and how the data itself should be cited or referenced. |
| [Single File STAC](https://github.com/stac-extensions/single-file-stac) | - | Collection, Item | Deprecated | **Unreleased** | An extension to provide a set of Collections and Items within a single file STAC. |
| [Solar System](https://github.com/thareUSGS/ssys)* | ssys | Catalog, Collection, Item | *Unknown* | 1.0.0 | SSYS STAC Extension Specification |
| [Stats](https://github.com/stac-extensions/stats) | stats | Catalog, Collection | Pilot | 0.2.0 | Describes the number of items, extensions and assets that are contained in a STAC catalog. |
| [Storage](https://github.com/stac-extensions/storage) | storage | Asset, Item | Pilot | 1.0.0 | Provides additional fields relating to how the asset is stored in the cloud |
| [Subjects](https://github.com/stac-extensions/subjects) | subjects | Collection, Item | *WIP* | **Unreleased** | Subjects Extension Specification |
| [Table](https://github.com/stac-extensions/table) | table | Collection, Item | Pilot | 1.2.0 | Describes tabular data assets using a list of Column objects. Tables can be specified in Collections. |
| [Tiled Assets](https://github.com/stac-extensions/tiled-assets) | tiles | Catalog, Collection, Item | *WIP* | **Unreleased** | Allows to specify numerous assets using asset templates via tile matrices and dimensions. |
| [Time Series](https://github.com/stac-extensions/timeseries) | ts | Collection, Item | Deprecated | **Unreleased** | Time Series STAC Extension Specification  |
| [Timestamps](https://github.com/stac-extensions/timestamps) | - | Catalog, Collection, Item | Pilot | 1.1.0 | Allows to specify numerous additional timestamps for assets and metadata. |
| [U.S. Fish & Wildlife Service (FWS) National Wetlands Inventory (NWI)](https://github.com/stac-extensions/usfws-nwi) | fws_nwi | Collection, Item | Proposal | 1.0.0 | Describes the U.S. Fish & Wildlife Service (FWS) National Wetlands Inventory (NWI) products |
| [Versioning Indicators](https://github.com/stac-extensions/version) | - | Collection, Item | Candidate | 1.1.0 | Provides fields and link relation types to provide a version and indicate deprecation. |
| [Video](https://github.com/stac-extensions/video) | video | Collection, Item | Proposal | 1.0.0 | Provides a way to describe video assets. |
| [View Geometry](https://github.com/stac-extensions/view) | view | Collection, Item | Stable | 1.0.0 | View Geometry adds metadata related to angles of sensors and other radiance angles that affect the view of resulting data. |
| [Virtual Assets](https://github.com/stac-extensions/virtual-assets) | virtual | Collection, Item | *WIP* | **Unreleased** | Allows the description of virtual assets composed from 2 or more assets with cross references and repositioning. |
| [Web Map Links](https://github.com/stac-extensions/web-map-links) | none, but each relat | Catalog, Collection, Item | *WIP* | **Unreleased** | Allows to provide links to web maps for visualization purposes. Currently, OGC WMTS and XYZ are supported. |
| [xarray Assets](https://github.com/stac-extensions/xarray-assets) | xarray | Asset | Pilot | 1.0.0 | This extension helps users open STAC Assets with xarray. It gives a place for catalog maintainers to specify various required or recommended options. |

* **Last updated:** Jan 27 2023, 01:18 
* **Count:** 54

### Grouped by maturity


#### Stable

* [Electro-Optical](https://github.com/stac-extensions/eo)

* [File Info](https://github.com/stac-extensions/file)

* [Item Assets Definition](https://github.com/stac-extensions/item-assets)

* [Projection](https://github.com/stac-extensions/projection)

* [Scientific Citation](https://github.com/stac-extensions/scientific)

* [View Geometry](https://github.com/stac-extensions/view)


#### Candidate

* [Datacube](https://github.com/stac-extensions/datacube)

* [Processing](https://github.com/stac-extensions/processing)

* [Raster](https://github.com/stac-extensions/raster)

* [SAR](https://github.com/stac-extensions/sar)

* [Satellite](https://github.com/stac-extensions/sat)

* [Versioning Indicators](https://github.com/stac-extensions/version)


#### Pilot

* [Alternate Assets](https://github.com/stac-extensions/alternate-assets)

* [Anonymized Location](https://github.com/stac-extensions/anonymized-location)

* [CARD4L (Optical and SAR)](https://github.com/stac-extensions/card4l)

* [Classification](https://github.com/stac-extensions/classification)

* [Grid](https://github.com/stac-extensions/grid)

* [Label](https://github.com/stac-extensions/label)

* [Military Grid Reference System](https://github.com/stac-extensions/mgrs)

* [NOAA Geostationary Operational Environmental Satellite (GOES)](https://github.com/stac-extensions/goes)

* [NOAA MRMS QPE](https://github.com/stac-extensions/noaa-mrms-qpe)

* [Order](https://github.com/stac-extensions/order)

* [Point Cloud](https://github.com/stac-extensions/pointcloud)

* [Stats](https://github.com/stac-extensions/stats)

* [Storage](https://github.com/stac-extensions/storage)

* [Table](https://github.com/stac-extensions/table)

* [Timestamps](https://github.com/stac-extensions/timestamps)

* [xarray Assets](https://github.com/stac-extensions/xarray-assets)


#### Proposal

* [CF](https://github.com/Fred-Leclercq/stac-CF-extention)*

* [Forecast](https://github.com/stac-extensions/forecast)

* [ML Model](https://github.com/stac-extensions/ml-model)

* [Quality](https://github.com/linz/stac/tree/master/extensions/quality)*

* [U.S. Fish & Wildlife Service (FWS) National Wetlands Inventory (NWI)](https://github.com/stac-extensions/usfws-nwi)

* [Video](https://github.com/stac-extensions/video)


#### WIP

* [Accuracy](https://github.com/stac-extensions/accuracy)

* [Aerial Photography](https://github.com/linz/stac/tree/master/extensions/aerial-photo)*

* [Camera](https://github.com/linz/stac/tree/master/extensions/camera)*

* [Composite](https://github.com/stac-extensions/composite)

* [Film](https://github.com/linz/stac/tree/master/extensions/film)*

* [Hyperspectral Imagery](https://github.com/stac-extensions/hsi)

* [InSAR](https://github.com/stac-extensions/insar)

* [Language (I18N)](https://github.com/stac-extensions/language)

* [ML AOI](https://github.com/stac-extensions/ml-aoi)

* [Perspective Imagery](https://github.com/stac-extensions/perspective-imagery)

* [Scanning](https://github.com/linz/stac/tree/master/extensions/scanning)*

* [Subjects](https://github.com/stac-extensions/subjects)

* [Tiled Assets](https://github.com/stac-extensions/tiled-assets)

* [Virtual Assets](https://github.com/stac-extensions/virtual-assets)

* [Web Map Links](https://github.com/stac-extensions/web-map-links)


#### Deprecated

* [Single File STAC](https://github.com/stac-extensions/single-file-stac)

* [Time Series](https://github.com/stac-extensions/timeseries)



## Adding a new extension

The general idea on how to [extend STAC](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md#extending-stac)
and [propose new extensions](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md#proposing-new-extensions) is explained on [the page about extensions in the stac-spec repository](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md).

### Using the stac-extensions template

**Create the repository:**

* Go to [template repository](https://github.com/stac-extensions/template), hit the green 'Use this template' button and choose 'Create a new repository'.
* Be sure to pick the right place ('Owner' and 'Repository name') to create it. You can request (via Gitter or e-mail) to become a member of the stac-extensions organization or put the next repository under your personal account or any other organization.
* Add a concise and clear description of the extension, it will be used as a description in the list above!
* Click 'Include all branches' for the CI to write correctly.
* Finish this by clicking the 'Create repository from template' button

**Write your extension:**

* In the repository 'Settings' go to 'Pages' and set the 'Source' to 'Deploy from a branch' and for the 'Branch' select 'gh-pages' and '/ (root)'
* Update the title, identifier, field name prefix, scope, and owner. Don't mess around with the formatting or structure as this will be used to generate the table above!
* Update the fields, select where they can be used, add documentation, etc. in the README.md
* Update the JSON Schema accordingly in schemas/schema.json
* Add examples
* Go through the files and update everything that is still named 'template' (the easiest way is to let an IDE/Editor search through all the files for 'template')
* Run the tests
* Update the changelog
* Let people discuss your extension, e.g. via Gitter
* Eventually, release the extension via GitHub Releases

You can add external/community extensions to the list above by editing the [config file](https://github.com/stac-extensions/stac-extensions.github.io/edit/main/python/config.py)
and creating a Pull Request for the change. All extensions hosted in the stac-extensions organization will be added automatically each night.