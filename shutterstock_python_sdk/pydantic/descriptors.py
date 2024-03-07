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

from shutterstock_python_sdk.pydantic.bands import Bands
from shutterstock_python_sdk.pydantic.descriptors_tags import DescriptorsTags
from shutterstock_python_sdk.pydantic.instruments import Instruments
from shutterstock_python_sdk.pydantic.preview import Preview

class Descriptors(BaseModel):
    tags: typing.Optional[DescriptorsTags] = Field(None, alias='tags')

    # The average ratio of the length of the music to the time it takes to render; for example, a render speed of 3.0 generates 30 seconds of music in about 10 seconds
    average_render_speed: typing.Optional[typing.Union[int, float]] = Field(None, alias='average_render_speed')

    # The bands that are available to use this descriptor
    bands: typing.Optional[typing.List[Bands]] = Field(None, alias='bands')

    # The ID of the descriptor
    id: typing.Optional[str] = Field(None, alias='id')

    # The instruments that can play with this descriptor
    instruments: typing.Optional[typing.List[Instruments]] = Field(None, alias='instruments')

    # The maximum beats per minute that the descriptor is intended to be used with
    max_tempo: typing.Optional[typing.Union[int, float]] = Field(None, alias='max_tempo')

    # The minimum beats per minute that the descriptor is intended to be used with
    min_tempo: typing.Optional[typing.Union[int, float]] = Field(None, alias='min_tempo')

    # The name of the descriptor
    name: typing.Optional[str] = Field(None, alias='name')

    # Preview of the descriptor
    previews: typing.Optional[typing.List[Preview]] = Field(None, alias='previews')
    class Config:
        arbitrary_types_allowed = True
