# STAC Extensions

The [stac-extensions](https://github.com/stac-extensions/) github organization is a home for extensions to the
[SpatioTemporal Asset Catalog](https://github.com/radiantearth/stac-spec) specification.

TODO: Flesh out more, on what's in this repo, what's in core, what may be in other repos, link to extensions section

The core STAC specification 
defines only a minimal core, but is designed for extension. It is expected that most real-world
implementations will use several extensions to fully describe their data.  

Extensions to the core STAC specification provide additional JSON fields that can be used to better describe
the data. Most tend to be about describing a particular domain or type of data, but some imply
functionality. 

Extensions should include a JSON Schema precisely describing the structure, a natural language description of the fields, and thorough examples.
Any data provider can create a proprietary extension, and when providers work together to share fields between
them they can create a shared extension and include it in the STAC repository.

Anyone is welcome to create an extension (see section 'Extending STAC'), and is encouraged to at least link 
to the extension from here. The [third-party / vendor extensions](#third-party--vendor-extensions) section is 
for the sharing of extensions. As third-parties create useful extensions for their implementation, it is 
expected that others will make use
of it, and then evolve to make it a 'community extension', that several providers maintain
together. For now anyone from the community is welcome to use this extensions/ folder of the
stac-spec repository to collaborate.

## General Conventions

1. Additional attributes relating to an [Item](../item-spec/item-spec.md) should be added into the Item Properties object, rather than directly in the Item object. 
2. In general, additional attributes that apply to an Item Asset should also be allowed in Item Properties and vice-versa.
For example, the `eo:bands` attribute may be used in Item Properties to describe the aggregation of all bands available in 
the Item Asset objects contained in the Item, but may also be used in an individual Item Asset to describe only the bands available in that asset.
3. Additional attributes relating to a [Catalog](../catalog-spec/catalog-spec.md) or [Collection](../collection-spec/collection-spec.md) should be added to the root of the object. 

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

## List of STAC Extensions

TODO: Link to core extensions

### Extensions in stac-extensions organization

These extensions add new fields or semantics to STAC objects.

| Extension Title                                  | Identifier        | Field Name Prefix   | Scope                     | Maturity   | Description |
| ------------------------------------------------ | ----------------- | ------------------- | ------------------------- | ---------- | ----------- |
| [Data Cube](datacube/README.md)                  | datacube          | cube                | Item, Collection          | *Proposal* | Data Cube related metadata, especially to describe their dimensions. |
| [File Info](file/README.md)                      | file              | file                | Item, Collection          | *Proposal* | Provides a way to specify file details such as size, data type and checksum for assets in Items and Collections. |
| [Item Asset Definition](item-assets/README.md)   | item-assets       | -                   | Collection                | *Proposal* | Provides a way to specify details about what assets may be found in Items belonging to a Collection. |
| [Label](label/README.md)                         | label             | label               | Item                      | *Proposal* | Items that relate labeled AOIs with source imagery |
| [Point Cloud](pointcloud/README.md)              | pointcloud        | pc                  | Item                      | *Proposal* | Provides a way to describe point cloud datasets. The point clouds can come from either active or passive sensors, and data is frequently acquired using tools such as LiDAR or coincidence-matched imagery. |
| [Processing](processing/README.md)               | processing        | processing          | Item, Collection          | *Proposal* | Indicates from which processing chain data originates and how the data itself has been produced. |
| [SAR](sar/README.md)                             | sar               | sar                 | Item                      | *Proposal* | Covers synthetic-aperture radar data that represents a snapshot of the earth for a single date and time. |
| [Satellite](sat/README.md)                       | sat               | sat                 | Item                      | *Proposal* | Satellite related metadata for data collected from satellites. |
| [Single File STAC](single-file-stac/README.md)   | single-file-stac  | -                   | Catalog                   | *Proposal* | An extension to provide a set of Collections and Items within a single file STAC. |
| [Tiled Assets](tiled-assets/README.md)           | tiled-assets      | tiles               | Item, Catalog, Collection | *Proposal* | Allows to specify numerous assets using asset templates via tile matrices and dimensions. |
| [Timestamps](timestamps/README.md)               | timestamps        | -                   | Item                      | *Proposal* | Allows to specify numerous timestamps for assets and metadata. |
| [Versioning Indicators](version/README.md)       | version           | -                   | Item, Collection          | *Proposal* | Provides fields and link relation types to provide a version and indicate deprecation. |
| [CARD4L](https://github.com/stac-extensions/card4l) | card4l         | card4l.             | Item  | *Proposal* | How to comply to the CEOS CARD4L product family specifications (Optical and SAR) |

## Proposed extensions

The following extensions are proposed through the
[STAC issue tracker](https://github.com/radiantearth/stac-spec/issues?q=is%3Aissue+is%3Aopen+label%3A%22new+extension%22) and are considered to be
implemented. If you would find any of these helpful or are considering to implement a similar
extension, please get in touch through the referenced issues:

- [Drone Extension](https://github.com/radiantearth/stac-spec/issues/149)
- [Full Motion Video Extension](https://github.com/radiantearth/stac-spec/issues/156)
- [Storage Extensions](https://github.com/radiantearth/stac-spec/issues/148)
- [gRPC STAC Extensions](https://github.com/radiantearth/stac-spec/issues/575)

## Using the stac-extensions template

TODO
