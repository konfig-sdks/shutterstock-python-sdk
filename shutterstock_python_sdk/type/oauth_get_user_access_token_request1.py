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


class RequiredOauthGetUserAccessTokenRequest1(TypedDict):
    # Client ID (Consumer Key) of your application
    client_id: str

    # Grant type: authorization_code generates user tokens, client_credentials generates short-lived client grants
    grant_type: str

class OptionalOauthGetUserAccessTokenRequest1(TypedDict, total=False):
    # Client Secret (Consumer Secret) of your application
    client_secret: str

    # Response code from the /oauth/authorize flow; required if grant_type=authorization_code
    code: str

    # Whether or not the token expires, expiring tokens come with a refresh_token to renew the access_token
    expires: str

    # User type to be authorized (usually 'customer')
    realm: str

    # Pass this along with grant_type=refresh_token to get a fresh access token
    refresh_token: str

class OauthGetUserAccessTokenRequest1(RequiredOauthGetUserAccessTokenRequest1, OptionalOauthGetUserAccessTokenRequest1):
    pass
