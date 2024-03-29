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

from shutterstock_python_sdk.type.audio_renders_files_list_tracks import AudioRendersFilesListTracks

class RequiredAudioRendersFilesList(TypedDict):
    # The bit depth of the audio files in bits/sample
    bits_sample: typing.Union[int, float]

    # The content-type of the file
    content_type: str

    # The internet-accessible URL from which the file can be downloaded. Any redirects encountered when using this URL must be followed
    download_url: str

    # The user-specified file name suggestion from the render request; this file name becomes the filename property of the Content-Disposition header when the user downloads the rendered audio file
    filename: str

    # The Sample rate of the audio files in Hertz (Hz)
    frequency_hz: typing.Union[int, float]

    # The data rate of the audio files in kilobits/second
    kbits_second: typing.Union[int, float]

    # Size of the file in bytes
    size_bytes: typing.Union[int, float]

    tracks: AudioRendersFilesListTracks

class OptionalAudioRendersFilesList(TypedDict, total=False):
    pass

class AudioRendersFilesList(RequiredAudioRendersFilesList, OptionalAudioRendersFilesList):
    pass
