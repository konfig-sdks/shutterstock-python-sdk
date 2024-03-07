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

from shutterstock_python_sdk.type.audio_asset_details import AudioAssetDetails
from shutterstock_python_sdk.type.shorts_loops_stems import ShortsLoopsStems

class RequiredAudioAssets(TypedDict):
    pass

class OptionalAudioAssets(TypedDict, total=False):
    album_art: AudioAssetDetails

    clean_audio: AudioAssetDetails

    original_audio: AudioAssetDetails

    preview_mp3: AudioAssetDetails

    preview_ogg: AudioAssetDetails

    shorts_loops_stems: ShortsLoopsStems

    waveform: AudioAssetDetails

class AudioAssets(RequiredAudioAssets, OptionalAudioAssets):
    pass
