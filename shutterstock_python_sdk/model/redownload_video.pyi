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


class RedownloadVideo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Data required to redownload a video
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def auth_cookie() -> typing.Type['Cookie']:
                return Cookie
            show_modal = schemas.BoolSchema
            
            
            class size(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WEB(cls):
                    return cls("web")
                
                @schemas.classproperty
                def SD(cls):
                    return cls("sd")
                
                @schemas.classproperty
                def HD(cls):
                    return cls("hd")
                
                @schemas.classproperty
                def _4K(cls):
                    return cls("4k")
            verification_code = schemas.StrSchema
            __annotations__ = {
                "auth_cookie": auth_cookie,
                "show_modal": show_modal,
                "size": size,
                "verification_code": verification_code,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth_cookie"]) -> 'Cookie': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_modal"]) -> MetaOapg.properties.show_modal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification_code"]) -> MetaOapg.properties.verification_code: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["auth_cookie", "show_modal", "size", "verification_code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth_cookie"]) -> typing.Union['Cookie', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_modal"]) -> typing.Union[MetaOapg.properties.show_modal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification_code"]) -> typing.Union[MetaOapg.properties.verification_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["auth_cookie", "show_modal", "size", "verification_code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        auth_cookie: typing.Union['Cookie', schemas.Unset] = schemas.unset,
        show_modal: typing.Union[MetaOapg.properties.show_modal, bool, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, str, schemas.Unset] = schemas.unset,
        verification_code: typing.Union[MetaOapg.properties.verification_code, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RedownloadVideo':
        return super().__new__(
            cls,
            *args,
            auth_cookie=auth_cookie,
            show_modal=show_modal,
            size=size,
            verification_code=verification_code,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.cookie import Cookie
