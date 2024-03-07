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

from shutterstock_python_sdk.type.price import Price
from shutterstock_python_sdk.type.url import Url

class RequiredLicenseVideoResult(TypedDict):
    # ID of the video that was licensed
    video_id: str

class OptionalLicenseVideoResult(TypedDict, total=False):
    # Number of credits that this licensing event used
    allotment_charge: int

    download: Url

    # Potential error that occurred during licensing
    error: str

    # ID of the license event
    license_id: str

    price: Price

class LicenseVideoResult(RequiredLicenseVideoResult, OptionalLicenseVideoResult):
    pass