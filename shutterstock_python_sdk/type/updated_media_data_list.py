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
from shutterstock_python_sdk.type.updated_media import UpdatedMedia

class RequiredUpdatedMediaDataList(TypedDict):
    pass

class OptionalUpdatedMediaDataList(TypedDict, total=False):
    # Updated media items
    data: typing.List[UpdatedMedia]

    # Error list; appears only if there was an error
    errors: typing.List[Error]

    # Server-generated message, if any
    message: str

    # Current page that is returned
    page: int

    # Number of results per page
    per_page: int

    # Total count of all results across all pages
    total_count: int

class UpdatedMediaDataList(RequiredUpdatedMediaDataList, OptionalUpdatedMediaDataList):
    pass
