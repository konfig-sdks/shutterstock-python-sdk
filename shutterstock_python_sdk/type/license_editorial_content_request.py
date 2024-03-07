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

from shutterstock_python_sdk.type.iso_country_code import ISOCountryCode
from shutterstock_python_sdk.type.license_editorial_content import LicenseEditorialContent

class RequiredLicenseEditorialContentRequest(TypedDict):
    country: ISOCountryCode

    # Editorial content to license
    editorial: typing.List[LicenseEditorialContent]

class OptionalLicenseEditorialContentRequest(TypedDict, total=False):
    pass

class LicenseEditorialContentRequest(RequiredLicenseEditorialContentRequest, OptionalLicenseEditorialContentRequest):
    pass
