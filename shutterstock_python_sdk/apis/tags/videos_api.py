# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_videos_collections_id_items.post import AddToCollectionItems
from shutterstock_python_sdk.paths.v2_videos_collections_featured_id.get import CollectionDetailsGet
from shutterstock_python_sdk.paths.v2_videos_collections_id.get import CollectionDetailsGet0
from shutterstock_python_sdk.paths.v2_videos_collections.post import CreateVideoCollections
from shutterstock_python_sdk.paths.v2_videos_collections_id.delete import DeleteCollection
from shutterstock_python_sdk.paths.v2_videos_id_similar.get import FindSimilar
from shutterstock_python_sdk.paths.v2_videos_collections_id_items.get import GetCollectionItems
from shutterstock_python_sdk.paths.v2_videos_collections_featured_id_items.get import GetFeaturedCollectionItems
from shutterstock_python_sdk.paths.v2_videos_licenses.post import LicenseVideos
from shutterstock_python_sdk.paths.v2_videos_categories.get import ListCategories
from shutterstock_python_sdk.paths.v2_videos_collections.get import ListCollections
from shutterstock_python_sdk.paths.v2_videos_collections_featured.get import ListFeaturedVideoCollections
from shutterstock_python_sdk.paths.v2_videos_licenses.get import ListLicenses
from shutterstock_python_sdk.paths.v2_videos_updated.get import ListUpdatedVideos
from shutterstock_python_sdk.paths.v2_videos.get import ListVideo
from shutterstock_python_sdk.paths.v2_videos_licenses_id_downloads.post import RedownloadDownloads
from shutterstock_python_sdk.paths.v2_videos_collections_id_items.delete import RemoveFromCollection
from shutterstock_python_sdk.paths.v2_videos_search_suggestions.get import SearchSuggestions
from shutterstock_python_sdk.paths.v2_videos_search.get import SearchVideo
from shutterstock_python_sdk.paths.v2_videos_collections_id.post import SetNewName
from shutterstock_python_sdk.paths.v2_videos_id.get import VideoDetails
from shutterstock_python_sdk.apis.tags.videos_api_raw import VideosApiRaw


class VideosApi(
    AddToCollectionItems,
    CollectionDetailsGet,
    CollectionDetailsGet0,
    CreateVideoCollections,
    DeleteCollection,
    FindSimilar,
    GetCollectionItems,
    GetFeaturedCollectionItems,
    LicenseVideos,
    ListCategories,
    ListCollections,
    ListFeaturedVideoCollections,
    ListLicenses,
    ListUpdatedVideos,
    ListVideo,
    RedownloadDownloads,
    RemoveFromCollection,
    SearchSuggestions,
    SearchVideo,
    SetNewName,
    VideoDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: VideosApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = VideosApiRaw(api_client)
