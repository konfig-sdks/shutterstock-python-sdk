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

from shutterstock_python_sdk.type.bands import Bands
from shutterstock_python_sdk.type.descriptors_tags import DescriptorsTags
from shutterstock_python_sdk.type.instruments import Instruments
from shutterstock_python_sdk.type.preview import Preview

class RequiredDescriptors(TypedDict):
    pass

class OptionalDescriptors(TypedDict, total=False):
    tags: DescriptorsTags

    # The average ratio of the length of the music to the time it takes to render; for example, a render speed of 3.0 generates 30 seconds of music in about 10 seconds
    average_render_speed: typing.Union[int, float]

    # The bands that are available to use this descriptor
    bands: typing.List[Bands]

    # The ID of the descriptor
    id: str

    # The instruments that can play with this descriptor
    instruments: typing.List[Instruments]

    # The maximum beats per minute that the descriptor is intended to be used with
    max_tempo: typing.Union[int, float]

    # The minimum beats per minute that the descriptor is intended to be used with
    min_tempo: typing.Union[int, float]

    # The name of the descriptor
    name: str

    # Preview of the descriptor
    previews: typing.List[Preview]

class Descriptors(RequiredDescriptors, OptionalDescriptors):
    pass
