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

from shutterstock_python_sdk.pydantic.editorial_assets import EditorialAssets
from shutterstock_python_sdk.pydantic.editorial_category import EditorialCategory
from shutterstock_python_sdk.pydantic.editorial_updated_content_keywords import EditorialUpdatedContentKeywords
from shutterstock_python_sdk.pydantic.editorial_updated_content_rights import EditorialUpdatedContentRights
from shutterstock_python_sdk.pydantic.editorial_updated_content_updates import EditorialUpdatedContentUpdates

class EditorialUpdatedContent(BaseModel):
    id: str = Field(alias='id')

    title: typing.Optional[str] = Field(None, alias='title')

    description: typing.Optional[str] = Field(None, alias='description')

    aspect: typing.Optional[typing.Union[int, float]] = Field(None, alias='aspect')

    assets: typing.Optional[EditorialAssets] = Field(None, alias='assets')

    byline: typing.Optional[str] = Field(None, alias='byline')

    caption: typing.Optional[str] = Field(None, alias='caption')

    # List of categories
    categories: typing.Optional[typing.List[EditorialCategory]] = Field(None, alias='categories')

    commercial_status: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='commercial_status')

    created_time: typing.Optional[datetime] = Field(None, alias='created_time')

    date_taken: typing.Optional[date] = Field(None, alias='date_taken')

    keywords: typing.Optional[EditorialUpdatedContentKeywords] = Field(None, alias='keywords')

    rights: typing.Optional[EditorialUpdatedContentRights] = Field(None, alias='rights')

    special_instructions: typing.Optional[str] = Field(None, alias='special_instructions')

    supplier_code: typing.Optional[str] = Field(None, alias='supplier_code')

    updated_time: typing.Optional[datetime] = Field(None, alias='updated_time')

    updates: typing.Optional[EditorialUpdatedContentUpdates] = Field(None, alias='updates')
    class Config:
        arbitrary_types_allowed = True