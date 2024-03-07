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

from shutterstock_python_sdk.type.category import Category
from shutterstock_python_sdk.type.contributor import Contributor
from shutterstock_python_sdk.type.model import Model
from shutterstock_python_sdk.type.video_assets import VideoAssets
from shutterstock_python_sdk.type.video_keywords import VideoKeywords

class RequiredVideo(TypedDict):
    contributor: Contributor

    # ID of the video
    id: str

    # Media type of this video, should always be \"video\"
    media_type: str

class OptionalVideo(TypedDict, total=False):
    # Description of this video
    description: str

    # Date this video was added to the Shutterstock library
    added_date: date

    # Affiliate referral link; appears only for registered affiliate partners
    affiliate_url: str

    # Aspect ratio of this video in decimal format, such as 0.6667
    aspect: typing.Union[int, float]

    # Aspect ratio of the video as a ratio, such as 16:9
    aspect_ratio: str

    assets: VideoAssets

    # List of categories
    categories: typing.List[Category]

    # Duration of this video, in seconds
    duration: typing.Union[int, float]

    # Whether or not this video has been released for use by the model appearing in it
    has_model_release: bool

    # Whether or not this video has received a release to show the landmark or property appearing in it
    has_property_release: bool

    # Whether or not this video contains adult content
    is_adult: bool

    # Whether or not this video is editorial content
    is_editorial: bool

    keywords: VideoKeywords

    # List of models in this video
    models: typing.List[Model]

    # Link to video information page; included only for certain accounts
    url: str

class Video(RequiredVideo, OptionalVideo):
    pass
