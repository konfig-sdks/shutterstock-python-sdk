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

from shutterstock_python_sdk.type.create_catalog_collection_item import CreateCatalogCollectionItem

class RequiredCreateCatalogCollection(TypedDict):
    name: str

class OptionalCreateCatalogCollection(TypedDict, total=False):
    items: typing.List[CreateCatalogCollectionItem]

    visibility: str

class CreateCatalogCollection(RequiredCreateCatalogCollection, OptionalCreateCatalogCollection):
    pass
