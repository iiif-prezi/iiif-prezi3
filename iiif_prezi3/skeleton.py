# generated by datamodel-codegen:
#   filename:  iiif_3_0.json
#   timestamp: 2022-10-21T15:13:50+00:00

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from .base import Base
from pydantic import AnyUrl, Extra, Field, PositiveFloat, PositiveInt, constr


class Behavior(Base):
    __root__: List[
        Union[
            constr(regex=r'^auto-advance$'),
            constr(regex=r'^no-auto-advance$'),
            constr(regex=r'^repeat$'),
            constr(regex=r'^no-repeat$'),
            constr(regex=r'^unordered$'),
            constr(regex=r'^individuals$'),
            constr(regex=r'^continuous$'),
            constr(regex=r'^paged$'),
            constr(regex=r'^facing-pages$'),
            constr(regex=r'^non-paged$'),
            constr(regex=r'^multi-part$'),
            constr(regex=r'^together$'),
            constr(regex=r'^sequence$'),
            constr(regex=r'^thumbnail-nav$'),
            constr(regex=r'^no-nav$'),
            constr(regex=r'^hidden$'),
        ]
    ]


class NavDate(Base):
    __root__: datetime


class Rights(Base):
    __root__: Union[AnyUrl, AnyUrl, AnyUrl] = Field(
        ...,
        title="Rights URI isn't from either Creative Commons or RightsStatements.org. Both require http links.",
    )


class ViewingDirection(Base):
    __root__: Union[
        constr(regex=r'^left-to-right$'),
        constr(regex=r'^right-to-left$'),
        constr(regex=r'^top-to-bottom$'),
        constr(regex=r'^bottom-to-top$'),
    ]


class Id(Base):
    __root__: AnyUrl = Field(..., title='Id must be presesnt and must be a URI')


class LngString(Base):
    __root__: Dict[str, List[str]]

    class Config:
        extra = Extra.forbid


class AnnoTargetItem(Base):
    source: Id
    scope: Id


class Choice(Base):
    type: str
    items: List


class BCP47(Base):
    __root__: Union[constr(regex=r'^[a-zA-Z-][a-zA-Z-]*$'), constr(regex=r'^none$')]


class Dimension(Base):
    __root__: PositiveInt


class Duration(Base):
    __root__: PositiveFloat


class Format(Base):
    __root__: constr(regex=r'^[a-z][a-z]*/.*$')


class AnnoSelectorItem(Base):
    type: str
    t: Optional[Duration] = None


class AnnoSelector(Base):
    __root__: Union[AnyUrl, AnnoSelectorItem]


class NavPlace(Base):
    id: Optional[Id] = None
    type: Optional[str] = 'FeatureCollection'
    features: Optional[List[Dict[str, Any]]] = None


class ResourceItem1(Base):
    id: Optional[Id] = None
    type: Optional[constr(regex=r'^TextualBody$')] = 'TextualBody'
    value: str
    format: Optional[Format] = None
    language: Optional[str] = None


class Class(Base):
    id: Id
    type: str
    label: Optional[LngString] = None


class ExternalItem(Class):
    format: Optional[Format] = None
    profile: Optional[str] = None


class External(Base):
    __root__: List[ExternalItem]


class KeyValueString(Base):
    label: LngString
    value: LngString


class SpecificResource(Base):
    id: Optional[Id] = None
    type: Optional[constr(regex=r'^SpecificResource$')] = 'SpecificResource'
    format: Optional[Format] = None
    accessibility: Optional[str] = None
    source: Id
    selector: Union[AnnoSelector, List[AnnoSelector]]


class HomepageItem(Class):
    format: Optional[Format] = None
    language: Optional[List[BCP47]] = None


class Homepage(Base):
    __root__: List[HomepageItem]


class Metadata(Base):
    __root__: List[KeyValueString]


class PartOf(Base):
    __root__: List[Class]


class Item(Class):
    type: Optional[constr(regex=r'^Canvas$')] = 'Canvas'


class SeeAlso(Base):
    __root__: External


class AnnoTarget(Base):
    __root__: Union[AnyUrl, SpecificResource, AnnoTargetItem]


class Model(Base):
    __root__: Union[Manifest, Collection, AnnotationPage]


class AnnotationPage(Base):
    class Config:
        extra = Extra.forbid

    _context: Optional[Any] = Field(None, alias='@context')
    id: Id
    type: Optional[constr(regex=r'^AnnotationPage$')] = 'AnnotationPage'
    label: Optional[LngString] = None
    service: Optional[Service] = None
    thumbnail: Optional[List[Resource]] = None
    items: Optional[List[Annotation]] = None


class Collection(Class):
    type: Optional[constr(regex=r'^Collection')] = Field(
        'Collection',
        description='If you are validating a manifest, you may get this error if there are errors in the manifest. The validator first validates it as a manifest and if that fails it will try and validate it using the other types.',
        title='Are you validating a collection?',
    )
    metadata: Optional[Metadata] = None
    summary: Optional[LngString] = None
    requiredStatement: Optional[KeyValueString] = None
    rights: Optional[Rights] = None
    navDate: Optional[NavDate] = None
    navPlace: Optional[NavPlace] = None
    provider: Optional[Provider] = None
    seeAlso: Optional[SeeAlso] = None
    services: Optional[Service] = None
    service: Optional[Service] = None
    thumbnail: Optional[List[Resource]] = None
    homepage: Optional[Homepage] = None
    behavior: Optional[Behavior] = None
    partOf: Optional[PartOf] = None
    items: Optional[List[Union[ManifestRef, CollectionRef, Collection]]] = None
    annotations: Optional[List[AnnotationPage]] = None


