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
from shutterstock_python_sdk.paths.v2_cv_similar_videos import get
from shutterstock_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2CvSimilarVideos(ApiTestMixin, unittest.TestCase):
    """
    V2CvSimilarVideos unit test stubs
        List similar videos
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
