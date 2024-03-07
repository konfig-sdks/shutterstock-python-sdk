# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_images_collections_id_items.post import AddToCollectionItems
from shutterstock_python_sdk.paths.v2_images_collections.post import CreateCollection
from shutterstock_python_sdk.paths.v2_images_collections_id.delete import DeleteCollection
from shutterstock_python_sdk.paths.v2_images_search_suggestions.post import ExtractKeywordsFromText
from shutterstock_python_sdk.paths.v2_images_collections_featured_id.get import FeaturedCollectionDetails
from shutterstock_python_sdk.paths.v2_images_collections_id.get import GetCollectionDetails
from shutterstock_python_sdk.paths.v2_images_collections_featured_id_items.get import GetCollectionItems
from shutterstock_python_sdk.paths.v2_images_collections_id_items.get import GetCollectionItems0
from shutterstock_python_sdk.paths.v2_images_id.get import GetDetails
from shutterstock_python_sdk.paths.v2_images_search_suggestions.get import GetSearchSuggestions
from shutterstock_python_sdk.paths.v2_images_licenses.post import LicenseImagesForMultiple
from shutterstock_python_sdk.paths.v2_images_categories.get import ListCategories
from shutterstock_python_sdk.paths.v2_images_collections.get import ListCollections
from shutterstock_python_sdk.paths.v2_images_collections_featured.get import ListFeaturedCollections
from shutterstock_python_sdk.paths.v2_images.get import ListInfo
from shutterstock_python_sdk.paths.v2_images_licenses.get import ListLicenses
from shutterstock_python_sdk.paths.v2_images_recommendations.get import ListRecommendedImages
from shutterstock_python_sdk.paths.v2_images_id_similar.get import ListSimilarImages
from shutterstock_python_sdk.paths.v2_images_updated.get import ListUpdatedContent
from shutterstock_python_sdk.paths.v2_images_licenses_id_downloads.post import RedownloadLicense
from shutterstock_python_sdk.paths.v2_images_collections_id_items.delete import RemoveFromCollection
from shutterstock_python_sdk.paths.v2_images_collections_id.post import RenameCollection
from shutterstock_python_sdk.paths.v2_bulk_search_images.post import RunMultipleSearches
from shutterstock_python_sdk.paths.v2_images_search.get import SearchImages
from shutterstock_python_sdk.apis.tags.images_api_raw import ImagesApiRaw


class ImagesApi(
    AddToCollectionItems,
    CreateCollection,
    DeleteCollection,
    ExtractKeywordsFromText,
    FeaturedCollectionDetails,
    GetCollectionDetails,
    GetCollectionItems,
    GetCollectionItems0,
    GetDetails,
    GetSearchSuggestions,
    LicenseImagesForMultiple,
    ListCategories,
    ListCollections,
    ListFeaturedCollections,
    ListInfo,
    ListLicenses,
    ListRecommendedImages,
    ListSimilarImages,
    ListUpdatedContent,
    RedownloadLicense,
    RemoveFromCollection,
    RenameCollection,
    RunMultipleSearches,
    SearchImages,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ImagesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ImagesApiRaw(api_client)
