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


class AccessTokenDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Access token details that are currently associated with this user
    """


    class MetaOapg:
        
        class properties:
            client_id = schemas.StrSchema
            contributor_id = schemas.StrSchema
            customer_id = schemas.StrSchema
            expires_in = schemas.IntSchema
            organization_id = schemas.StrSchema
            
            
            class realm(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "customer": "CUSTOMER",
                        "contributor": "CONTRIBUTOR",
                    }
                
                @schemas.classproperty
                def CUSTOMER(cls):
                    return cls("customer")
                
                @schemas.classproperty
                def CONTRIBUTOR(cls):
                    return cls("contributor")
        
            @staticmethod
            def scopes() -> typing.Type['AccessTokenDetailsScopes']:
                return AccessTokenDetailsScopes
            user_id = schemas.StrSchema
            username = schemas.StrSchema
            __annotations__ = {
                "client_id": client_id,
                "contributor_id": contributor_id,
                "customer_id": customer_id,
                "expires_in": expires_in,
                "organization_id": organization_id,
                "realm": realm,
                "scopes": scopes,
                "user_id": user_id,
                "username": username,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributor_id"]) -> MetaOapg.properties.contributor_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_id"]) -> MetaOapg.properties.customer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_id"]) -> MetaOapg.properties.organization_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realm"]) -> MetaOapg.properties.realm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> 'AccessTokenDetailsScopes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["client_id", "contributor_id", "customer_id", "expires_in", "organization_id", "realm", "scopes", "user_id", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributor_id"]) -> typing.Union[MetaOapg.properties.contributor_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_id"]) -> typing.Union[MetaOapg.properties.customer_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> typing.Union[MetaOapg.properties.expires_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_id"]) -> typing.Union[MetaOapg.properties.organization_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realm"]) -> typing.Union[MetaOapg.properties.realm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> typing.Union['AccessTokenDetailsScopes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["client_id", "contributor_id", "customer_id", "expires_in", "organization_id", "realm", "scopes", "user_id", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        contributor_id: typing.Union[MetaOapg.properties.contributor_id, str, schemas.Unset] = schemas.unset,
        customer_id: typing.Union[MetaOapg.properties.customer_id, str, schemas.Unset] = schemas.unset,
        expires_in: typing.Union[MetaOapg.properties.expires_in, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        organization_id: typing.Union[MetaOapg.properties.organization_id, str, schemas.Unset] = schemas.unset,
        realm: typing.Union[MetaOapg.properties.realm, str, schemas.Unset] = schemas.unset,
        scopes: typing.Union['AccessTokenDetailsScopes', schemas.Unset] = schemas.unset,
        user_id: typing.Union[MetaOapg.properties.user_id, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessTokenDetails':
        return super().__new__(
            cls,
            *args,
            client_id=client_id,
            contributor_id=contributor_id,
            customer_id=customer_id,
            expires_in=expires_in,
            organization_id=organization_id,
            realm=realm,
            scopes=scopes,
            user_id=user_id,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.access_token_details_scopes import AccessTokenDetailsScopes
