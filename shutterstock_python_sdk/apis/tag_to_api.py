import typing_extensions

from shutterstock_python_sdk.apis.tags import TagValues
from shutterstock_python_sdk.apis.tags.images_api import ImagesApi
from shutterstock_python_sdk.apis.tags.videos_api import VideosApi
from shutterstock_python_sdk.apis.tags.audio_api import AudioApi
from shutterstock_python_sdk.apis.tags.editorial_images_api import EditorialImagesApi
from shutterstock_python_sdk.apis.tags.catalog_api import CatalogApi
from shutterstock_python_sdk.apis.tags.sound_effects_api import SoundEffectsApi
from shutterstock_python_sdk.apis.tags.contributors_api import ContributorsApi
from shutterstock_python_sdk.apis.tags.computer_vision_api import ComputerVisionApi
from shutterstock_python_sdk.apis.tags.editorial_video_api import EditorialVideoApi
from shutterstock_python_sdk.apis.tags.custom_music_api import CustomMusicApi
from shutterstock_python_sdk.apis.tags.users_api import UsersApi
from shutterstock_python_sdk.apis.tags.oauth_api import OauthApi
from shutterstock_python_sdk.apis.tags.test_api import TestApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.IMAGES: ImagesApi,
        TagValues.VIDEOS: VideosApi,
        TagValues.AUDIO: AudioApi,
        TagValues.EDITORIAL_IMAGES: EditorialImagesApi,
        TagValues.CATALOG: CatalogApi,
        TagValues.SOUND_EFFECTS: SoundEffectsApi,
        TagValues.CONTRIBUTORS: ContributorsApi,
        TagValues.COMPUTER_VISION: ComputerVisionApi,
        TagValues.EDITORIAL_VIDEO: EditorialVideoApi,
        TagValues.CUSTOM_MUSIC: CustomMusicApi,
        TagValues.USERS: UsersApi,
        TagValues.OAUTH: OauthApi,
        TagValues.TEST: TestApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.IMAGES: ImagesApi,
        TagValues.VIDEOS: VideosApi,
        TagValues.AUDIO: AudioApi,
        TagValues.EDITORIAL_IMAGES: EditorialImagesApi,
        TagValues.CATALOG: CatalogApi,
        TagValues.SOUND_EFFECTS: SoundEffectsApi,
        TagValues.CONTRIBUTORS: ContributorsApi,
        TagValues.COMPUTER_VISION: ComputerVisionApi,
        TagValues.EDITORIAL_VIDEO: EditorialVideoApi,
        TagValues.CUSTOM_MUSIC: CustomMusicApi,
        TagValues.USERS: UsersApi,
        TagValues.OAUTH: OauthApi,
        TagValues.TEST: TestApi,
    }
)
