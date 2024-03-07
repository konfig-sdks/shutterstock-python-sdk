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

from shutterstock_python_sdk.pydantic.error_items import ErrorItems

class Error(BaseModel):
    # Specific details about this error
    message: str = Field(alias='message')

    # The error code of this error
    code: typing.Optional[str] = Field(None, alias='code')

    # Debugging information about the error
    data: typing.Optional[str] = Field(None, alias='data')

    items: typing.Optional[ErrorItems] = Field(None, alias='items')

    # Internal code reference to the source of the error
    path: typing.Optional[str] = Field(None, alias='path')
    class Config:
        arbitrary_types_allowed = True
