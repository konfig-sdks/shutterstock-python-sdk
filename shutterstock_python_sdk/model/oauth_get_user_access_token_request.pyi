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


class OauthGetUserAccessTokenRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "grant_type",
            "client_id",
        }
        
        class properties:
            client_id = schemas.StrSchema
            
            
            class grant_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AUTHORIZATION_CODE(cls):
                    return cls("authorization_code")
                
                @schemas.classproperty
                def CLIENT_CREDENTIALS(cls):
                    return cls("client_credentials")
                
                @schemas.classproperty
                def REFRESH_TOKEN(cls):
                    return cls("refresh_token")
            client_secret = schemas.StrSchema
            code = schemas.StrSchema
            expires = schemas.BoolSchema
            
            
            class realm(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CUSTOMER(cls):
                    return cls("customer")
                
                @schemas.classproperty
                def CONTRIBUTOR(cls):
                    return cls("contributor")
            refresh_token = schemas.StrSchema
            __annotations__ = {
                "client_id": client_id,
                "grant_type": grant_type,
                "client_secret": client_secret,
                "code": code,
                "expires": expires,
                "realm": realm,
                "refresh_token": refresh_token,
            }
    
    grant_type: MetaOapg.properties.grant_type
    client_id: MetaOapg.properties.client_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires"]) -> MetaOapg.properties.expires: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realm"]) -> MetaOapg.properties.realm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh_token"]) -> MetaOapg.properties.refresh_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["client_id", "grant_type", "client_secret", "code", "expires", "realm", "refresh_token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_secret"]) -> typing.Union[MetaOapg.properties.client_secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires"]) -> typing.Union[MetaOapg.properties.expires, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realm"]) -> typing.Union[MetaOapg.properties.realm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh_token"]) -> typing.Union[MetaOapg.properties.refresh_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["client_id", "grant_type", "client_secret", "code", "expires", "realm", "refresh_token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        grant_type: typing.Union[MetaOapg.properties.grant_type, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, ],
        client_secret: typing.Union[MetaOapg.properties.client_secret, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        expires: typing.Union[MetaOapg.properties.expires, bool, schemas.Unset] = schemas.unset,
        realm: typing.Union[MetaOapg.properties.realm, str, schemas.Unset] = schemas.unset,
        refresh_token: typing.Union[MetaOapg.properties.refresh_token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OauthGetUserAccessTokenRequest':
        return super().__new__(
            cls,
            *args,
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            expires=expires,
            realm=realm,
            refresh_token=refresh_token,
            _configuration=_configuration,
            **kwargs,
        )
