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

from shutterstock_python_sdk.pydantic.featured_collection_cover_item import FeaturedCollectionCoverItem

class FeaturedCollection(BaseModel):
    # Collection ID
    id: str = Field(alias='id')

    # Name of the collection
    name: str = Field(alias='name')

    # Total number of items in the collection
    total_item_count: int = Field(alias='total_item_count')

    cover_item: typing.Optional[FeaturedCollectionCoverItem] = Field(None, alias='cover_item')

    # Date that the collection was created
    created_time: typing.Optional[datetime] = Field(None, alias='created_time')

    hero_item: typing.Optional[FeaturedCollectionCoverItem] = Field(None, alias='hero_item')

    # Date that an item in the collection was last added or removed
    items_updated_time: typing.Optional[datetime] = Field(None, alias='items_updated_time')

    # Unique share url for the collection
    share_url: typing.Optional[str] = Field(None, alias='share_url')

    # Date that the collection was last modified
    updated_time: typing.Optional[datetime] = Field(None, alias='updated_time')
    class Config:
        arbitrary_types_allowed = True
