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

from shutterstock_python_sdk.type.error import Error
from shutterstock_python_sdk.type.license_sfx_result import LicenseSFXResult

class RequiredLicenseSFXResultDataList(TypedDict):
    pass

class OptionalLicenseSFXResultDataList(TypedDict, total=False):
    # Sound effects license results
    data: typing.List[LicenseSFXResult]

    # Error list; appears only if there was an error
    errors: typing.List[Error]

    # Server-generated message, if any
    message: str

class LicenseSFXResultDataList(RequiredLicenseSFXResultDataList, OptionalLicenseSFXResultDataList):
    pass
