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
from shutterstock_python_sdk.paths.v2_audio_collections_id import delete
from shutterstock_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2AudioCollectionsId(ApiTestMixin, unittest.TestCase):
    """
    V2AudioCollectionsId unit test stubs
        Delete audio collections
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
