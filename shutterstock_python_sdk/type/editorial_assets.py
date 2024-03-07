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

from shutterstock_python_sdk.type.image_size_details import ImageSizeDetails
from shutterstock_python_sdk.type.thumbnail import Thumbnail

class RequiredEditorialAssets(TypedDict):
    pass

class OptionalEditorialAssets(TypedDict, total=False):
    medium_jpg: ImageSizeDetails

    original: ImageSizeDetails

    small_jpg: ImageSizeDetails

    thumb_170: Thumbnail

    thumb_220: Thumbnail

    watermark_1500: Thumbnail

    watermark_450: Thumbnail

class EditorialAssets(RequiredEditorialAssets, OptionalEditorialAssets):
    pass
