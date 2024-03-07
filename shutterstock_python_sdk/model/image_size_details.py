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


class ImageSizeDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Image size information
    """


    class MetaOapg:
        
        class properties:
            display_name = schemas.StrSchema
            dpi = schemas.IntSchema
            file_size = schemas.IntSchema
            format = schemas.StrSchema
            height = schemas.IntSchema
            is_licensable = schemas.BoolSchema
            width = schemas.IntSchema
            __annotations__ = {
                "display_name": display_name,
                "dpi": dpi,
                "file_size": file_size,
                "format": format,
                "height": height,
                "is_licensable": is_licensable,
                "width": width,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpi"]) -> MetaOapg.properties.dpi: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_licensable"]) -> MetaOapg.properties.is_licensable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["display_name", "dpi", "file_size", "format", "height", "is_licensable", "width", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpi"]) -> typing.Union[MetaOapg.properties.dpi, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_size"]) -> typing.Union[MetaOapg.properties.file_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> typing.Union[MetaOapg.properties.format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_licensable"]) -> typing.Union[MetaOapg.properties.is_licensable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["display_name", "dpi", "file_size", "format", "height", "is_licensable", "width", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        dpi: typing.Union[MetaOapg.properties.dpi, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        file_size: typing.Union[MetaOapg.properties.file_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        format: typing.Union[MetaOapg.properties.format, str, schemas.Unset] = schemas.unset,
        height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_licensable: typing.Union[MetaOapg.properties.is_licensable, bool, schemas.Unset] = schemas.unset,
        width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImageSizeDetails':
        return super().__new__(
            cls,
            *args,
            display_name=display_name,
            dpi=dpi,
            file_size=file_size,
            format=format,
            height=height,
            is_licensable=is_licensable,
            width=width,
            _configuration=_configuration,
            **kwargs,
        )
