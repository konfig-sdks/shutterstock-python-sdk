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

from shutterstock_python_sdk.pydantic.category import Category
from shutterstock_python_sdk.pydantic.contributor import Contributor
from shutterstock_python_sdk.pydantic.model import Model
from shutterstock_python_sdk.pydantic.video_assets import VideoAssets
from shutterstock_python_sdk.pydantic.video_keywords import VideoKeywords

class Video(BaseModel):
    contributor: Contributor = Field(alias='contributor')

    # ID of the video
    id: str = Field(alias='id')

    # Media type of this video, should always be \"video\"
    media_type: str = Field(alias='media_type')

    # Description of this video
    description: typing.Optional[str] = Field(None, alias='description')

    # Date this video was added to the Shutterstock library
    added_date: typing.Optional[date] = Field(None, alias='added_date')

    # Affiliate referral link; appears only for registered affiliate partners
    affiliate_url: typing.Optional[str] = Field(None, alias='affiliate_url')

    # Aspect ratio of this video in decimal format, such as 0.6667
    aspect: typing.Optional[typing.Union[int, float]] = Field(None, alias='aspect')

    # Aspect ratio of the video as a ratio, such as 16:9
    aspect_ratio: typing.Optional[str] = Field(None, alias='aspect_ratio')

    assets: typing.Optional[VideoAssets] = Field(None, alias='assets')

    # List of categories
    categories: typing.Optional[typing.List[Category]] = Field(None, alias='categories')

    # Duration of this video, in seconds
    duration: typing.Optional[typing.Union[int, float]] = Field(None, alias='duration')

    # Whether or not this video has been released for use by the model appearing in it
    has_model_release: typing.Optional[bool] = Field(None, alias='has_model_release')

    # Whether or not this video has received a release to show the landmark or property appearing in it
    has_property_release: typing.Optional[bool] = Field(None, alias='has_property_release')

    # Whether or not this video contains adult content
    is_adult: typing.Optional[bool] = Field(None, alias='is_adult')

    # Whether or not this video is editorial content
    is_editorial: typing.Optional[bool] = Field(None, alias='is_editorial')

    keywords: typing.Optional[VideoKeywords] = Field(None, alias='keywords')

    # List of models in this video
    models: typing.Optional[typing.List[Model]] = Field(None, alias='models')

    # Link to video information page; included only for certain accounts
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
