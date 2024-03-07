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

from shutterstock_python_sdk.pydantic.error import Error
from shutterstock_python_sdk.pydantic.updated_media import UpdatedMedia

class UpdatedMediaDataList(BaseModel):
    # Updated media items
    data: typing.Optional[typing.List[UpdatedMedia]] = Field(None, alias='data')

    # Error list; appears only if there was an error
    errors: typing.Optional[typing.List[Error]] = Field(None, alias='errors')

    # Server-generated message, if any
    message: typing.Optional[str] = Field(None, alias='message')

    # Current page that is returned
    page: typing.Optional[int] = Field(None, alias='page')

    # Number of results per page
    per_page: typing.Optional[int] = Field(None, alias='per_page')

    # Total count of all results across all pages
    total_count: typing.Optional[int] = Field(None, alias='total_count')
    class Config:
        arbitrary_types_allowed = True