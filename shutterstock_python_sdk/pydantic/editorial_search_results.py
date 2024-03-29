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

from shutterstock_python_sdk.pydantic.editorial_content import EditorialContent

class EditorialSearchResults(BaseModel):
    # Editorial items
    data: typing.List[EditorialContent] = Field(alias='data')

    # Total count of all results
    total_count: int = Field(alias='total_count')

    # Optional error message
    message: typing.Optional[str] = Field(None, alias='message')

    # Cursor value that represents the next page of results
    next: typing.Optional[str] = Field(None, alias='next')

    # Current page of the response
    page: typing.Optional[int] = Field(None, alias='page')

    # Number of results per page
    per_page: typing.Optional[int] = Field(None, alias='per_page')

    # Cursor value that represents the previous page of results
    prev: typing.Optional[str] = Field(None, alias='prev')

    # Unique identifier for the search request
    search_id: typing.Optional[str] = Field(None, alias='search_id')
    class Config:
        arbitrary_types_allowed = True
