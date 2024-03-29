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


class LicenseFormat(BaseModel):
    # Description of the license
    description: typing.Optional[str] = Field(None, alias='description')

    # Format or extension of the media, such as mpeg for videos or jpeg for images
    format: typing.Optional[str] = Field(None, alias='format')

    # Media type of the license
    media_type: typing.Optional[Literal["image", "video", "audio", "editorial"]] = Field(None, alias='media_type')

    # Width of the media, in pixels, allowed by this license
    min_resolution: typing.Optional[int] = Field(None, alias='min_resolution')

    # Keyword that details the size of the media, such as hd or sd for video, huge or vector for images
    size: typing.Optional[str] = Field(None, alias='size')
    class Config:
        arbitrary_types_allowed = True
