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

from shutterstock_python_sdk.type.audio_render_timeline_span_region_end_type import AudioRenderTimelineSpanRegionEndType
from shutterstock_python_sdk.type.audio_render_timeline_span_region_key import AudioRenderTimelineSpanRegionKey

class RequiredAudioRenderTimelineSpanRegion(TypedDict):
    # The beat, relative to the span, at which the region object's music begins
    beat: int

    # The descriptor ID needed to compose the music
    descriptor: str

    # An identifier which must be unique within the parent span
    id: typing.Union[int, float]

    # The type of region
    region: str

class OptionalAudioRenderTimelineSpanRegion(TypedDict, total=False):
    end_type: AudioRenderTimelineSpanRegionEndType

    key: AudioRenderTimelineSpanRegionKey

class AudioRenderTimelineSpanRegion(RequiredAudioRenderTimelineSpanRegion, OptionalAudioRenderTimelineSpanRegion):
    pass