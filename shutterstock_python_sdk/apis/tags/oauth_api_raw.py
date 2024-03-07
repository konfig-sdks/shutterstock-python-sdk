# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_oauth_authorize.get import AuthorizeApplicationsRaw
from shutterstock_python_sdk.paths.v2_oauth_access_token.post import GetUserAccessTokenRaw


class OauthApiRaw(
    AuthorizeApplicationsRaw,
    GetUserAccessTokenRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
