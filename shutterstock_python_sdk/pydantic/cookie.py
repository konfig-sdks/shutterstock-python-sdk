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
from pydantic import BaseModel, Field, RootModel


class Cookie(BaseModel):
    # The name of the cookie
    name: str = Field(alias='name')

    # The value of the cookie
    value: str = Field(alias='value')
    class Config:
        arbitrary_types_allowed = True
