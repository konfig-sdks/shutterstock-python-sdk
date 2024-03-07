# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_oauth_authorize.get import AuthorizeApplications
from shutterstock_python_sdk.paths.v2_oauth_access_token.post import GetUserAccessToken
from shutterstock_python_sdk.apis.tags.oauth_api_raw import OauthApiRaw


class OauthApi(
    AuthorizeApplications,
    GetUserAccessToken,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: OauthApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = OauthApiRaw(api_client)
