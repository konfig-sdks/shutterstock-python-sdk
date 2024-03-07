# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import shutterstock_python_sdk
from shutterstock_python_sdk.paths.v2_videos_collections_id_items import post
from shutterstock_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2VideosCollectionsIdItems(ApiTestMixin, unittest.TestCase):
    """
    V2VideosCollectionsIdItems unit test stubs
        Add videos to collections
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''




if __name__ == '__main__':
    unittest.main()