class Manifest(Class):
    _context: Optional[Union[List[AnyUrl], str]] = Field(None, alias='@context')
    id: Id
    label: LngString
    type: Optional[constr(regex=r'^Manifest')] = 'Manifest'
    metadata: Optional[Metadata] = None
    summary: Optional[LngString] = None
    requiredStatement: Optional[KeyValueString] = None
    rendering: Optional[External] = None
    service: Optional[Service] = None
    services: Optional[Service] = None
    viewingDirection: Optional[ViewingDirection] = None
    rights: Optional[Rights] = None
    start: Optional[Any] = None
    navDate: Optional[NavDate] = None
    navPlace: Optional[NavPlace] = None
    provider: Optional[Provider] = None
    seeAlso: Optional[SeeAlso] = None
    thumbnail: Optional[List[Resource]] = None
    homepage: Optional[Homepage] = None
    behavior: Optional[Behavior] = None
    partOf: Optional[PartOf] = None
    items: Optional[List[Canvas]] = None
    structures: Optional[List[Range]] = None
    annotations: Optional[List[AnnotationPage]] = None


class BodyItem(Choice):
    items: List[Resource]


class Annotation(Class):
    type: Optional[constr(regex=r'^Annotation$')] = 'Annotation'
    service: Optional[Service] = None
    thumbnail: Optional[List[Resource]] = None
    motivation: Optional[Union[str, List[str]]] = None
    body: Optional[Union[Resource, BodyItem, List[Dict[str, Any]]]] = None
    target: Union[AnnoTarget, List[AnnoTarget]]


class Canvas(Class):
    type: Optional[constr(regex=r'^Canvas$')] = 'Canvas'
    height: Optional[Dimension] = None
    width: Optional[Dimension] = None
    duration: Optional[Duration] = None
    metadata: Optional[Metadata] = None
    summary: Optional[LngString] = None
    requiredStatement: Optional[KeyValueString] = None
    rights: Optional[Rights] = None
    navDate: Optional[NavDate] = None
    navPlace: Optional[NavPlace] = None
    provider: Optional[Provider] = None
    seeAlso: Optional[SeeAlso] = None
    service: Optional[Service] = None
    thumbnail: Optional[List[Resource]] = None
    homepage: Optional[Homepage] = None
    behavior: Optional[Behavior] = None
    partOf: Optional[PartOf] = None
    items: List[AnnotationPage]
    annotations: Optional[List[AnnotationPage]] = None


class ProviderItem(Class):
    type: Optional[constr(regex=r'^Agent$')] = 'Agent'
    homepage: Optional[Homepage] = None
    logo: Optional[List[Resource]] = None
    seeAlso: Optional[SeeAlso] = None


class Provider(Base):
    __root__: List[ProviderItem]


class Range(Class):
    type: Optional[constr(regex=r'^Range$')] = 'Range'
    supplementary: Optional[AnnotationCollection] = None
    service: Optional[Service] = None
    annotations: Optional[List[AnnotationPage]] = None
    thumbnail: Optional[List[Resource]] = None
    items: List[Union[SpecificResource, Item, Range, CanvasRef, RangeRef]]


class ResourceItem(Base):
    id: Id
    type: str
    height: Optional[Dimension] = None
    width: Optional[Dimension] = None
    duration: Optional[Duration] = None
    language: Optional[str] = None
    service: Optional[Service] = None
    format: Optional[Format] = None
    label: Optional[LngString] = None
    thumbnail: Optional[List[Resource]] = None
    annotations: Optional[List[AnnotationPage]] = None


class Resource(Base):
    __root__: Union[ResourceItem, ResourceItem1]


class ServiceItem(Class):
    profile: Optional[str] = None
    service: Optional[Service] = None


class ServiceItem1(Base):
    _id: Id = Field(..., alias='@id')
    _type: str = Field(..., alias='@type')
    profile: Optional[str] = None
    service: Optional[Service] = None


class Service(Base):
    __root__: List[Union[ServiceItem, ServiceItem1]]


class AnnotationCollection(Class):
    type: Optional[constr(regex=r'^AnnotationCollection$')] = 'AnnotationCollection'
    partOf: Optional[PartOf] = None
    next: Optional[AnnotationPage] = None
    first: Optional[AnnotationPage] = None
    last: Optional[AnnotationPage] = None
    service: Optional[Service] = None
    thumbnail: Optional[List[Resource]] = None
    items: Optional[List[Annotation]] = None


class Reference(Base):
    id: Id
    label: LngString
    type: constr(
        regex=r'^Manifest$|^AnnotationPage$|^Collection$|^AnnotationCollection$|^Canvas$|^Range$'
    )
    thumbnail: Optional[List[Resource]] = None


class CollectionRef(Reference):
    type: Optional[constr(regex=r'^Collection$')] = None


class ManifestRef(Reference):
    type: Optional[constr(regex=r'^Manifest$')] = None


class CanvasRef(Reference):
    type: Optional[constr(regex=r'^Canvas$')] = None


class RangeRef(Reference):
    type: Optional[constr(regex=r'^Range$')] = None


Model.update_forward_refs()
AnnotationPage.update_forward_refs()
Collection.update_forward_refs()
Manifest.update_forward_refs()
BodyItem.update_forward_refs()
Annotation.update_forward_refs()
Canvas.update_forward_refs()
ProviderItem.update_forward_refs()
Range.update_forward_refs()
ResourceItem.update_forward_refs()
ServiceItem.update_forward_refs()
ServiceItem1.update_forward_refs()
