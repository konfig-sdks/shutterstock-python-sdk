# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from shutterstock_python_sdk import schemas  # noqa: F401


class ContributorProfile(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contributor profile data
    """


    class MetaOapg:
        required = {
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            about = schemas.StrSchema
        
            @staticmethod
            def contributor_type() -> typing.Type['ContributorProfileContributorType']:
                return ContributorProfileContributorType
            display_name = schemas.StrSchema
        
            @staticmethod
            def equipment() -> typing.Type['ContributorProfileEquipment']:
                return ContributorProfileEquipment
            location = schemas.StrSchema
            portfolio_url = schemas.StrSchema
        
            @staticmethod
            def social_media() -> typing.Type['ContributorProfileSocialMedia']:
                return ContributorProfileSocialMedia
        
            @staticmethod
            def styles() -> typing.Type['ContributorProfileStyles']:
                return ContributorProfileStyles
        
            @staticmethod
            def subjects() -> typing.Type['ContributorProfileSubjects']:
                return ContributorProfileSubjects
            website = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "about": about,
                "contributor_type": contributor_type,
                "display_name": display_name,
                "equipment": equipment,
                "location": location,
                "portfolio_url": portfolio_url,
                "social_media": social_media,
                "styles": styles,
                "subjects": subjects,
                "website": website,
            }
    
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["about"]) -> MetaOapg.properties.about: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributor_type"]) -> 'ContributorProfileContributorType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["equipment"]) -> 'ContributorProfileEquipment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["portfolio_url"]) -> MetaOapg.properties.portfolio_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["social_media"]) -> 'ContributorProfileSocialMedia': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["styles"]) -> 'ContributorProfileStyles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subjects"]) -> 'ContributorProfileSubjects': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "about", "contributor_type", "display_name", "equipment", "location", "portfolio_url", "social_media", "styles", "subjects", "website", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["about"]) -> typing.Union[MetaOapg.properties.about, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributor_type"]) -> typing.Union['ContributorProfileContributorType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["equipment"]) -> typing.Union['ContributorProfileEquipment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["portfolio_url"]) -> typing.Union[MetaOapg.properties.portfolio_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["social_media"]) -> typing.Union['ContributorProfileSocialMedia', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["styles"]) -> typing.Union['ContributorProfileStyles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subjects"]) -> typing.Union['ContributorProfileSubjects', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "about", "contributor_type", "display_name", "equipment", "location", "portfolio_url", "social_media", "styles", "subjects", "website", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        about: typing.Union[MetaOapg.properties.about, str, schemas.Unset] = schemas.unset,
        contributor_type: typing.Union['ContributorProfileContributorType', schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        equipment: typing.Union['ContributorProfileEquipment', schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, str, schemas.Unset] = schemas.unset,
        portfolio_url: typing.Union[MetaOapg.properties.portfolio_url, str, schemas.Unset] = schemas.unset,
        social_media: typing.Union['ContributorProfileSocialMedia', schemas.Unset] = schemas.unset,
        styles: typing.Union['ContributorProfileStyles', schemas.Unset] = schemas.unset,
        subjects: typing.Union['ContributorProfileSubjects', schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContributorProfile':
        return super().__new__(
            cls,
            *args,
            id=id,
            about=about,
            contributor_type=contributor_type,
            display_name=display_name,
            equipment=equipment,
            location=location,
            portfolio_url=portfolio_url,
            social_media=social_media,
            styles=styles,
            subjects=subjects,
            website=website,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.contributor_profile_contributor_type import ContributorProfileContributorType
from shutterstock_python_sdk.model.contributor_profile_equipment import ContributorProfileEquipment
from shutterstock_python_sdk.model.contributor_profile_social_media import ContributorProfileSocialMedia
from shutterstock_python_sdk.model.contributor_profile_styles import ContributorProfileStyles
from shutterstock_python_sdk.model.contributor_profile_subjects import ContributorProfileSubjects