# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_user_access_token.get import GetAccessTokenDetails
from shutterstock_python_sdk.paths.v2_user.get import GetUserDetails
from shutterstock_python_sdk.paths.v2_user_subscriptions.get import ListSubscriptions
from shutterstock_python_sdk.apis.tags.users_api_raw import UsersApiRaw


class UsersApi(
    GetAccessTokenDetails,
    GetUserDetails,
    ListSubscriptions,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersApiRaw(api_client)