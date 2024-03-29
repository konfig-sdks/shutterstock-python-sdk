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

from shutterstock_python_sdk.type.error import Error
from shutterstock_python_sdk.type.subscription import Subscription

class RequiredSubscriptionDataList(TypedDict):
    pass

class OptionalSubscriptionDataList(TypedDict, total=False):
    # Subscriptions retrieved from this user
    data: typing.List[Subscription]

    # Error list; appears only if there was an error
    errors: typing.List[Error]

    # Optional error message
    message: str

    # Current page that is being queried
    page: int

    # Amount of subscriptions to show per page
    per_page: int

    # Total number of subscriptions for this user
    total_count: int

class SubscriptionDataList(RequiredSubscriptionDataList, OptionalSubscriptionDataList):
    pass
