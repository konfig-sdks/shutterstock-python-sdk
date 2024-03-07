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

from shutterstock_python_sdk.type.editorial_content import EditorialContent
from shutterstock_python_sdk.type.error import Error

class RequiredEditorialImageContentDataList(TypedDict):
    pass

class OptionalEditorialImageContentDataList(TypedDict, total=False):
    # Editorial items
    data: typing.List[EditorialContent]

    # Error list; appears only if there was an error
    errors: typing.List[Error]

    # Optional error message
    message: str

    # Current page of the response
    page: int

    # Number of results per page
    per_page: int

    # Total count of all results
    total_count: int

class EditorialImageContentDataList(RequiredEditorialImageContentDataList, OptionalEditorialImageContentDataList):
    pass
