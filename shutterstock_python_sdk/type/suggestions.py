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

from shutterstock_python_sdk.type.suggestions_data import SuggestionsData

class RequiredSuggestions(TypedDict):
    pass

class OptionalSuggestions(TypedDict, total=False):
    data: SuggestionsData

class Suggestions(RequiredSuggestions, OptionalSuggestions):
    pass
