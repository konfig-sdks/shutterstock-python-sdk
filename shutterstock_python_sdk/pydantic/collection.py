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

from shutterstock_python_sdk.pydantic.collection_item import CollectionItem

class Collection(BaseModel):
    # The collection ID
    id: str = Field(alias='id')

    # The name of the collection
    name: str = Field(alias='name')

    # The number of items in the collection
    total_item_count: int = Field(alias='total_item_count')

    cover_item: typing.Optional[CollectionItem] = Field(None, alias='cover_item')

    # When the collection was created
    created_time: typing.Optional[datetime] = Field(None, alias='created_time')

    # The last time this collection's items were updated
    items_updated_time: typing.Optional[datetime] = Field(None, alias='items_updated_time')

    # A code that can be used to share the collection (optional)
    share_code: typing.Optional[str] = Field(None, alias='share_code')

    # The browser URL that can be used to share the collection (optional)
    share_url: typing.Optional[str] = Field(None, alias='share_url')

    # The last time the collection was update (other than changes to the items in it)
    updated_time: typing.Optional[datetime] = Field(None, alias='updated_time')
    class Config:
        arbitrary_types_allowed = True