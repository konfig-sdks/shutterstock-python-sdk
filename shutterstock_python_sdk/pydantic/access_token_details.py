# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from shutterstock_python_sdk.pydantic.access_token_details_scopes import AccessTokenDetailsScopes

class AccessTokenDetails(BaseModel):
    # Client ID that is associated with the user
    client_id: typing.Optional[str] = Field(None, alias='client_id')

    # Contributor ID that is associated with the user
    contributor_id: typing.Optional[str] = Field(None, alias='contributor_id')

    # Customer ID that is associated with the user
    customer_id: typing.Optional[str] = Field(None, alias='customer_id')

    # Number of seconds until the access token expires; no expiration if this value is null
    expires_in: typing.Optional[int] = Field(None, alias='expires_in')

    # Organization ID that is associated with the user
    organization_id: typing.Optional[str] = Field(None, alias='organization_id')

    # Type of access token
    realm: typing.Optional[Literal["customer", "contributor"]] = Field(None, alias='realm')

    scopes: typing.Optional[AccessTokenDetailsScopes] = Field(None, alias='scopes')

    # User ID that is associated with the user
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    # User name that is associated with the user
    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
