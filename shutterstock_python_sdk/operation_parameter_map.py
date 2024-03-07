operation_parameter_map = {
    '/v2/audio/collections/{id}/items-POST': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v2/audio/collections-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/v2/audio/collections/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v2/audio/collections/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'share_code'
            },
        ]
    },
    '/v2/audio/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'view'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/audio/licenses-POST': {
        'parameters': [
            {
                'name': 'audio'
            },
            {
                'name': 'license'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/audio/licenses-GET': {
        'parameters': [
            {
                'name': 'audio_id'
            },
            {
                'name': 'license'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'username'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'download_availability'
            },
            {
                'name': 'team_history'
            },
        ]
    },
    '/v2/audio/collections/{id}/items-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'share_code'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v2/audio/collections-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'embed'
            },
        ]
    },
    '/v2/audio/genres-GET': {
        'parameters': [
            {
                'name': 'language'
            },
        ]
    },
    '/v2/audio/instruments-GET': {
        'parameters': [
            {
                'name': 'language'
            },
        ]
    },
    '/v2/audio/moods-GET': {
        'parameters': [
            {
                'name': 'language'
            },
        ]
    },
    '/v2/audio-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'view'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/audio/licenses/{id}/downloads-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v2/audio/collections/{id}/items-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'item_id'
            },
        ]
    },
    '/v2/audio/search-GET': {
        'parameters': [
            {
                'name': 'artists'
            },
            {
                'name': 'bpm'
            },
            {
                'name': 'bpm_from'
            },
            {
                'name': 'bpm_to'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'duration_from'
            },
            {
                'name': 'duration_to'
            },
            {
                'name': 'genre'
            },
            {
                'name': 'is_instrumental'
            },
            {
                'name': 'instruments'
            },
            {
                'name': 'moods'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'sort_order'
            },
            {
                'name': 'vocal_description'
            },
            {
                'name': 'view'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'library'
            },
            {
                'name': 'language'
            },
        ]
    },
    '/v2/audio/collections/{id}-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v2/catalog/collections/{collection_id}/items-POST': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'collection_id'
            },
        ]
    },
    '/v2/catalog/collections-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'items'
            },
            {
                'name': 'visibility'
            },
        ]
    },
    '/v2/catalog/collections/{collection_id}-DELETE': {
        'parameters': [
            {
                'name': 'collection_id'
            },
        ]
    },
    '/v2/catalog/collections-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'shared'
            },
        ]
    },
    '/v2/catalog/collections/{collection_id}/items-DELETE': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'collection_id'
            },
        ]
    },
    '/v2/catalog/search-GET': {
        'parameters': [
            {
                'name': 'sort'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'collection_id'
            },
            {
                'name': 'asset_type'
            },
        ]
    },
    '/v2/catalog/collections/{collection_id}-PATCH': {
        'parameters': [
            {
                'name': 'collection_id'
            },
            {
                'name': 'cover_asset'
            },
            {
                'name': 'name'
            },
            {
                'name': 'visibility'
            },
        ]
    },
    '/v2/cv/similar/images-GET': {
        'parameters': [
            {
                'name': 'asset_id'
            },
            {
                'name': 'license'
            },
            {
                'name': 'safe'
            },
            {
                'name': 'language'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'view'
            },
        ]
    },
    '/v2/cv/similar/videos-GET': {
        'parameters': [
            {
                'name': 'asset_id'
            },
            {
                'name': 'license'
            },
            {
                'name': 'safe'
            },
            {
                'name': 'language'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'view'
            },
        ]
    },
    '/v2/cv/keywords-GET': {
        'parameters': [
            {
                'name': 'asset_id'
            },
        ]
    },
    '/v2/cv/images-POST': {
        'parameters': [
            {
                'name': 'base64_image'
            },
        ]
    },
    '/v2/images-POST': {
        'parameters': [
            {
                'name': 'base64_image'
            },
        ]
    },
    '/v2/contributors/{contributor_id}/collections/{id}-GET': {
        'parameters': [
            {
                'name': 'contributor_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v2/contributors/{contributor_id}/collections/{id}/items-GET': {
        'parameters': [
            {
                'name': 'contributor_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v2/contributors/{contributor_id}-GET': {
        'parameters': [
            {
                'name': 'contributor_id'
            },
        ]
    },
    '/v2/contributors-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v2/contributors/{contributor_id}/collections-GET': {
        'parameters': [
            {
                'name': 'contributor_id'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v2/ai/audio/renders-POST': {
        'parameters': [
            {
                'name': 'audio_renders'
            },
        ]
    },
    '/v2/ai/audio/renders-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v2/ai/audio/descriptors-GET': {
        'parameters': [
            {
                'name': 'render_speed_over'
            },
            {
                'name': 'band_id'
            },
            {
                'name': 'band_name'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'id'
            },
            {
                'name': 'instrument_name'
            },
            {
                'name': 'instrument_id'
            },
            {
                'name': 'tempo'
            },
            {
                'name': 'tempo_to'
            },
            {
                'name': 'tempo_from'
            },
            {
                'name': 'name'
            },
            {
                'name': 'tag'
            },
        ]
    },
    '/v2/ai/audio/instruments-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'page'
            },
            {
                'name': 'name'
            },
            {
                'name': 'tag'
            },
        ]
    },
    '/v2/editorial/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/editorial/images/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/v2/editorial/images/livefeeds/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/v2/editorial/images/livefeeds/{id}/items-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/v2/editorial/livefeeds/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/v2/editorial/livefeeds/{id}/items-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/v2/editorial/livefeeds-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/v2/editorial/images/licenses-POST': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'editorial'
            },
        ]
    },
    '/v2/editorial/licenses-POST': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'editorial'
            },
        ]
    },
    '/v2/editorial/categories-GET': {
        'parameters': [
        ]
    },
    '/v2/editorial/images/categories-GET': {
        'parameters': [
        ]
    },
    '/v2/editorial/images/licenses-GET': {
        'parameters': [
            {
                'name': 'image_id'
            },
            {
                'name': 'license'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'username'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'download_availability'
            },
            {
                'name': 'team_history'
            },
        ]
    },
    '/v2/editorial/images/livefeeds-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/v2/editorial/images/updated-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'date_updated_start'
            },
            {
                'name': 'date_updated_end'
            },
            {
                'name': 'country'
            },
            {
                'name': 'date_taken_start'
            },
            {
                'name': 'date_taken_end'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'supplier_code'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/v2/editorial/updated-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'date_updated_start'
            },
            {
                'name': 'date_updated_end'
            },
            {
                'name': 'country'
            },
            {
                'name': 'date_taken_start'
            },
            {
                'name': 'date_taken_end'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'supplier_code'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/v2/editorial/images/search-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'category'
            },
            {
                'name': 'supplier_code'
            },
            {
                'name': 'date_start'
            },
            {
                'name': 'date_end'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/v2/editorial/search-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'category'
            },
            {
                'name': 'supplier_code'
            },
            {
                'name': 'date_start'
            },
            {
                'name': 'date_end'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/v2/editorial/videos/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/editorial/videos/licenses-POST': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'editorial'
            },
        ]
    },
    '/v2/editorial/videos/categories-GET': {
        'parameters': [
        ]
    },
    '/v2/editorial/videos/licenses-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'license'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'username'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'download_availability'
            },
            {
                'name': 'team_history'
            },
        ]
    },
    '/v2/editorial/videos/search-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'category'
            },
            {
                'name': 'supplier_code'
            },
            {
                'name': 'date_start'
            },
            {
                'name': 'date_end'
            },
            {
                'name': 'resolution'
            },
            {
                'name': 'fps'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/v2/images/collections/{id}/items-POST': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v2/images/collections-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/v2/images/collections/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v2/images/search/suggestions-POST': {
        'parameters': [
            {
                'name': 'text'
            },
        ]
    },
    '/v2/images/collections/featured/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'asset_hint'
            },
        ]
    },
    '/v2/images/collections/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'share_code'
            },
        ]
    },
    '/v2/images/collections/featured/{id}/items-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/v2/images/collections/{id}/items-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'share_code'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v2/images/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'language'
            },
            {
                'name': 'view'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/images/search/suggestions-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/images/licenses-POST': {
        'parameters': [
            {
                'name': 'images'
            },
            {
                'name': 'subscription_id'
            },
            {
                'name': 'format'
            },
            {
                'name': 'size'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/images/categories-GET': {
        'parameters': [
            {
                'name': 'language'
            },
        ]
    },
    '/v2/images/collections-GET': {
        'parameters': [
            {
                'name': 'embed'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/v2/images/collections/featured-GET': {
        'parameters': [
            {
                'name': 'embed'
            },
            {
                'name': 'type'
            },
            {
                'name': 'asset_hint'
            },
        ]
    },
    '/v2/images-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'view'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/images/licenses-GET': {
        'parameters': [
            {
                'name': 'image_id'
            },
            {
                'name': 'license'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'username'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'download_availability'
            },
            {
                'name': 'team_history'
            },
        ]
    },
    '/v2/images/recommendations-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_items'
            },
            {
                'name': 'safe'
            },
        ]
    },
    '/v2/images/{id}/similar-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'language'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'view'
            },
        ]
    },
    '/v2/images/updated-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'interval'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v2/images/licenses/{id}/downloads-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'auth_cookie'
            },
            {
                'name': 'show_modal'
            },
            {
                'name': 'size'
            },
            {
                'name': 'verification_code'
            },
        ]
    },
    '/v2/images/collections/{id}/items-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'item_id'
            },
        ]
    },
    '/v2/images/collections/{id}-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v2/bulk_search/images-POST': {
        'parameters': [
            {
                'name': 'added_date'
            },
            {
                'name': 'added_date_start'
            },
            {
                'name': 'aspect_ratio_min'
            },
            {
                'name': 'aspect_ratio_max'
            },
            {
                'name': 'aspect_ratio'
            },
            {
                'name': 'added_date_end'
            },
            {
                'name': 'category'
            },
            {
                'name': 'color'
            },
            {
                'name': 'contributor'
            },
            {
                'name': 'contributor_country'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'height'
            },
            {
                'name': 'height_from'
            },
            {
                'name': 'height_to'
            },
            {
                'name': 'image_type'
            },
            {
                'name': 'keyword_safe_search'
            },
            {
                'name': 'language'
            },
            {
                'name': 'license'
            },
            {
                'name': 'model'
            },
            {
                'name': 'orientation'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'people_model_released'
            },
            {
                'name': 'people_age'
            },
            {
                'name': 'people_ethnicity'
            },
            {
                'name': 'people_gender'
            },
            {
                'name': 'people_number'
            },
            {
                'name': 'region'
            },
            {
                'name': 'safe'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'spellcheck_query'
            },
            {
                'name': 'view'
            },
            {
                'name': 'width'
            },
            {
                'name': 'width_from'
            },
            {
                'name': 'width_to'
            },
        ]
    },
    '/v2/images/search-GET': {
        'parameters': [
            {
                'name': 'added_date'
            },
            {
                'name': 'added_date_start'
            },
            {
                'name': 'aspect_ratio_min'
            },
            {
                'name': 'aspect_ratio_max'
            },
            {
                'name': 'aspect_ratio'
            },
            {
                'name': 'ai_search'
            },
            {
                'name': 'ai_labels_limit'
            },
            {
                'name': 'ai_industry'
            },
            {
                'name': 'ai_objective'
            },
            {
                'name': 'added_date_end'
            },
            {
                'name': 'category'
            },
            {
                'name': 'color'
            },
            {
                'name': 'contributor'
            },
            {
                'name': 'contributor_country'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'height'
            },
            {
                'name': 'height_from'
            },
            {
                'name': 'height_to'
            },
            {
                'name': 'image_type'
            },
            {
                'name': 'keyword_safe_search'
            },
            {
                'name': 'language'
            },
            {
                'name': 'license'
            },
            {
                'name': 'model'
            },
            {
                'name': 'orientation'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'people_model_released'
            },
            {
                'name': 'people_age'
            },
            {
                'name': 'people_ethnicity'
            },
            {
                'name': 'people_gender'
            },
            {
                'name': 'people_number'
            },
            {
                'name': 'query'
            },
            {
                'name': 'region'
            },
            {
                'name': 'safe'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'spellcheck_query'
            },
            {
                'name': 'view'
            },
            {
                'name': 'width'
            },
            {
                'name': 'width_from'
            },
            {
                'name': 'width_to'
            },
        ]
    },
    '/v2/oauth/authorize-GET': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'response_type'
            },
            {
                'name': 'state'
            },
            {
                'name': 'realm'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/v2/oauth/access_token-POST': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'code'
            },
            {
                'name': 'expires'
            },
            {
                'name': 'realm'
            },
            {
                'name': 'refresh_token'
            },
        ]
    },
    '/v2/sfx/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'language'
            },
            {
                'name': 'view'
            },
            {
                'name': 'library'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/sfx/licenses-POST': {
        'parameters': [
            {
                'name': 'sound_effects'
            },
        ]
    },
    '/v2/sfx-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'view'
            },
            {
                'name': 'language'
            },
            {
                'name': 'library'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/sfx/licenses-GET': {
        'parameters': [
            {
                'name': 'sfx_id'
            },
            {
                'name': 'license'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'username'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'license_id'
            },
            {
                'name': 'download_availability'
            },
            {
                'name': 'team_history'
            },
        ]
    },
    '/v2/sfx/licenses/{id}/downloads-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v2/sfx/search-GET': {
        'parameters': [
            {
                'name': 'added_date'
            },
            {
                'name': 'added_date_start'
            },
            {
                'name': 'added_date_end'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'duration_from'
            },
            {
                'name': 'duration_to'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'safe'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'view'
            },
            {
                'name': 'language'
            },
        ]
    },
    '/v2/test-GET': {
        'parameters': [
            {
                'name': 'text'
            },
        ]
    },
    '/v2/test/validate-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'user-agent'
            },
        ]
    },
    '/v2/user/access_token-GET': {
        'parameters': [
        ]
    },
    '/v2/user-GET': {
        'parameters': [
        ]
    },
    '/v2/user/subscriptions-GET': {
        'parameters': [
        ]
    },
    '/v2/videos/collections/{id}/items-POST': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v2/videos/collections/featured/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'embed'
            },
        ]
    },
    '/v2/videos/collections/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'share_code'
            },
        ]
    },
    '/v2/videos/collections-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/v2/videos/collections/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v2/videos/{id}/similar-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'language'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'view'
            },
        ]
    },
    '/v2/videos/collections/{id}/items-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'share_code'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v2/videos/collections/featured/{id}/items-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/v2/videos/licenses-POST': {
        'parameters': [
            {
                'name': 'videos'
            },
            {
                'name': 'subscription_id'
            },
            {
                'name': 'size'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/videos/categories-GET': {
        'parameters': [
            {
                'name': 'language'
            },
        ]
    },
    '/v2/videos/collections-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'embed'
            },
        ]
    },
    '/v2/videos/collections/featured-GET': {
        'parameters': [
            {
                'name': 'embed'
            },
        ]
    },
    '/v2/videos/licenses-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'license'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'username'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'download_availability'
            },
            {
                'name': 'team_history'
            },
        ]
    },
    '/v2/videos/updated-GET': {
        'parameters': [
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'interval'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v2/videos-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'view'
            },
            {
                'name': 'search_id'
            },
        ]
    },
    '/v2/videos/licenses/{id}/downloads-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'auth_cookie'
            },
            {
                'name': 'show_modal'
            },
            {
                'name': 'size'
            },
            {
                'name': 'verification_code'
            },
        ]
    },
    '/v2/videos/collections/{id}/items-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'item_id'
            },
        ]
    },
    '/v2/videos/search/suggestions-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/videos/search-GET': {
        'parameters': [
            {
                'name': 'added_date'
            },
            {
                'name': 'added_date_start'
            },
            {
                'name': 'added_date_end'
            },
            {
                'name': 'aspect_ratio'
            },
            {
                'name': 'category'
            },
            {
                'name': 'contributor'
            },
            {
                'name': 'contributor_country'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'duration_from'
            },
            {
                'name': 'duration_to'
            },
            {
                'name': 'fps'
            },
            {
                'name': 'fps_from'
            },
            {
                'name': 'fps_to'
            },
            {
                'name': 'keyword_safe_search'
            },
            {
                'name': 'language'
            },
            {
                'name': 'license'
            },
            {
                'name': 'model'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'people_age'
            },
            {
                'name': 'people_ethnicity'
            },
            {
                'name': 'people_gender'
            },
            {
                'name': 'people_number'
            },
            {
                'name': 'people_model_released'
            },
            {
                'name': 'query'
            },
            {
                'name': 'resolution'
            },
            {
                'name': 'safe'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'view'
            },
        ]
    },
    '/v2/videos/collections/{id}-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/v2/videos/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'language'
            },
            {
                'name': 'view'
            },
            {
                'name': 'search_id'
            },
        ]
    },
};