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

from shutterstock_python_sdk.pydantic.editorial_cover_item import EditorialCoverItem

class EditorialLivefeed(BaseModel):
    # Livefeed ID
    id: str = Field(alias='id')

    # Name of the livefeed
    name: str = Field(alias='name')

    # Total count of items in the livefeed
    total_item_count: int = Field(alias='total_item_count')

    cover_item: typing.Optional[EditorialCoverItem] = Field(None, alias='cover_item')

    # When the livefeed was initially created
    created_time: typing.Optional[datetime] = Field(None, alias='created_time')
    class Config:
        arbitrary_types_allowed = True
