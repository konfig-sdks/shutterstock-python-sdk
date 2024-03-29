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


class LicenseImage(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Data required to license an image
    """


    class MetaOapg:
        required = {
            "image_id",
        }
        
        class properties:
            image_id = schemas.StrSchema
        
            @staticmethod
            def auth_cookie() -> typing.Type['Cookie']:
                return Cookie
        
            @staticmethod
            def custom_dimensions() -> typing.Type['CustomSizeDimensions']:
                return CustomSizeDimensions
            editorial_acknowledgement = schemas.BoolSchema
            
            
            class format(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "jpg": "JPG",
                    }
                
                @schemas.classproperty
                def JPG(cls):
                    return cls("jpg")
        
            @staticmethod
            def metadata() -> typing.Type['LicenseRequestMetadata']:
                return LicenseRequestMetadata
            price = schemas.NumberSchema
            search_id = schemas.StrSchema
            show_modal = schemas.BoolSchema
            
            
            class size(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "small": "SMALL",
                        "medium": "MEDIUM",
                        "huge": "HUGE",
                        "custom": "CUSTOM",
                    }
                
                @schemas.classproperty
                def SMALL(cls):
                    return cls("small")
                
                @schemas.classproperty
                def MEDIUM(cls):
                    return cls("medium")
                
                @schemas.classproperty
                def HUGE(cls):
                    return cls("huge")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
            subscription_id = schemas.StrSchema
            verification_code = schemas.StrSchema
            __annotations__ = {
                "image_id": image_id,
                "auth_cookie": auth_cookie,
                "custom_dimensions": custom_dimensions,
                "editorial_acknowledgement": editorial_acknowledgement,
                "format": format,
                "metadata": metadata,
                "price": price,
                "search_id": search_id,
                "show_modal": show_modal,
                "size": size,
                "subscription_id": subscription_id,
                "verification_code": verification_code,
            }
    
    image_id: MetaOapg.properties.image_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_id"]) -> MetaOapg.properties.image_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth_cookie"]) -> 'Cookie': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_dimensions"]) -> 'CustomSizeDimensions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editorial_acknowledgement"]) -> MetaOapg.properties.editorial_acknowledgement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'LicenseRequestMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["search_id"]) -> MetaOapg.properties.search_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_modal"]) -> MetaOapg.properties.show_modal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription_id"]) -> MetaOapg.properties.subscription_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification_code"]) -> MetaOapg.properties.verification_code: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["image_id", "auth_cookie", "custom_dimensions", "editorial_acknowledgement", "format", "metadata", "price", "search_id", "show_modal", "size", "subscription_id", "verification_code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_id"]) -> MetaOapg.properties.image_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth_cookie"]) -> typing.Union['Cookie', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_dimensions"]) -> typing.Union['CustomSizeDimensions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editorial_acknowledgement"]) -> typing.Union[MetaOapg.properties.editorial_acknowledgement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> typing.Union[MetaOapg.properties.format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['LicenseRequestMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["search_id"]) -> typing.Union[MetaOapg.properties.search_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_modal"]) -> typing.Union[MetaOapg.properties.show_modal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription_id"]) -> typing.Union[MetaOapg.properties.subscription_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification_code"]) -> typing.Union[MetaOapg.properties.verification_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["image_id", "auth_cookie", "custom_dimensions", "editorial_acknowledgement", "format", "metadata", "price", "search_id", "show_modal", "size", "subscription_id", "verification_code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        image_id: typing.Union[MetaOapg.properties.image_id, str, ],
        auth_cookie: typing.Union['Cookie', schemas.Unset] = schemas.unset,
        custom_dimensions: typing.Union['CustomSizeDimensions', schemas.Unset] = schemas.unset,
        editorial_acknowledgement: typing.Union[MetaOapg.properties.editorial_acknowledgement, bool, schemas.Unset] = schemas.unset,
        format: typing.Union[MetaOapg.properties.format, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['LicenseRequestMetadata', schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        search_id: typing.Union[MetaOapg.properties.search_id, str, schemas.Unset] = schemas.unset,
        show_modal: typing.Union[MetaOapg.properties.show_modal, bool, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, str, schemas.Unset] = schemas.unset,
        subscription_id: typing.Union[MetaOapg.properties.subscription_id, str, schemas.Unset] = schemas.unset,
        verification_code: typing.Union[MetaOapg.properties.verification_code, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LicenseImage':
        return super().__new__(
            cls,
            *args,
            image_id=image_id,
            auth_cookie=auth_cookie,
            custom_dimensions=custom_dimensions,
            editorial_acknowledgement=editorial_acknowledgement,
            format=format,
            metadata=metadata,
            price=price,
            search_id=search_id,
            show_modal=show_modal,
            size=size,
            subscription_id=subscription_id,
            verification_code=verification_code,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.cookie import Cookie
from shutterstock_python_sdk.model.custom_size_dimensions import CustomSizeDimensions
from shutterstock_python_sdk.model.license_request_metadata import LicenseRequestMetadata
