# STAC Extensions

The [stac-extensions](https://github.com/stac-extensions/) github organization is a home for extensions to the
[SpatioTemporal Asset Catalog](https://github.com/radiantearth/stac-spec) specification.

To learn about STAC and Extensions start with the [extensions](https://github.com/radiantearth/stac-spec/tree/master/extensions)
section of the core specification. It explains how extensions work, lists all the known extensions, and has
instructions for how to go about '[extending STAC](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md#extending-stac)'.

The [stac-extensions](https://github.com/stac-extensions/) github organization is a home for many of the leading 'community extensions',
providing a neutral home for collaboration. Many of these used to be in the core
[stac-spec repository](https://github.com/radiantearth/stac-spec), but were removed for 1.0.0 so they could evolve at their
own pace, instead of having to follow the core STAC release cycle.

## List of STAC Extensions

This is meant to be the definitive list of STAC Extensions, but not all of them may be part of this GitHub organization
and are hosted externally instead.

| Title | Field Name Prefix | Scope | Maturity | Version | Description |
| ----- | ----------------- | ----- | -------- | ---------- | ----------- |
| [Accuracy](https://github.com/stac-extensions/accuracy) | accuracy | Collection, Item | Proposal | **Unreleased** | Fields to provide estimates of accuracy, both geometric and measurement (e.g., radiometric) accuracy. |
| [Aerial Photography](https://github.com/linz/stac/tree/master/extensions/aerial-photo) | aerial-photo | Collection, Item | Work In Progress (Before proposal) | *Unknown* | Aerial photography related metadata, such as run, sequence number, altitude and scale. |
| [Alternate Assets](https://github.com/stac-extensions/alternate-assets) | - | Asset | Proposal | 1.1.0 | Describes alternate locations and mirrors of assets |
| [Anonymized Location](https://github.com/stac-extensions/anonymized-location) | anon | Collection, Item | Proposal | 1.0.0 | Provides a way to anonymize location data |
| [CARD4L (Optical and SAR)](https://github.com/stac-extensions/card4l) | card4l | Item | Proposal | 0.1.0 | Describes how to comply to the CEOS CARD4L specifications (SAR and Optical) with STAC |
| [Camera](https://github.com/linz/stac/tree/master/extensions/camera) | camera | Collection, Item | Work In Progress (Before proposal) | *Unknown* | Camera related metadata, such as focal length and sequence number. Especially useful for aerial imagery surveys. |
| [Classification](https://github.com/stac-extensions/classification) | classification | Collection, Item | Proposal | 1.1.0 | Describes categorical values and bitfields to give values in a file a certain meaning (classification). |
| [Composite](https://github.com/stac-extensions/composite) | composite | Item | Proposal | **Unreleased** | Defines how virtual assets can be composed from existing assets in STAC |
| [Datacube](https://github.com/stac-extensions/datacube) | cube | Collection, Item | Proposal | 2.1.0 | Datacube related metadata to describe their dimensions and variables. |
| [Electro-Optical](https://github.com/stac-extensions/eo) | eo | Collection, Item | Stable | 1.0.0 | Covers electro-optical data that represents a snapshot of the Earth. It could consist of cloud cover and multiple spectral bands, for example visible bands, infrared bands, red edge bands and panchromatic bands. |
| [File Info](https://github.com/stac-extensions/file) | file | Catalog, Collection, Item | Proposal | 2.1.0 | Specifies file-related details such as size, data type and checksum for assets and links in STAC. |
| [Film](https://github.com/linz/stac/tree/master/extensions/film) | film | Collection, Item | Work In Progress (Before proposal) | *Unknown* | Film related metadata, such as roll, negative sequence and other physical attributes. Especially useful for digitised historic aerial imagery surveys. |
| [Forecast](https://github.com/stac-extensions/forecast) | forecast | Collection, Item | Proposal | 0.1.0 | Common fields for (meteorological/weather) forecast data. |
| [Grid](https://github.com/stac-extensions/grid) | grid | Item | Proposal | 1.1.0 | Describes gridded data products, especially the grid code. |
| [Hyperspectral Imagery](https://github.com/stac-extensions/hsi) | hsi | Collection, Item | Proposal | **Unreleased** | Hyperspectral Imagery Extension Specification |
| [InSAR](https://github.com/stac-extensions/insar) | insar | Item | Proposal | **Unreleased** | STAC extension for InSAR |
| [Item Assets Definition](https://github.com/stac-extensions/item-assets) | - | Collection | Proposal | 1.0.0 | Item Assets Definition Specification |
| [Label](https://github.com/stac-extensions/label) | label | Collection, Item | Proposal | 1.0.1 | Label extension |
| [ML AOI](https://github.com/stac-extensions/ml-aoi) | ml-aoi | Collection, Item | Proposal | **Unreleased** | An Item and Collection extension to provide labeled training data for machine learning models. |
| [ML Model](https://github.com/stac-extensions/ml-model) | ml-model | Collection, Item | Proposal | 1.0.0 | ML Model Extension Specification |
| [Military Grid Reference System](https://github.com/stac-extensions/mgrs) | mgrs | Item | Proposal | 1.0.0 | MGRS STAC Extension |
| [NOAA Geostationary Operational Environmental Satellite (GOES)](https://github.com/stac-extensions/goes) | goes | Collection, Item | Proposal | 1.0.0 | STAC Extension for NOAA GOES (Geostationary Operational Environmental Satellite) products |
| [NOAA MRMS QPE](https://github.com/stac-extensions/noaa-mrms-qpe) | noaa_mrms_qpe | Collection, Item | Proposal | 1.0.0 | None |
| [Order](https://github.com/stac-extensions/order) | order | Collection, Item | Proposal | 1.0.0 | Order Extension Specification |
| [Perspective Imagery](https://github.com/stac-extensions/perspective-imagery) | pers | Collection, Item | Proposal | **Unreleased** | STAC extension for describing perspective imagery collected by photogrammetric or non-photogrammetric cameras |
| [Point Cloud](https://github.com/stac-extensions/pointcloud) | pc | Collection, Item | Proposal | 1.0.0 | Point Cloud Extension Specification |
| [Processing](https://github.com/stac-extensions/processing) | processing | Collection, Item | Proposal | 1.1.0 | Processing Extension Specification |
| [Projection](https://github.com/stac-extensions/projection) | proj | Collection, Item | Stable | 1.0.0 | Projection Extension Specification |
| [Quality](https://github.com/linz/stac/tree/master/extensions/quality) | quality | Collection | Proposal | *Unknown* | Geospatial quality and accuracy of collections, such as horizontal and vertical accuracy. |
| [Raster](https://github.com/stac-extensions/raster) | raster | Collection, Item | Proposal | 1.1.0 | Raster Extension Specification |
| [SAR](https://github.com/stac-extensions/sar) | sar | Collection, Item | Proposal | 1.0.0 | SAR Extension Specification |
| [Satellite](https://github.com/stac-extensions/sat) | sat | Collection, Item | Proposal | 1.0.0 | Satellite Extension for STAC, providing fields to help describe satellite data collection |
| [Scanning](https://github.com/linz/stac/tree/master/extensions/scanning) | scan | Collection, Item | Work In Progress (Before proposal) | *Unknown* | Scanning related metadata, such as the scan date and time. Especially useful for digitised images. |
| [Scientific Citation](https://github.com/stac-extensions/scientific) | sci | Collection, Item | Stable | 1.0.0 | Scientific Citation Extension Specification |
| [Single File STAC](https://github.com/stac-extensions/single-file-stac) | - | Collection, Item | **Deprecated** | **Unreleased** | Single File STAC Specification |
| [Stats](https://github.com/stac-extensions/stats) | *Unknown* | Catalog, Collection | *Unknown* | 0.2.0 | Extension to describe number of items, extensions and assets that are contained in a STAC catalog. |
| [Storage](https://github.com/stac-extensions/storage) | storage | Asset, Item | Proposal | 1.0.0 | Storage Extension Specification |
| [Subjects](https://github.com/stac-extensions/subjects) | subjects | Collection, Item | Proposal | **Unreleased** | Subjects Extension Specification |
| [Table](https://github.com/stac-extensions/table) | table | Collection, Item | Proposal | 1.2.0 | None |
| [Template](https://github.com/stac-extensions/vector-label) | template | Collection, Item | Proposal | **Unreleased** | Vector Label Extension Specification |
| [Tiled Assets](https://github.com/stac-extensions/tiled-assets) | tiles | Catalog, Collection, Item | Proposal | **Unreleased** | Tiled Assets specification |
| [Time Series](https://github.com/stac-extensions/timeseries) | ts | Collection, Item | Proposal | **Unreleased** | Time Series STAC Extension Specification  |
| [Timestamps](https://github.com/stac-extensions/timestamps) | - | Collection, Item | Proposal | 1.0.0 | Timestamps Extension Specification |
| [U.S. Fish & Wildlife Service (FWS) National Wetlands Inventory (NWI)](https://github.com/stac-extensions/usfws-nwi) | fws_nwi | Collection, Item | Proposal | 1.0.0 | None |
| [Versioning Indicators](https://github.com/stac-extensions/version) | - | Collection, Item | Proposal | 1.1.0 | Versioning Indicators Extension Specification |
| [Video](https://github.com/stac-extensions/video) | video | Collection, Item | Proposal | 1.0.0 | Provides a way to describe video assets. |
| [View Geometry](https://github.com/stac-extensions/view) | view | Collection, Item | Stable | 1.0.0 | View Extension Specification |
| [Virtual Assets](https://github.com/stac-extensions/virtual-assets) | virtual | Collection, Item | Proposal | **Unreleased** | Virtual-Assets Extension Specification |
| [Web Map Links](https://github.com/stac-extensions/web-map-links) | none, but each relation type has potentially a distinct prefix for additional data (e.g. `wmts` and `xyz`) | Catalog, Collection, Item | Proposal | **Unreleased** | Defines how to link to web mapping services |
| [xarray Assets](https://github.com/stac-extensions/xarray-assets) | xarray | Asset | Proposal | 1.0.0 | None |<br>

Last updated: Dec 06 2022, 15:26 

## Adding a new extension

The general idea on how to [extend STAC](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md#extending-stac)
and [propose new extensions](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md#proposing-new-extensions) is explained on [the page about extensions in the stac-spec repository](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md).

### Using the stac-extensions template

**Create the repository:**

* Go to [template repository](https://github.com/stac-extensions/template), hit the green 'Use this template' button and choose 'Create a new repository'.
* Be sure to pick the right place ('Owner' and 'Repository name') to create it. You can request (via Gitter or e-mail) to become a member of the stac-extensions organization or put the next repository under your personal account or any other organization.
* Add a concise and clear description about the extension, it will be used as a description in the list above!
* Click 'Include all branches' for the CI to write correctly.
* Finish this by clicking the 'Create repository from template' button

**Write your extension:**

* In the repository 'Settings' go to 'Pages' and set the 'Source' to 'Deploy from a branch' and for the 'Branch' select 'gh-pages' and '/ (root)'
* Update the title, identifier, field name prefix, scope and owner. Don't mess around with the formatting or structure as this will be used to generate the table above!
* Update the fields, select where they can be used, add documentation etc. in the README.md
* Update the JSON Schema accordingly in schemas/schema.json
* Add examples
* Go through the files and update everything that is still named 'template' (the easiest way is to let an IDE/Editor search through all the files for 'template')
* Run the tests
* Update the changelog
* Let people discuss your extension, e.g. via Gitter
* Eventually, release the extension via GitHub Releases