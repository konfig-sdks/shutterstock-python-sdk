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


class ContributorProfileSocialMedia(BaseModel):
    # Facebook link for contributor
    facebook: typing.Optional[str] = Field(None, alias='facebook')

    # Google+ link for contributor
    google_plus: typing.Optional[str] = Field(None, alias='google_plus')

    # LinkedIn link for contributor
    linkedin: typing.Optional[str] = Field(None, alias='linkedin')

    # Pinterest page for contributor
    pinterest: typing.Optional[str] = Field(None, alias='pinterest')

    # Tumblr link for contributor
    tumblr: typing.Optional[str] = Field(None, alias='tumblr')

    # Twitter link for contributor
    twitter: typing.Optional[str] = Field(None, alias='twitter')
    class Config:
        arbitrary_types_allowed = True