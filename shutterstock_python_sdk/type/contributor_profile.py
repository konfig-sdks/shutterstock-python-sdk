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

from shutterstock_python_sdk.type.contributor_profile_contributor_type import ContributorProfileContributorType
from shutterstock_python_sdk.type.contributor_profile_equipment import ContributorProfileEquipment
from shutterstock_python_sdk.type.contributor_profile_social_media import ContributorProfileSocialMedia
from shutterstock_python_sdk.type.contributor_profile_styles import ContributorProfileStyles
from shutterstock_python_sdk.type.contributor_profile_subjects import ContributorProfileSubjects

class RequiredContributorProfile(TypedDict):
    # Contributor ID
    id: str

class OptionalContributorProfile(TypedDict, total=False):
    # Short description of the contributors' library
    about: str

    contributor_type: ContributorProfileContributorType

    # Preferred name to be displayed for the contributor
    display_name: str

    equipment: ContributorProfileEquipment

    # Country code representing the contributor's locale
    location: str

    # Web URL for the contributors' profile
    portfolio_url: str

    social_media: ContributorProfileSocialMedia

    styles: ContributorProfileStyles

    subjects: ContributorProfileSubjects

    # Personal website for the contributor
    website: str

class ContributorProfile(RequiredContributorProfile, OptionalContributorProfile):
    pass