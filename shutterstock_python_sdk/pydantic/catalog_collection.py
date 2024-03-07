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

from shutterstock_python_sdk.pydantic.catalog_collection_item import CatalogCollectionItem
from shutterstock_python_sdk.pydantic.catalog_collection_role_assignments import CatalogCollectionRoleAssignments

class CatalogCollection(BaseModel):
    created_time: datetime = Field(alias='created_time')

    id: str = Field(alias='id')

    name: str = Field(alias='name')

    role_assignments: CatalogCollectionRoleAssignments = Field(alias='role_assignments')

    total_item_count: typing.Union[int, float] = Field(alias='total_item_count')

    updated_time: datetime = Field(alias='updated_time')

    visibility: Literal["private", "public"] = Field(alias='visibility')

    cover_asset: typing.Optional[CatalogCollectionItem] = Field(None, alias='cover_asset')
    class Config:
        arbitrary_types_allowed = True