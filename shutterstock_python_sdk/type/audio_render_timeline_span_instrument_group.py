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

from shutterstock_python_sdk.type.audio_render_timeline_span_instrument_group_status import AudioRenderTimelineSpanInstrumentGroupStatus

class RequiredAudioRenderTimelineSpanInstrumentGroup(TypedDict):
    # The instrument ID
    instrument_group: str

class OptionalAudioRenderTimelineSpanInstrumentGroup(TypedDict, total=False):
    # An array of status objects
    statuses: typing.List[AudioRenderTimelineSpanInstrumentGroupStatus]

class AudioRenderTimelineSpanInstrumentGroup(RequiredAudioRenderTimelineSpanInstrumentGroup, OptionalAudioRenderTimelineSpanInstrumentGroup):
    pass
