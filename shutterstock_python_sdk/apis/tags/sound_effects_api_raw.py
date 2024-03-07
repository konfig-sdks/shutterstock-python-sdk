# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from shutterstock_python_sdk.paths.v2_sfx_id.get import GetDetailsRaw
from shutterstock_python_sdk.paths.v2_sfx_licenses.post import LicenseAssetsRaw
from shutterstock_python_sdk.paths.v2_sfx.get import ListDetailsRaw
from shutterstock_python_sdk.paths.v2_sfx_licenses.get import ListLicensesRaw
from shutterstock_python_sdk.paths.v2_sfx_licenses_id_downloads.post import RedownloadLicensesRaw
from shutterstock_python_sdk.paths.v2_sfx_search.get import SearchSoundEffectsRaw


class SoundEffectsApiRaw(
    GetDetailsRaw,
    LicenseAssetsRaw,
    ListDetailsRaw,
    ListLicensesRaw,
    RedownloadLicensesRaw,
    SearchSoundEffectsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass