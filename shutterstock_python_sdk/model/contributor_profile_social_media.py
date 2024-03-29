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


class ContributorProfileSocialMedia(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contributor profile social media links
    """


    class MetaOapg:
        
        class properties:
            facebook = schemas.StrSchema
            google_plus = schemas.StrSchema
            linkedin = schemas.StrSchema
            pinterest = schemas.StrSchema
            tumblr = schemas.StrSchema
            twitter = schemas.StrSchema
            __annotations__ = {
                "facebook": facebook,
                "google_plus": google_plus,
                "linkedin": linkedin,
                "pinterest": pinterest,
                "tumblr": tumblr,
                "twitter": twitter,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["facebook"]) -> MetaOapg.properties.facebook: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["google_plus"]) -> MetaOapg.properties.google_plus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkedin"]) -> MetaOapg.properties.linkedin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pinterest"]) -> MetaOapg.properties.pinterest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tumblr"]) -> MetaOapg.properties.tumblr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twitter"]) -> MetaOapg.properties.twitter: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["facebook", "google_plus", "linkedin", "pinterest", "tumblr", "twitter", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["facebook"]) -> typing.Union[MetaOapg.properties.facebook, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["google_plus"]) -> typing.Union[MetaOapg.properties.google_plus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkedin"]) -> typing.Union[MetaOapg.properties.linkedin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pinterest"]) -> typing.Union[MetaOapg.properties.pinterest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tumblr"]) -> typing.Union[MetaOapg.properties.tumblr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twitter"]) -> typing.Union[MetaOapg.properties.twitter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["facebook", "google_plus", "linkedin", "pinterest", "tumblr", "twitter", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        facebook: typing.Union[MetaOapg.properties.facebook, str, schemas.Unset] = schemas.unset,
        google_plus: typing.Union[MetaOapg.properties.google_plus, str, schemas.Unset] = schemas.unset,
        linkedin: typing.Union[MetaOapg.properties.linkedin, str, schemas.Unset] = schemas.unset,
        pinterest: typing.Union[MetaOapg.properties.pinterest, str, schemas.Unset] = schemas.unset,
        tumblr: typing.Union[MetaOapg.properties.tumblr, str, schemas.Unset] = schemas.unset,
        twitter: typing.Union[MetaOapg.properties.twitter, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContributorProfileSocialMedia':
        return super().__new__(
            cls,
            *args,
            facebook=facebook,
            google_plus=google_plus,
            linkedin=linkedin,
            pinterest=pinterest,
            tumblr=tumblr,
            twitter=twitter,
            _configuration=_configuration,
            **kwargs,
        )
