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

from shutterstock_python_sdk.pydantic.instrument_tags import InstrumentTags
from shutterstock_python_sdk.pydantic.preview import Preview

class Instrument(BaseModel):
    tags: typing.Optional[InstrumentTags] = Field(None, alias='tags')

    # The id of the instrument
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of the instrument
    name: typing.Optional[str] = Field(None, alias='name')

    # Preview of the instrument
    previews: typing.Optional[typing.List[Preview]] = Field(None, alias='previews')
    class Config:
        arbitrary_types_allowed = True