# Change Log

## Version 3.0

Version 3 contains a new version of the Skeleton with different, hopefully more useful names for the IIIF classes. The renamed classes are below:

Classes renamed:

 * Model -> AbstractIIIFResource (top level class for Manifests, Collections, AnnotationPages and Annotation Collections)
 * ExternalItem -> LinkedResource
 * External -> LinkedResources (list of linked resources)
 * HomepageItem -> Homepage
 * Homepage -> Homepages (list of homepages)
 * ProviderItem -> Provider
 * Provider -> Providers (list of providers)
 * ServiceItem -> ServiceV3
 * ServiceItem1 -> ServiceV2
 * ResourceItem -> AnnotationBody
 * BodyItem -> Body (list of resources which are one of AnnotationBody, TextualBody or SpecificResource)
 * ResourceItem1 -> TextualBody
 * SelectorItem -> PointSelector
 * SelectorItem1 -> FragmentSelector
 * SelectorItem2 -> SVGSelector
 * SelectorItem3 -> ImageAPISelector

New classes:
 * AnnotationCollectionRef
 * AnnotationCollectionRefExtended
 * AnnotationPageRefExtended

Classes removed:
 * Item (Duplicate of Canvas)
 * AnnoTargetItem (replaced by SpecificResource)