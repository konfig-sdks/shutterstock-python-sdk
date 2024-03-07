# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_ai_audio_renders.post import CreateRenderedAudio
from shutterstock_python_sdk.paths.v2_ai_audio_renders.get import GetAudioRendersDetails
from shutterstock_python_sdk.paths.v2_ai_audio_descriptors.get import ListAudioDescriptors
from shutterstock_python_sdk.paths.v2_ai_audio_instruments.get import ListComputerAudioInstruments
from shutterstock_python_sdk.apis.tags.custom_music_api_raw import CustomMusicApiRaw


class CustomMusicApi(
    CreateRenderedAudio,
    GetAudioRendersDetails,
    ListAudioDescriptors,
    ListComputerAudioInstruments,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CustomMusicApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CustomMusicApiRaw(api_client)
