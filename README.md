# STAC Extensions

The [stac-extensions](https://github.com/stac-extensions/) github organization is a home for extensions to the
[SpatioTemporal Asset Catalog](https://github.com/radiantearth/stac-spec) specification.

To learn about STAC and Extensions start with the [extensions](https://github.com/radiantearth/stac-spec/tree/master/extensions)
section of the core specification. It explains how extensions work, lists all the known extensions, and has
instructions for how to go about '[extending STAC](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md#extending-stac)'.

The [stac-extensions](https://github.com/stac-extensions/) github organization is a home for many of the leading 'community extensions',
providing a neutral home for collaboration. Many of these used to be in the core [stac-spec
repository]((https://github.com/radiantearth/stac-spec)), but were removed for 1.0.0 so they could evolve at their
own pace, instead of having to follow the core STAC release cycle.

## List of STAC Extensions

The definitive list of STAC Extensions is in the core spec repository, in the [Extensions 
README](https://github.com/radiantearth/stac-spec/blob/master/extensions/README.md). This includes the official core
extensions, as well as a complete list of 'community' extensions. A subset of the community extensions use this 
stac-extensions GitHub organization, and those are listed in the next section.

### Extensions in stac-extensions organization

These extensions add new fields or semantics to STAC objects.

| Extension Title                                              | Field Name Prefix | Scope                     | Maturity   | Latest Version | Description                                                  |
| ------------------------------------------------------------ | ----------------- | ------------------------- | ---------- | ---------- | ------------------------------------------------------------ |
| [CARD4L](https://github.com/stac-extensions/card4l)          | card4l.           | Item                      | *Proposal* | **not published**         | How to comply to the CEOS CARD4L product family specifications (Optical and SAR) |
| [Data Cube](https://github.com/stac-extensions/datacube)     | cube              | Item, Collection          | *Pilot* | v1.0.0    | Data Cube related metadata, especially to describe their dimensions. |
| [Electro-Optical](https://github.com/stac-extensions/eo)     | eo                | Item, Collection          | Stable     | v1.0.0     | Covers electro-optical data that represents a snapshot of the Earth for a single date and time. It could consist of multiple spectral bands, for example visible bands, infrared bands, red edge bands and panchromatic bands. The extension provides common fields like bands, cloud cover, gsd and more. |
| [File Info](https://github.com/stac-extensions/file)         | file              | Item, Collection          | *Pilot* | v2.0.0     | Provides a way to specify file details such as size, data type and checksum for assets in Items and Collections. |
| [Item Asset Definition](https://github.com/stac-extensions/item-assets) | -      | Collection                | *Pilot* | v1.0.0     | Provides a way to specify details about what assets may be found in Items belonging to a Collection. |
| [Label](https://github.com/stac-extensions/label)            | label             | Item, Collection          | *Pilot* | v1.0.0        | Items that relate labeled AOIs with source imagery           |
| [ML AOI](https://github.com/stac-extensions/ml-aoi)           | ml-aoi            | Item, Collection         | *Proposal*    | **not published**  | An Item and Collection extension to provide labeled training data for machine learning models. |
| [MGRS](https://github.com/stac-extensions/mgrs)              | mgrs              | Item, Collection          | *Proposal*    | **not published**      |                                                              |
| [Point Cloud](https://github.com/stac-extensions/pointcloud) | pc                | Item, Collection          | *Pilot* | v1.0.0     | Provides a way to describe point cloud datasets. The point clouds can come from either active or passive sensors, and data is frequently acquired using tools such as LiDAR or coincidence-matched imagery. |
| [Processing](https://github.com/stac-extensions/processing)  | processing        | Item, Collection          | *Proposal* | v1.0.0     | Indicates from which processing chain data originates and how the data itself has been produced. |
| [Projection](https://github.com/stac-extensions/projection)  | proj              | Item, Collection          | Stable     | v1.0.0        | Provides a way to describe Items whose assets are in a geospatial projection. |
| [Raster](https://github.com/stac-extensions/raster)          | raster            | Item, Collection          | *Pilot*    | v1.0.0     | Describes raster assets at band level (one or multiple) with specific information such as data type, unit, number of bits used, nodata. |
| [SAR](https://github.com/stac-extensions/sar)                | sar               | Item, Collection          | *Pilot* | v1.0.0        | Covers synthetic-aperture radar data that represents a snapshot of the earth for a single date and time. |
| [Satellite](https://github.com/stac-extensions/sat)          | sat               | Item, Collection          | *Pilot* | v1.0.0        | Satellite related metadata for data collected from satellites. |
| [Scientific Citation](https://github.com/stac-extensions/scientific) | sci               | Item, Collection  | Stable     | v1.0.0        | Metadata that indicate from which publication data originates and how the data itself should be cited or referenced. |
| [Single File STAC](https://github.com/stac-extensions/single-file-stac) | -                 | Catalog        | *Proposal* | **not published**      | An extension to provide a set of Collections and Items within a single file STAC. |
| [Storage](storage/README.md)                                 | storage           | Item, Collection          | *Proposal*     | **not published**      | Provides additional fields relating to how the asset is stored. |
| [Tiled Assets](https://github.com/stac-extensions/tiled-assets) | tiles             | Item, Catalog, Collection | *Proposal* | **not published**      | Allows to specify numerous assets using asset templates via tile matrices and dimensions. |
| [Timestamps](https://github.com/stac-extensions/timestamps)  | -                 | Item, Collection          | *Pilot* | v1.0.0        | Allows to specify numerous timestamps for assets and metadata. |
| [Versioning Indicators](https://github.com/stac-extensions/version) | -                 | Item, Collection   | *Pilot* | v1.0.0        | Provides fields and link relation types to provide a version and indicate deprecation. |
| [View Geometry](https://github.com/stac-extensions/view)     | view              | Item, Collection          | Stable     | v1.0.0      | View Geometry adds metadata related to angles of sensors and other radiance angles that affect the view of resulting data |
| [Virtual Assets](https://github.com/stac-extensions/virtual-assets)     | virtual              | Item, Collection          | *Proposal*     | **not published**       | Allows the description of virtual assets composed from 2 or more assets with cross references and repositioning. |

## Extension Maturity

Extensions in this directory are meant to evolve to maturity, and thus may be in different states
in terms of stability and number of implementations. All extensions included must include a
maturity classification, so that STAC spec users can easily get a sense of how much they can count
on the extension.

| Maturity Classification |  Min Impl # | Description | Stability |
| ----------------------- | ----------- | ----------- | --------- |
| Proposal                | 0           | An idea put forward by a community member to gather feedback | Not stable - breaking changes almost guaranteed as implementers try out the idea. |
| Pilot                   | 1           | Idea is fleshed out, with examples and a JSON schema, and implemented in one or more catalogs. Additional implementations encouraged to help give feedback | Approaching stability - breaking changes are not anticipated but can easily come from additional feedback |
| Candidate               | 3           | A number of implementers are using it and are standing behind it as a solid extension. Can generally count on an extension at this maturity level | Mostly stable, breaking changes require a new version and minor changes are unlikely. The extension has a [code owner](../.github/CODEOWNERS). |
| Stable                  | 6           | Highest current level of maturity. The community of extension maintainers commits to a STAC review process for any changes, which are not made lightly. | Completely stable, all changes require a new version number and review process. |
| Deprecated              | N/A         | A previous extension that has likely been superseded by a newer one or did not work out for some reason. | DO NOT USE, is not supported |

Maturity mostly comes through diverse implementations, so the minimum number of implementations
column is the main gating function for an extension to mature. But extension authors can also
choose to hold back the maturity advancement if they don't feel they are yet ready to commit to
the less breaking changes of the next level.

A 'mature' classification level will likely be added once there are extensions that have been
stable for over a year and are used in twenty or more implementations.

## Adding a new extension

### Using the stac-extensions template

TODO: Overview of using the template.

Step-by-step (add an image or two)

* Request to become a member of stac-extensions if you want to it to have that visibility, or put in your personal or org's repo
* Go to [template repo](https://github.com/stac-extensions/template) and hit the green 'Use this template' button.
* Be sure to pick the right place to create it.
* Description - briefly describe it
* click 'copy all branches' for the CI to write correctly.
* Title your table properly - likely is just item properties or collection fields, though some are both. But make your heading clear.
* Schemas - start with the templates, and add in your properties.
* In 'settings' turn on github pages (unless we find a way to do this automatically) - probaby add a picture for this.
