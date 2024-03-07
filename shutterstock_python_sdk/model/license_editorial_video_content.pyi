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


class LicenseEditorialVideoContent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Individual editorial video content to license
    """


    class MetaOapg:
        required = {
            "license",
            "editorial_id",
        }
        
        class properties:
            editorial_id = schemas.StrSchema
            
            
            class license(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DIGITAL_ONLY(cls):
                    return cls("premier_editorial_video_digital_only")
                
                @schemas.classproperty
                def ALL_MEDIA(cls):
                    return cls("premier_editorial_video_all_media")
                
                @schemas.classproperty
                def ALL_MEDIA_SINGLE_TERRITORY(cls):
                    return cls("premier_editorial_video_all_media_single_territory")
                
                @schemas.classproperty
                def COMP(cls):
                    return cls("premier_editorial_video_comp")
        
            @staticmethod
            def metadata() -> typing.Type['LicenseRequestMetadata']:
                return LicenseRequestMetadata
            
            
            class size(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ORIGINAL(cls):
                    return cls("original")
            __annotations__ = {
                "editorial_id": editorial_id,
                "license": license,
                "metadata": metadata,
                "size": size,
            }
    
    license: MetaOapg.properties.license
    editorial_id: MetaOapg.properties.editorial_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editorial_id"]) -> MetaOapg.properties.editorial_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license"]) -> MetaOapg.properties.license: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'LicenseRequestMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["editorial_id", "license", "metadata", "size", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editorial_id"]) -> MetaOapg.properties.editorial_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license"]) -> MetaOapg.properties.license: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['LicenseRequestMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["editorial_id", "license", "metadata", "size", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        license: typing.Union[MetaOapg.properties.license, str, ],
        editorial_id: typing.Union[MetaOapg.properties.editorial_id, str, ],
        metadata: typing.Union['LicenseRequestMetadata', schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LicenseEditorialVideoContent':
        return super().__new__(
            cls,
            *args,
            license=license,
            editorial_id=editorial_id,
            metadata=metadata,
            size=size,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.license_request_metadata import LicenseRequestMetadata
