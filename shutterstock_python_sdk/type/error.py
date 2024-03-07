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

from shutterstock_python_sdk.type.error_items import ErrorItems

class RequiredError(TypedDict):
    # Specific details about this error
    message: str

class OptionalError(TypedDict, total=False):
    # The error code of this error
    code: str

    # Debugging information about the error
    data: str

    items: ErrorItems

    # Internal code reference to the source of the error
    path: str

class Error(RequiredError, OptionalError):
    pass
