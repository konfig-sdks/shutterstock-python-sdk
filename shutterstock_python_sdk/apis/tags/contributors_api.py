# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_contributors_contributor_id_collections_id.get import GetCollectionDetails
from shutterstock_python_sdk.paths.v2_contributors_contributor_id_collections_id_items.get import GetCollectionItems
from shutterstock_python_sdk.paths.v2_contributors_contributor_id.get import GetDetails
from shutterstock_python_sdk.paths.v2_contributors.get import GetDetailsMultiple
from shutterstock_python_sdk.paths.v2_contributors_contributor_id_collections.get import ListCollections
from shutterstock_python_sdk.apis.tags.contributors_api_raw import ContributorsApiRaw


class ContributorsApi(
    GetCollectionDetails,
    GetCollectionItems,
    GetDetails,
    GetDetailsMultiple,
    ListCollections,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ContributorsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ContributorsApiRaw(api_client)