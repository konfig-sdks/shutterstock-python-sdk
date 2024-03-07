# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from shutterstock_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    IMAGES = "images"
    VIDEOS = "videos"
    AUDIO = "audio"
    EDITORIAL_IMAGES = "editorial_images"
    CATALOG = "catalog"
    SOUND_EFFECTS = "sound_effects"
    CONTRIBUTORS = "contributors"
    COMPUTER_VISION = "computer_vision"
    EDITORIAL_VIDEO = "editorial_video"
    CUSTOM_MUSIC = "custom_music"
    USERS = "users"
    OAUTH = "oauth"
    TEST = "test"
