import typing_extensions

from shutterstock_python_sdk.paths import PathValues
from shutterstock_python_sdk.apis.paths.v2_ai_audio_descriptors import V2AiAudioDescriptors
from shutterstock_python_sdk.apis.paths.v2_ai_audio_instruments import V2AiAudioInstruments
from shutterstock_python_sdk.apis.paths.v2_ai_audio_renders import V2AiAudioRenders
from shutterstock_python_sdk.apis.paths.v2_audio import V2Audio
from shutterstock_python_sdk.apis.paths.v2_audio_collections import V2AudioCollections
from shutterstock_python_sdk.apis.paths.v2_audio_collections_id import V2AudioCollectionsId
from shutterstock_python_sdk.apis.paths.v2_audio_collections_id_items import V2AudioCollectionsIdItems
from shutterstock_python_sdk.apis.paths.v2_audio_genres import V2AudioGenres
from shutterstock_python_sdk.apis.paths.v2_audio_instruments import V2AudioInstruments
from shutterstock_python_sdk.apis.paths.v2_audio_licenses import V2AudioLicenses
from shutterstock_python_sdk.apis.paths.v2_audio_licenses_id_downloads import V2AudioLicensesIdDownloads
from shutterstock_python_sdk.apis.paths.v2_audio_moods import V2AudioMoods
from shutterstock_python_sdk.apis.paths.v2_audio_search import V2AudioSearch
from shutterstock_python_sdk.apis.paths.v2_audio_id import V2AudioId
from shutterstock_python_sdk.apis.paths.v2_bulk_search_images import V2BulkSearchImages
from shutterstock_python_sdk.apis.paths.v2_catalog_collections import V2CatalogCollections
from shutterstock_python_sdk.apis.paths.v2_catalog_collections_collection_id import V2CatalogCollectionsCollectionId
from shutterstock_python_sdk.apis.paths.v2_catalog_collections_collection_id_items import V2CatalogCollectionsCollectionIdItems
from shutterstock_python_sdk.apis.paths.v2_catalog_search import V2CatalogSearch
from shutterstock_python_sdk.apis.paths.v2_contributors import V2Contributors
from shutterstock_python_sdk.apis.paths.v2_contributors_contributor_id import V2ContributorsContributorId
from shutterstock_python_sdk.apis.paths.v2_contributors_contributor_id_collections import V2ContributorsContributorIdCollections
from shutterstock_python_sdk.apis.paths.v2_contributors_contributor_id_collections_id import V2ContributorsContributorIdCollectionsId
from shutterstock_python_sdk.apis.paths.v2_contributors_contributor_id_collections_id_items import V2ContributorsContributorIdCollectionsIdItems
from shutterstock_python_sdk.apis.paths.v2_cv_images import V2CvImages
from shutterstock_python_sdk.apis.paths.v2_cv_keywords import V2CvKeywords
from shutterstock_python_sdk.apis.paths.v2_cv_similar_images import V2CvSimilarImages
from shutterstock_python_sdk.apis.paths.v2_cv_similar_videos import V2CvSimilarVideos
from shutterstock_python_sdk.apis.paths.v2_editorial_categories import V2EditorialCategories
from shutterstock_python_sdk.apis.paths.v2_editorial_images_categories import V2EditorialImagesCategories
from shutterstock_python_sdk.apis.paths.v2_editorial_images_licenses import V2EditorialImagesLicenses
from shutterstock_python_sdk.apis.paths.v2_editorial_images_livefeeds import V2EditorialImagesLivefeeds
from shutterstock_python_sdk.apis.paths.v2_editorial_images_livefeeds_id import V2EditorialImagesLivefeedsId
from shutterstock_python_sdk.apis.paths.v2_editorial_images_livefeeds_id_items import V2EditorialImagesLivefeedsIdItems
from shutterstock_python_sdk.apis.paths.v2_editorial_images_search import V2EditorialImagesSearch
from shutterstock_python_sdk.apis.paths.v2_editorial_images_updated import V2EditorialImagesUpdated
from shutterstock_python_sdk.apis.paths.v2_editorial_images_id import V2EditorialImagesId
from shutterstock_python_sdk.apis.paths.v2_editorial_licenses import V2EditorialLicenses
from shutterstock_python_sdk.apis.paths.v2_editorial_livefeeds import V2EditorialLivefeeds
from shutterstock_python_sdk.apis.paths.v2_editorial_livefeeds_id import V2EditorialLivefeedsId
from shutterstock_python_sdk.apis.paths.v2_editorial_livefeeds_id_items import V2EditorialLivefeedsIdItems
from shutterstock_python_sdk.apis.paths.v2_editorial_search import V2EditorialSearch
from shutterstock_python_sdk.apis.paths.v2_editorial_updated import V2EditorialUpdated
from shutterstock_python_sdk.apis.paths.v2_editorial_videos_categories import V2EditorialVideosCategories
from shutterstock_python_sdk.apis.paths.v2_editorial_videos_licenses import V2EditorialVideosLicenses
from shutterstock_python_sdk.apis.paths.v2_editorial_videos_search import V2EditorialVideosSearch
from shutterstock_python_sdk.apis.paths.v2_editorial_videos_id import V2EditorialVideosId
from shutterstock_python_sdk.apis.paths.v2_editorial_id import V2EditorialId
from shutterstock_python_sdk.apis.paths.v2_images import V2Images
from shutterstock_python_sdk.apis.paths.v2_images_categories import V2ImagesCategories
from shutterstock_python_sdk.apis.paths.v2_images_collections import V2ImagesCollections
from shutterstock_python_sdk.apis.paths.v2_images_collections_featured import V2ImagesCollectionsFeatured
from shutterstock_python_sdk.apis.paths.v2_images_collections_featured_id import V2ImagesCollectionsFeaturedId
from shutterstock_python_sdk.apis.paths.v2_images_collections_featured_id_items import V2ImagesCollectionsFeaturedIdItems
from shutterstock_python_sdk.apis.paths.v2_images_collections_id import V2ImagesCollectionsId
from shutterstock_python_sdk.apis.paths.v2_images_collections_id_items import V2ImagesCollectionsIdItems
from shutterstock_python_sdk.apis.paths.v2_images_licenses import V2ImagesLicenses
from shutterstock_python_sdk.apis.paths.v2_images_licenses_id_downloads import V2ImagesLicensesIdDownloads
from shutterstock_python_sdk.apis.paths.v2_images_recommendations import V2ImagesRecommendations
from shutterstock_python_sdk.apis.paths.v2_images_search import V2ImagesSearch
from shutterstock_python_sdk.apis.paths.v2_images_search_suggestions import V2ImagesSearchSuggestions
from shutterstock_python_sdk.apis.paths.v2_images_updated import V2ImagesUpdated
from shutterstock_python_sdk.apis.paths.v2_images_id import V2ImagesId
from shutterstock_python_sdk.apis.paths.v2_images_id_similar import V2ImagesIdSimilar
from shutterstock_python_sdk.apis.paths.v2_oauth_access_token import V2OauthAccessToken
from shutterstock_python_sdk.apis.paths.v2_oauth_authorize import V2OauthAuthorize
from shutterstock_python_sdk.apis.paths.v2_sfx import V2Sfx
from shutterstock_python_sdk.apis.paths.v2_sfx_licenses import V2SfxLicenses
from shutterstock_python_sdk.apis.paths.v2_sfx_licenses_id_downloads import V2SfxLicensesIdDownloads
from shutterstock_python_sdk.apis.paths.v2_sfx_search import V2SfxSearch
from shutterstock_python_sdk.apis.paths.v2_sfx_id import V2SfxId
from shutterstock_python_sdk.apis.paths.v2_test import V2Test
from shutterstock_python_sdk.apis.paths.v2_test_validate import V2TestValidate
from shutterstock_python_sdk.apis.paths.v2_user import V2User
from shutterstock_python_sdk.apis.paths.v2_user_access_token import V2UserAccessToken
from shutterstock_python_sdk.apis.paths.v2_user_subscriptions import V2UserSubscriptions
from shutterstock_python_sdk.apis.paths.v2_videos import V2Videos
from shutterstock_python_sdk.apis.paths.v2_videos_categories import V2VideosCategories
from shutterstock_python_sdk.apis.paths.v2_videos_collections import V2VideosCollections
from shutterstock_python_sdk.apis.paths.v2_videos_collections_featured import V2VideosCollectionsFeatured
from shutterstock_python_sdk.apis.paths.v2_videos_collections_featured_id import V2VideosCollectionsFeaturedId
from shutterstock_python_sdk.apis.paths.v2_videos_collections_featured_id_items import V2VideosCollectionsFeaturedIdItems
from shutterstock_python_sdk.apis.paths.v2_videos_collections_id import V2VideosCollectionsId
from shutterstock_python_sdk.apis.paths.v2_videos_collections_id_items import V2VideosCollectionsIdItems
from shutterstock_python_sdk.apis.paths.v2_videos_licenses import V2VideosLicenses
from shutterstock_python_sdk.apis.paths.v2_videos_licenses_id_downloads import V2VideosLicensesIdDownloads
from shutterstock_python_sdk.apis.paths.v2_videos_search import V2VideosSearch
from shutterstock_python_sdk.apis.paths.v2_videos_search_suggestions import V2VideosSearchSuggestions
from shutterstock_python_sdk.apis.paths.v2_videos_updated import V2VideosUpdated
from shutterstock_python_sdk.apis.paths.v2_videos_id import V2VideosId
from shutterstock_python_sdk.apis.paths.v2_videos_id_similar import V2VideosIdSimilar

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_AI_AUDIO_DESCRIPTORS: V2AiAudioDescriptors,
        PathValues.V2_AI_AUDIO_INSTRUMENTS: V2AiAudioInstruments,
        PathValues.V2_AI_AUDIO_RENDERS: V2AiAudioRenders,
        PathValues.V2_AUDIO: V2Audio,
        PathValues.V2_AUDIO_COLLECTIONS: V2AudioCollections,
        PathValues.V2_AUDIO_COLLECTIONS_ID: V2AudioCollectionsId,
        PathValues.V2_AUDIO_COLLECTIONS_ID_ITEMS: V2AudioCollectionsIdItems,
        PathValues.V2_AUDIO_GENRES: V2AudioGenres,
        PathValues.V2_AUDIO_INSTRUMENTS: V2AudioInstruments,
        PathValues.V2_AUDIO_LICENSES: V2AudioLicenses,
        PathValues.V2_AUDIO_LICENSES_ID_DOWNLOADS: V2AudioLicensesIdDownloads,
        PathValues.V2_AUDIO_MOODS: V2AudioMoods,
        PathValues.V2_AUDIO_SEARCH: V2AudioSearch,
        PathValues.V2_AUDIO_ID: V2AudioId,
        PathValues.V2_BULK_SEARCH_IMAGES: V2BulkSearchImages,
        PathValues.V2_CATALOG_COLLECTIONS: V2CatalogCollections,
        PathValues.V2_CATALOG_COLLECTIONS_COLLECTION_ID: V2CatalogCollectionsCollectionId,
        PathValues.V2_CATALOG_COLLECTIONS_COLLECTION_ID_ITEMS: V2CatalogCollectionsCollectionIdItems,
        PathValues.V2_CATALOG_SEARCH: V2CatalogSearch,
        PathValues.V2_CONTRIBUTORS: V2Contributors,
        PathValues.V2_CONTRIBUTORS_CONTRIBUTOR_ID: V2ContributorsContributorId,
        PathValues.V2_CONTRIBUTORS_CONTRIBUTOR_ID_COLLECTIONS: V2ContributorsContributorIdCollections,
        PathValues.V2_CONTRIBUTORS_CONTRIBUTOR_ID_COLLECTIONS_ID: V2ContributorsContributorIdCollectionsId,
        PathValues.V2_CONTRIBUTORS_CONTRIBUTOR_ID_COLLECTIONS_ID_ITEMS: V2ContributorsContributorIdCollectionsIdItems,
        PathValues.V2_CV_IMAGES: V2CvImages,
        PathValues.V2_CV_KEYWORDS: V2CvKeywords,
        PathValues.V2_CV_SIMILAR_IMAGES: V2CvSimilarImages,
        PathValues.V2_CV_SIMILAR_VIDEOS: V2CvSimilarVideos,
        PathValues.V2_EDITORIAL_CATEGORIES: V2EditorialCategories,
        PathValues.V2_EDITORIAL_IMAGES_CATEGORIES: V2EditorialImagesCategories,
        PathValues.V2_EDITORIAL_IMAGES_LICENSES: V2EditorialImagesLicenses,
        PathValues.V2_EDITORIAL_IMAGES_LIVEFEEDS: V2EditorialImagesLivefeeds,
        PathValues.V2_EDITORIAL_IMAGES_LIVEFEEDS_ID: V2EditorialImagesLivefeedsId,
        PathValues.V2_EDITORIAL_IMAGES_LIVEFEEDS_ID_ITEMS: V2EditorialImagesLivefeedsIdItems,
        PathValues.V2_EDITORIAL_IMAGES_SEARCH: V2EditorialImagesSearch,
        PathValues.V2_EDITORIAL_IMAGES_UPDATED: V2EditorialImagesUpdated,
        PathValues.V2_EDITORIAL_IMAGES_ID: V2EditorialImagesId,
        PathValues.V2_EDITORIAL_LICENSES: V2EditorialLicenses,
        PathValues.V2_EDITORIAL_LIVEFEEDS: V2EditorialLivefeeds,
        PathValues.V2_EDITORIAL_LIVEFEEDS_ID: V2EditorialLivefeedsId,
        PathValues.V2_EDITORIAL_LIVEFEEDS_ID_ITEMS: V2EditorialLivefeedsIdItems,
        PathValues.V2_EDITORIAL_SEARCH: V2EditorialSearch,
        PathValues.V2_EDITORIAL_UPDATED: V2EditorialUpdated,
        PathValues.V2_EDITORIAL_VIDEOS_CATEGORIES: V2EditorialVideosCategories,
        PathValues.V2_EDITORIAL_VIDEOS_LICENSES: V2EditorialVideosLicenses,
        PathValues.V2_EDITORIAL_VIDEOS_SEARCH: V2EditorialVideosSearch,
        PathValues.V2_EDITORIAL_VIDEOS_ID: V2EditorialVideosId,
        PathValues.V2_EDITORIAL_ID: V2EditorialId,
        PathValues.V2_IMAGES: V2Images,
        PathValues.V2_IMAGES_CATEGORIES: V2ImagesCategories,
        PathValues.V2_IMAGES_COLLECTIONS: V2ImagesCollections,
        PathValues.V2_IMAGES_COLLECTIONS_FEATURED: V2ImagesCollectionsFeatured,
        PathValues.V2_IMAGES_COLLECTIONS_FEATURED_ID: V2ImagesCollectionsFeaturedId,
        PathValues.V2_IMAGES_COLLECTIONS_FEATURED_ID_ITEMS: V2ImagesCollectionsFeaturedIdItems,
        PathValues.V2_IMAGES_COLLECTIONS_ID: V2ImagesCollectionsId,
        PathValues.V2_IMAGES_COLLECTIONS_ID_ITEMS: V2ImagesCollectionsIdItems,
        PathValues.V2_IMAGES_LICENSES: V2ImagesLicenses,
        PathValues.V2_IMAGES_LICENSES_ID_DOWNLOADS: V2ImagesLicensesIdDownloads,
        PathValues.V2_IMAGES_RECOMMENDATIONS: V2ImagesRecommendations,
        PathValues.V2_IMAGES_SEARCH: V2ImagesSearch,
        PathValues.V2_IMAGES_SEARCH_SUGGESTIONS: V2ImagesSearchSuggestions,
        PathValues.V2_IMAGES_UPDATED: V2ImagesUpdated,
        PathValues.V2_IMAGES_ID: V2ImagesId,
        PathValues.V2_IMAGES_ID_SIMILAR: V2ImagesIdSimilar,
        PathValues.V2_OAUTH_ACCESS_TOKEN: V2OauthAccessToken,
        PathValues.V2_OAUTH_AUTHORIZE: V2OauthAuthorize,
        PathValues.V2_SFX: V2Sfx,
        PathValues.V2_SFX_LICENSES: V2SfxLicenses,
        PathValues.V2_SFX_LICENSES_ID_DOWNLOADS: V2SfxLicensesIdDownloads,
        PathValues.V2_SFX_SEARCH: V2SfxSearch,
        PathValues.V2_SFX_ID: V2SfxId,
        PathValues.V2_TEST: V2Test,
        PathValues.V2_TEST_VALIDATE: V2TestValidate,
        PathValues.V2_USER: V2User,
        PathValues.V2_USER_ACCESS_TOKEN: V2UserAccessToken,
        PathValues.V2_USER_SUBSCRIPTIONS: V2UserSubscriptions,
        PathValues.V2_VIDEOS: V2Videos,
        PathValues.V2_VIDEOS_CATEGORIES: V2VideosCategories,
        PathValues.V2_VIDEOS_COLLECTIONS: V2VideosCollections,
        PathValues.V2_VIDEOS_COLLECTIONS_FEATURED: V2VideosCollectionsFeatured,
        PathValues.V2_VIDEOS_COLLECTIONS_FEATURED_ID: V2VideosCollectionsFeaturedId,
        PathValues.V2_VIDEOS_COLLECTIONS_FEATURED_ID_ITEMS: V2VideosCollectionsFeaturedIdItems,
        PathValues.V2_VIDEOS_COLLECTIONS_ID: V2VideosCollectionsId,
        PathValues.V2_VIDEOS_COLLECTIONS_ID_ITEMS: V2VideosCollectionsIdItems,
        PathValues.V2_VIDEOS_LICENSES: V2VideosLicenses,
        PathValues.V2_VIDEOS_LICENSES_ID_DOWNLOADS: V2VideosLicensesIdDownloads,
        PathValues.V2_VIDEOS_SEARCH: V2VideosSearch,
        PathValues.V2_VIDEOS_SEARCH_SUGGESTIONS: V2VideosSearchSuggestions,
        PathValues.V2_VIDEOS_UPDATED: V2VideosUpdated,
        PathValues.V2_VIDEOS_ID: V2VideosId,
        PathValues.V2_VIDEOS_ID_SIMILAR: V2VideosIdSimilar,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_AI_AUDIO_DESCRIPTORS: V2AiAudioDescriptors,
        PathValues.V2_AI_AUDIO_INSTRUMENTS: V2AiAudioInstruments,
        PathValues.V2_AI_AUDIO_RENDERS: V2AiAudioRenders,
        PathValues.V2_AUDIO: V2Audio,
        PathValues.V2_AUDIO_COLLECTIONS: V2AudioCollections,
        PathValues.V2_AUDIO_COLLECTIONS_ID: V2AudioCollectionsId,
        PathValues.V2_AUDIO_COLLECTIONS_ID_ITEMS: V2AudioCollectionsIdItems,
        PathValues.V2_AUDIO_GENRES: V2AudioGenres,
        PathValues.V2_AUDIO_INSTRUMENTS: V2AudioInstruments,
        PathValues.V2_AUDIO_LICENSES: V2AudioLicenses,
        PathValues.V2_AUDIO_LICENSES_ID_DOWNLOADS: V2AudioLicensesIdDownloads,
        PathValues.V2_AUDIO_MOODS: V2AudioMoods,
        PathValues.V2_AUDIO_SEARCH: V2AudioSearch,
        PathValues.V2_AUDIO_ID: V2AudioId,
        PathValues.V2_BULK_SEARCH_IMAGES: V2BulkSearchImages,
        PathValues.V2_CATALOG_COLLECTIONS: V2CatalogCollections,
        PathValues.V2_CATALOG_COLLECTIONS_COLLECTION_ID: V2CatalogCollectionsCollectionId,
        PathValues.V2_CATALOG_COLLECTIONS_COLLECTION_ID_ITEMS: V2CatalogCollectionsCollectionIdItems,
        PathValues.V2_CATALOG_SEARCH: V2CatalogSearch,
        PathValues.V2_CONTRIBUTORS: V2Contributors,
        PathValues.V2_CONTRIBUTORS_CONTRIBUTOR_ID: V2ContributorsContributorId,
        PathValues.V2_CONTRIBUTORS_CONTRIBUTOR_ID_COLLECTIONS: V2ContributorsContributorIdCollections,
        PathValues.V2_CONTRIBUTORS_CONTRIBUTOR_ID_COLLECTIONS_ID: V2ContributorsContributorIdCollectionsId,
        PathValues.V2_CONTRIBUTORS_CONTRIBUTOR_ID_COLLECTIONS_ID_ITEMS: V2ContributorsContributorIdCollectionsIdItems,
        PathValues.V2_CV_IMAGES: V2CvImages,
        PathValues.V2_CV_KEYWORDS: V2CvKeywords,
        PathValues.V2_CV_SIMILAR_IMAGES: V2CvSimilarImages,
        PathValues.V2_CV_SIMILAR_VIDEOS: V2CvSimilarVideos,
        PathValues.V2_EDITORIAL_CATEGORIES: V2EditorialCategories,
        PathValues.V2_EDITORIAL_IMAGES_CATEGORIES: V2EditorialImagesCategories,
        PathValues.V2_EDITORIAL_IMAGES_LICENSES: V2EditorialImagesLicenses,
        PathValues.V2_EDITORIAL_IMAGES_LIVEFEEDS: V2EditorialImagesLivefeeds,
        PathValues.V2_EDITORIAL_IMAGES_LIVEFEEDS_ID: V2EditorialImagesLivefeedsId,
        PathValues.V2_EDITORIAL_IMAGES_LIVEFEEDS_ID_ITEMS: V2EditorialImagesLivefeedsIdItems,
        PathValues.V2_EDITORIAL_IMAGES_SEARCH: V2EditorialImagesSearch,
        PathValues.V2_EDITORIAL_IMAGES_UPDATED: V2EditorialImagesUpdated,
        PathValues.V2_EDITORIAL_IMAGES_ID: V2EditorialImagesId,
        PathValues.V2_EDITORIAL_LICENSES: V2EditorialLicenses,
        PathValues.V2_EDITORIAL_LIVEFEEDS: V2EditorialLivefeeds,
        PathValues.V2_EDITORIAL_LIVEFEEDS_ID: V2EditorialLivefeedsId,
        PathValues.V2_EDITORIAL_LIVEFEEDS_ID_ITEMS: V2EditorialLivefeedsIdItems,
        PathValues.V2_EDITORIAL_SEARCH: V2EditorialSearch,
        PathValues.V2_EDITORIAL_UPDATED: V2EditorialUpdated,
        PathValues.V2_EDITORIAL_VIDEOS_CATEGORIES: V2EditorialVideosCategories,
        PathValues.V2_EDITORIAL_VIDEOS_LICENSES: V2EditorialVideosLicenses,
        PathValues.V2_EDITORIAL_VIDEOS_SEARCH: V2EditorialVideosSearch,
        PathValues.V2_EDITORIAL_VIDEOS_ID: V2EditorialVideosId,
        PathValues.V2_EDITORIAL_ID: V2EditorialId,
        PathValues.V2_IMAGES: V2Images,
        PathValues.V2_IMAGES_CATEGORIES: V2ImagesCategories,
        PathValues.V2_IMAGES_COLLECTIONS: V2ImagesCollections,
        PathValues.V2_IMAGES_COLLECTIONS_FEATURED: V2ImagesCollectionsFeatured,
        PathValues.V2_IMAGES_COLLECTIONS_FEATURED_ID: V2ImagesCollectionsFeaturedId,
        PathValues.V2_IMAGES_COLLECTIONS_FEATURED_ID_ITEMS: V2ImagesCollectionsFeaturedIdItems,
        PathValues.V2_IMAGES_COLLECTIONS_ID: V2ImagesCollectionsId,
        PathValues.V2_IMAGES_COLLECTIONS_ID_ITEMS: V2ImagesCollectionsIdItems,
        PathValues.V2_IMAGES_LICENSES: V2ImagesLicenses,
        PathValues.V2_IMAGES_LICENSES_ID_DOWNLOADS: V2ImagesLicensesIdDownloads,
        PathValues.V2_IMAGES_RECOMMENDATIONS: V2ImagesRecommendations,
        PathValues.V2_IMAGES_SEARCH: V2ImagesSearch,
        PathValues.V2_IMAGES_SEARCH_SUGGESTIONS: V2ImagesSearchSuggestions,
        PathValues.V2_IMAGES_UPDATED: V2ImagesUpdated,
        PathValues.V2_IMAGES_ID: V2ImagesId,
        PathValues.V2_IMAGES_ID_SIMILAR: V2ImagesIdSimilar,
        PathValues.V2_OAUTH_ACCESS_TOKEN: V2OauthAccessToken,
        PathValues.V2_OAUTH_AUTHORIZE: V2OauthAuthorize,
        PathValues.V2_SFX: V2Sfx,
        PathValues.V2_SFX_LICENSES: V2SfxLicenses,
        PathValues.V2_SFX_LICENSES_ID_DOWNLOADS: V2SfxLicensesIdDownloads,
        PathValues.V2_SFX_SEARCH: V2SfxSearch,
        PathValues.V2_SFX_ID: V2SfxId,
        PathValues.V2_TEST: V2Test,
        PathValues.V2_TEST_VALIDATE: V2TestValidate,
        PathValues.V2_USER: V2User,
        PathValues.V2_USER_ACCESS_TOKEN: V2UserAccessToken,
        PathValues.V2_USER_SUBSCRIPTIONS: V2UserSubscriptions,
        PathValues.V2_VIDEOS: V2Videos,
        PathValues.V2_VIDEOS_CATEGORIES: V2VideosCategories,
        PathValues.V2_VIDEOS_COLLECTIONS: V2VideosCollections,
        PathValues.V2_VIDEOS_COLLECTIONS_FEATURED: V2VideosCollectionsFeatured,
        PathValues.V2_VIDEOS_COLLECTIONS_FEATURED_ID: V2VideosCollectionsFeaturedId,
        PathValues.V2_VIDEOS_COLLECTIONS_FEATURED_ID_ITEMS: V2VideosCollectionsFeaturedIdItems,
        PathValues.V2_VIDEOS_COLLECTIONS_ID: V2VideosCollectionsId,
        PathValues.V2_VIDEOS_COLLECTIONS_ID_ITEMS: V2VideosCollectionsIdItems,
        PathValues.V2_VIDEOS_LICENSES: V2VideosLicenses,
        PathValues.V2_VIDEOS_LICENSES_ID_DOWNLOADS: V2VideosLicensesIdDownloads,
        PathValues.V2_VIDEOS_SEARCH: V2VideosSearch,
        PathValues.V2_VIDEOS_SEARCH_SUGGESTIONS: V2VideosSearchSuggestions,
        PathValues.V2_VIDEOS_UPDATED: V2VideosUpdated,
        PathValues.V2_VIDEOS_ID: V2VideosId,
        PathValues.V2_VIDEOS_ID_SIMILAR: V2VideosIdSimilar,
    }
)
