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


class EditorialAssets(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Asset information, including size and thumbnail URLs
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def medium_jpg() -> typing.Type['ImageSizeDetails']:
                return ImageSizeDetails
        
            @staticmethod
            def original() -> typing.Type['ImageSizeDetails']:
                return ImageSizeDetails
        
            @staticmethod
            def small_jpg() -> typing.Type['ImageSizeDetails']:
                return ImageSizeDetails
        
            @staticmethod
            def thumb_170() -> typing.Type['Thumbnail']:
                return Thumbnail
        
            @staticmethod
            def thumb_220() -> typing.Type['Thumbnail']:
                return Thumbnail
        
            @staticmethod
            def watermark_1500() -> typing.Type['Thumbnail']:
                return Thumbnail
        
            @staticmethod
            def watermark_450() -> typing.Type['Thumbnail']:
                return Thumbnail
            __annotations__ = {
                "medium_jpg": medium_jpg,
                "original": original,
                "small_jpg": small_jpg,
                "thumb_170": thumb_170,
                "thumb_220": thumb_220,
                "watermark_1500": watermark_1500,
                "watermark_450": watermark_450,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["medium_jpg"]) -> 'ImageSizeDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original"]) -> 'ImageSizeDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["small_jpg"]) -> 'ImageSizeDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumb_170"]) -> 'Thumbnail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumb_220"]) -> 'Thumbnail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["watermark_1500"]) -> 'Thumbnail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["watermark_450"]) -> 'Thumbnail': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["medium_jpg", "original", "small_jpg", "thumb_170", "thumb_220", "watermark_1500", "watermark_450", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["medium_jpg"]) -> typing.Union['ImageSizeDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original"]) -> typing.Union['ImageSizeDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["small_jpg"]) -> typing.Union['ImageSizeDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumb_170"]) -> typing.Union['Thumbnail', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumb_220"]) -> typing.Union['Thumbnail', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["watermark_1500"]) -> typing.Union['Thumbnail', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["watermark_450"]) -> typing.Union['Thumbnail', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["medium_jpg", "original", "small_jpg", "thumb_170", "thumb_220", "watermark_1500", "watermark_450", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        medium_jpg: typing.Union['ImageSizeDetails', schemas.Unset] = schemas.unset,
        original: typing.Union['ImageSizeDetails', schemas.Unset] = schemas.unset,
        small_jpg: typing.Union['ImageSizeDetails', schemas.Unset] = schemas.unset,
        thumb_170: typing.Union['Thumbnail', schemas.Unset] = schemas.unset,
        thumb_220: typing.Union['Thumbnail', schemas.Unset] = schemas.unset,
        watermark_1500: typing.Union['Thumbnail', schemas.Unset] = schemas.unset,
        watermark_450: typing.Union['Thumbnail', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditorialAssets':
        return super().__new__(
            cls,
            *args,
            medium_jpg=medium_jpg,
            original=original,
            small_jpg=small_jpg,
            thumb_170=thumb_170,
            thumb_220=thumb_220,
            watermark_1500=watermark_1500,
            watermark_450=watermark_450,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.image_size_details import ImageSizeDetails
from shutterstock_python_sdk.model.thumbnail import Thumbnail
