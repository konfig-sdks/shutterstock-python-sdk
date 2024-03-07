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


class RequiredContributorProfileSocialMedia(TypedDict):
    pass

class OptionalContributorProfileSocialMedia(TypedDict, total=False):
    # Facebook link for contributor
    facebook: str

    # Google+ link for contributor
    google_plus: str

    # LinkedIn link for contributor
    linkedin: str

    # Pinterest page for contributor
    pinterest: str

    # Tumblr link for contributor
    tumblr: str

    # Twitter link for contributor
    twitter: str

class ContributorProfileSocialMedia(RequiredContributorProfileSocialMedia, OptionalContributorProfileSocialMedia):
    pass