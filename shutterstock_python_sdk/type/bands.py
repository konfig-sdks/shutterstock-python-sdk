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


class RequiredBands(TypedDict):
    pass

class OptionalBands(TypedDict, total=False):
    # The ID of the band
    id: str

    # The name of the band
    name: str

class Bands(RequiredBands, OptionalBands):
    pass