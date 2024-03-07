# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_audio_collections_id_items.post import AddTracksToCollectionRaw
from shutterstock_python_sdk.paths.v2_audio_collections.post import CreateCollectionsRaw
from shutterstock_python_sdk.paths.v2_audio_collections_id.delete import DeleteCollectionRaw
from shutterstock_python_sdk.paths.v2_audio_collections_id.get import GetCollectionDetailsRaw
from shutterstock_python_sdk.paths.v2_audio_id.get import GetTrackDetailsRaw
from shutterstock_python_sdk.paths.v2_audio_licenses.post import LicenseTracksRaw
from shutterstock_python_sdk.paths.v2_audio_licenses.get import ListAudioLicensesRaw
from shutterstock_python_sdk.paths.v2_audio_collections_id_items.get import ListCollectionItemsRaw
from shutterstock_python_sdk.paths.v2_audio_collections.get import ListCollectionsRaw
from shutterstock_python_sdk.paths.v2_audio_genres.get import ListGenresRaw
from shutterstock_python_sdk.paths.v2_audio_instruments.get import ListInstrumentsRaw
from shutterstock_python_sdk.paths.v2_audio_moods.get import ListMoodsRaw
from shutterstock_python_sdk.paths.v2_audio.get import ListTracksRaw
from shutterstock_python_sdk.paths.v2_audio_licenses_id_downloads.post import RedownloadTracksRaw
from shutterstock_python_sdk.paths.v2_audio_collections_id_items.delete import RemoveTracksFromCollectionRaw
from shutterstock_python_sdk.paths.v2_audio_search.get import SearchTracksRaw
from shutterstock_python_sdk.paths.v2_audio_collections_id.post import SetCollectionNameRaw


class AudioApiRaw(
    AddTracksToCollectionRaw,
    CreateCollectionsRaw,
    DeleteCollectionRaw,
    GetCollectionDetailsRaw,
    GetTrackDetailsRaw,
    LicenseTracksRaw,
    ListAudioLicensesRaw,
    ListCollectionItemsRaw,
    ListCollectionsRaw,
    ListGenresRaw,
    ListInstrumentsRaw,
    ListMoodsRaw,
    ListTracksRaw,
    RedownloadTracksRaw,
    RemoveTracksFromCollectionRaw,
    SearchTracksRaw,
    SetCollectionNameRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass