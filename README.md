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

Last Updated: Aug 12 23:10  2021 UTC.

| Extension Title | Field Name Prefix | Scope | Maturity | Published? | Description |
| :-------------- | :---------------- | :---- | :------- | ---------- | :---------- |
   [Alternate Assets](https://github.com/stac-extensions/alternate-assets)|-|Asset|Proposal|-|Extension for describing alternate locations and mirrors of assets|
   [Anonymized Location](https://github.com/stac-extensions/anonymized-location)|anon|Item, Collection|Proposal|-|Anonymized Location Extension Specification|
   [](https://github.com/stac-extensions/card4l)||||-|Extension that explains how to comply to the CEOS CARD4L specifications (SAR and Optical)|
   [Template](https://github.com/stac-extensions/classification)|template|Item, Collection|Proposal|-|An extension to give values in a file a certain meaning (classification).|
   [Composite](https://github.com/stac-extensions/composite)|composite|Item|Proposal|-|Composite Extension Specification|
   [Datacube](https://github.com/stac-extensions/datacube)|cube|Item, Collection|Proposal|-|Data cube Extension Specification|
   [Electro-Optical](https://github.com/stac-extensions/eo)|eo|Item, Collection|Stable|-|EO Extension Specification|
   [File Info](https://github.com/stac-extensions/file)|file|Item, Collection|Proposal|-|File Info Extension Specification|
   [Item Assets Definition](https://github.com/stac-extensions/item-assets)|-|Collection|Proposal|-|Item Assets Definition Specification|
   [Label](https://github.com/stac-extensions/label)|label|Item, Collection|Proposal|-|Label extension|
   [Military Grid Reference System](https://github.com/stac-extensions/mgrs)|mgrs|Item|Proposal|-|MGRS STAC Extension|
   [ML AOI](https://github.com/stac-extensions/ml-aoi)|ml-aoi|Item, Collection|Proposal|-|An Item and Collection extension to provide labeled training data for machine learning models.|
   [Order](https://github.com/stac-extensions/order)|order|Item, Collection|Proposal|-|Order Extension Specification|
   [Point Cloud](https://github.com/stac-extensions/pointcloud)|pc|Item, Collection|Proposal|-|Point Cloud Extension Specification|
   [Processing](https://github.com/stac-extensions/processing)|processing|Item, Collection|Proposal|-|Processing Extension Specification|
   [Projection](https://github.com/stac-extensions/projection)|proj|Item, Collection|Stable|-|Projection Extension Specification|
   [Raster](https://github.com/stac-extensions/raster)|raster|Item, Collection|Proposal|-|Raster Extension Specification|
   [Remote Data (Example Extension)](https://github.com/stac-extensions/remote-data)|rd|Item, Collection|Proposal|-|Example Extension|
   [SAR](https://github.com/stac-extensions/sar)|sar|Item, Collection|Proposal|-|SAR Extension Specification|
   [Satellite](https://github.com/stac-extensions/sat)|sat|Item, Collection|Proposal|-|Satellite Extension for STAC, providing fields to help describe satellite data collection|
   [Scientific Citation](https://github.com/stac-extensions/scientific)|sci|Item, Collection|Stable|-|Scientific Citation Extension Specification|
   [Single File STAC](https://github.com/stac-extensions/single-file-stac)|-|Item, Collection|Proposal|-|Single File STAC Specification|
   [](https://github.com/stac-extensions/stac-extensions.github.io)||||-|Overview of STAC Extensions, with advice on creating new extensions|
   [Storage](https://github.com/stac-extensions/storage)|storage|Item, Asset|Proposal|-|Storage Extension Specification|
   [Template](https://github.com/stac-extensions/template)|template|Item, Collection|Proposal|-|A template repository for new extensions. It enables CI for schema publishing and proposes some core structures.|
   [Tiled Assets](https://github.com/stac-extensions/tiled-assets)|tiles|Item, Catalog, Collection|Proposal|-|Tiled Assets specification|
   [Timestamps](https://github.com/stac-extensions/timestamps)|-|Item, Collection|Proposal|-|Timestamps Extension Specification|
   [Versioning Indicators](https://github.com/stac-extensions/version)|-|Item, Collection|Proposal|-|Versioning Indicators Extension Specification|
   [View Geometry](https://github.com/stac-extensions/view)|view|Item, Collection|Stable|-|View Extension Specification|
   [Virtual Assets](https://github.com/stac-extensions/virtual-assets)|virtual|Item, Collection|Proposal|-|Virtual-Assets Extension Specification|## Extension Maturity

Extensions in this directory are meant to evolve to maturity, and thus may be in different states
in terms of stability and number of implementations. All extensions included must include a
maturity classification, so that STAC spec users can easily get a sense of how much they can count
on the extension.

| Maturity Classification | Min Impl # | Description                                                                                                                                                | Stability                                                                                                                                      |
| ----------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Proposal                | 0          | An idea put forward by a community member to gather feedback                                                                                               | Not stable - breaking changes almost guaranteed as implementers try out the idea.                                                              |
| Pilot                   | 1          | Idea is fleshed out, with examples and a JSON schema, and implemented in one or more catalogs. Additional implementations encouraged to help give feedback | Approaching stability - breaking changes are not anticipated but can easily come from additional feedback                                      |
| Candidate               | 3          | A number of implementers are using it and are standing behind it as a solid extension. Can generally count on an extension at this maturity level          | Mostly stable, breaking changes require a new version and minor changes are unlikely. The extension has a [code owner](../.github/CODEOWNERS). |
| Stable                  | 6          | Highest current level of maturity. The community of extension maintainers commits to a STAC review process for any changes, which are not made lightly.    | Completely stable, all changes require a new version number and review process.                                                                |
| Deprecated              | N/A        | A previous extension that has likely been superseded by a newer one or did not work out for some reason.                                                   | DO NOT USE, is not supported                                                                                                                   |

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