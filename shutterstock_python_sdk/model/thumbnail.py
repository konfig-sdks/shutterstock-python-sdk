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


class Thumbnail(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Image thumbnail information
    """


    class MetaOapg:
        required = {
            "width",
            "url",
            "height",
        }
        
        class properties:
            height = schemas.IntSchema
            url = schemas.StrSchema
            width = schemas.IntSchema
            __annotations__ = {
                "height": height,
                "url": url,
                "width": width,
            }
    
    width: MetaOapg.properties.width
    url: MetaOapg.properties.url
    height: MetaOapg.properties.height
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["height", "url", "width", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["height", "url", "width", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Thumbnail':
        return super().__new__(
            cls,
            *args,
            width=width,
            url=url,
            height=height,
            _configuration=_configuration,
            **kwargs,
        )
