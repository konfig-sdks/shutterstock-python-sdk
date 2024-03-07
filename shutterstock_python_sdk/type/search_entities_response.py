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


class RequiredSearchEntitiesResponse(TypedDict):
    pass

class OptionalSearchEntitiesResponse(TypedDict, total=False):
    # The top keywords from the submitted text
    keywords: typing.List[str]

class SearchEntitiesResponse(RequiredSearchEntitiesResponse, OptionalSearchEntitiesResponse):
    pass