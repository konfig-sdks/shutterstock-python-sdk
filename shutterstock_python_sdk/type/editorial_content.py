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

from shutterstock_python_sdk.type.editorial_assets import EditorialAssets
from shutterstock_python_sdk.type.editorial_category import EditorialCategory
from shutterstock_python_sdk.type.editorial_content_keywords import EditorialContentKeywords

class RequiredEditorialContent(TypedDict):
    id: str

class OptionalEditorialContent(TypedDict, total=False):
    title: str

    description: str

    aspect: typing.Union[int, float]

    assets: EditorialAssets

    byline: str

    caption: str

    # List of categories
    categories: typing.List[EditorialCategory]

    date_taken: date

    keywords: EditorialContentKeywords

    special_instructions: str

class EditorialContent(RequiredEditorialContent, OptionalEditorialContent):
    pass