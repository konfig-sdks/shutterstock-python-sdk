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


class Preview(BaseModel):
    # Content type of the preview, currently audio/mp3
    content_type: typing.Optional[Literal["audio/mp3"]] = Field(None, alias='content_type')

    # Url of the instrument's preview file
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
