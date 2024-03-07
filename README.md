<div align="center">

[![Visit Shutterstock](./header.png)](https://developers.shutterstock.com)

# Shutterstock<a id="shutterstock"></a>

The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`shutterstock.audio.add_tracks_to_collection`](#shutterstockaudioadd_tracks_to_collection)
  * [`shutterstock.audio.create_collections`](#shutterstockaudiocreate_collections)
  * [`shutterstock.audio.delete_collection`](#shutterstockaudiodelete_collection)
  * [`shutterstock.audio.get_collection_details`](#shutterstockaudioget_collection_details)
  * [`shutterstock.audio.get_track_details`](#shutterstockaudioget_track_details)
  * [`shutterstock.audio.license_tracks`](#shutterstockaudiolicense_tracks)
  * [`shutterstock.audio.list_audio_licenses`](#shutterstockaudiolist_audio_licenses)
  * [`shutterstock.audio.list_collection_items`](#shutterstockaudiolist_collection_items)
  * [`shutterstock.audio.list_collections`](#shutterstockaudiolist_collections)
  * [`shutterstock.audio.list_genres`](#shutterstockaudiolist_genres)
  * [`shutterstock.audio.list_instruments`](#shutterstockaudiolist_instruments)
  * [`shutterstock.audio.list_moods`](#shutterstockaudiolist_moods)
  * [`shutterstock.audio.list_tracks`](#shutterstockaudiolist_tracks)
  * [`shutterstock.audio.redownload_tracks`](#shutterstockaudioredownload_tracks)
  * [`shutterstock.audio.remove_tracks_from_collection`](#shutterstockaudioremove_tracks_from_collection)
  * [`shutterstock.audio.search_tracks`](#shutterstockaudiosearch_tracks)
  * [`shutterstock.audio.set_collection_name`](#shutterstockaudioset_collection_name)
  * [`shutterstock.catalog.add_to_collection_items`](#shutterstockcatalogadd_to_collection_items)
  * [`shutterstock.catalog.create_collection`](#shutterstockcatalogcreate_collection)
  * [`shutterstock.catalog.delete_collection`](#shutterstockcatalogdelete_collection)
  * [`shutterstock.catalog.list_collections`](#shutterstockcataloglist_collections)
  * [`shutterstock.catalog.remove_items_from_collection`](#shutterstockcatalogremove_items_from_collection)
  * [`shutterstock.catalog.search_assets`](#shutterstockcatalogsearch_assets)
  * [`shutterstock.catalog.update_collection_metadata`](#shutterstockcatalogupdate_collection_metadata)
  * [`shutterstock.computer_vision.list_similar_images`](#shutterstockcomputer_visionlist_similar_images)
  * [`shutterstock.computer_vision.list_similar_videos`](#shutterstockcomputer_visionlist_similar_videos)
  * [`shutterstock.computer_vision.list_suggested_keywords`](#shutterstockcomputer_visionlist_suggested_keywords)
  * [`shutterstock.computer_vision.upload_image`](#shutterstockcomputer_visionupload_image)
  * [`shutterstock.computer_vision.upload_image_ephemeral`](#shutterstockcomputer_visionupload_image_ephemeral)
  * [`shutterstock.contributors.get_collection_details`](#shutterstockcontributorsget_collection_details)
  * [`shutterstock.contributors.get_collection_items`](#shutterstockcontributorsget_collection_items)
  * [`shutterstock.contributors.get_details`](#shutterstockcontributorsget_details)
  * [`shutterstock.contributors.get_details_multiple`](#shutterstockcontributorsget_details_multiple)
  * [`shutterstock.contributors.list_collections`](#shutterstockcontributorslist_collections)
  * [`shutterstock.custom_music.create_rendered_audio`](#shutterstockcustom_musiccreate_rendered_audio)
  * [`shutterstock.custom_music.get_audio_renders_details`](#shutterstockcustom_musicget_audio_renders_details)
  * [`shutterstock.custom_music.list_audio_descriptors`](#shutterstockcustom_musiclist_audio_descriptors)
  * [`shutterstock.custom_music.list_computer_audio_instruments`](#shutterstockcustom_musiclist_computer_audio_instruments)
  * [`shutterstock.editorial_images.get_details`](#shutterstockeditorial_imagesget_details)
  * [`shutterstock.editorial_images.get_image_details`](#shutterstockeditorial_imagesget_image_details)
  * [`shutterstock.editorial_images.get_livefeed_images`](#shutterstockeditorial_imagesget_livefeed_images)
  * [`shutterstock.editorial_images.get_livefeed_items`](#shutterstockeditorial_imagesget_livefeed_items)
  * [`shutterstock.editorial_images.get_livefeed_items_0`](#shutterstockeditorial_imagesget_livefeed_items_0)
  * [`shutterstock.editorial_images.get_livefeed_items_1`](#shutterstockeditorial_imagesget_livefeed_items_1)
  * [`shutterstock.editorial_images.get_livefeed_list`](#shutterstockeditorial_imagesget_livefeed_list)
  * [`shutterstock.editorial_images.license_content`](#shutterstockeditorial_imageslicense_content)
  * [`shutterstock.editorial_images.license_content_0`](#shutterstockeditorial_imageslicense_content_0)
  * [`shutterstock.editorial_images.list_categories`](#shutterstockeditorial_imageslist_categories)
  * [`shutterstock.editorial_images.list_categories_0`](#shutterstockeditorial_imageslist_categories_0)
  * [`shutterstock.editorial_images.list_licenses`](#shutterstockeditorial_imageslist_licenses)
  * [`shutterstock.editorial_images.list_livefeed_images`](#shutterstockeditorial_imageslist_livefeed_images)
  * [`shutterstock.editorial_images.list_updated_content`](#shutterstockeditorial_imageslist_updated_content)
  * [`shutterstock.editorial_images.list_updated_content_0`](#shutterstockeditorial_imageslist_updated_content_0)
  * [`shutterstock.editorial_images.search`](#shutterstockeditorial_imagessearch)
  * [`shutterstock.editorial_images.search_content`](#shutterstockeditorial_imagessearch_content)
  * [`shutterstock.editorial_video.get_content_details`](#shutterstockeditorial_videoget_content_details)
  * [`shutterstock.editorial_video.license_videos`](#shutterstockeditorial_videolicense_videos)
  * [`shutterstock.editorial_video.list_video_categories`](#shutterstockeditorial_videolist_video_categories)
  * [`shutterstock.editorial_video.list_video_licenses`](#shutterstockeditorial_videolist_video_licenses)
  * [`shutterstock.editorial_video.search_video_content`](#shutterstockeditorial_videosearch_video_content)
  * [`shutterstock.images.add_to_collection_items`](#shutterstockimagesadd_to_collection_items)
  * [`shutterstock.images.create_collection`](#shutterstockimagescreate_collection)
  * [`shutterstock.images.delete_collection`](#shutterstockimagesdelete_collection)
  * [`shutterstock.images.extract_keywords_from_text`](#shutterstockimagesextract_keywords_from_text)
  * [`shutterstock.images.featured_collection_details`](#shutterstockimagesfeatured_collection_details)
  * [`shutterstock.images.get_collection_details`](#shutterstockimagesget_collection_details)
  * [`shutterstock.images.get_collection_items`](#shutterstockimagesget_collection_items)
  * [`shutterstock.images.get_collection_items_0`](#shutterstockimagesget_collection_items_0)
  * [`shutterstock.images.get_details`](#shutterstockimagesget_details)
  * [`shutterstock.images.get_search_suggestions`](#shutterstockimagesget_search_suggestions)
  * [`shutterstock.images.license_images_for_multiple`](#shutterstockimageslicense_images_for_multiple)
  * [`shutterstock.images.list_categories`](#shutterstockimageslist_categories)
  * [`shutterstock.images.list_collections`](#shutterstockimageslist_collections)
  * [`shutterstock.images.list_featured_collections`](#shutterstockimageslist_featured_collections)
  * [`shutterstock.images.list_info`](#shutterstockimageslist_info)
  * [`shutterstock.images.list_licenses`](#shutterstockimageslist_licenses)
  * [`shutterstock.images.list_recommended_images`](#shutterstockimageslist_recommended_images)
  * [`shutterstock.images.list_similar_images`](#shutterstockimageslist_similar_images)
  * [`shutterstock.images.list_updated_content`](#shutterstockimageslist_updated_content)
  * [`shutterstock.images.redownload_license`](#shutterstockimagesredownload_license)
  * [`shutterstock.images.remove_from_collection`](#shutterstockimagesremove_from_collection)
  * [`shutterstock.images.rename_collection`](#shutterstockimagesrename_collection)
  * [`shutterstock.images.run_multiple_searches`](#shutterstockimagesrun_multiple_searches)
  * [`shutterstock.images.search_images`](#shutterstockimagessearch_images)
  * [`shutterstock.oauth.authorize_applications`](#shutterstockoauthauthorize_applications)
  * [`shutterstock.oauth.get_user_access_token`](#shutterstockoauthget_user_access_token)
  * [`shutterstock.sound_effects.get_details`](#shutterstocksound_effectsget_details)
  * [`shutterstock.sound_effects.license_assets`](#shutterstocksound_effectslicense_assets)
  * [`shutterstock.sound_effects.list_details`](#shutterstocksound_effectslist_details)
  * [`shutterstock.sound_effects.list_licenses`](#shutterstocksound_effectslist_licenses)
  * [`shutterstock.sound_effects.redownload_licenses`](#shutterstocksound_effectsredownload_licenses)
  * [`shutterstock.sound_effects.search_sound_effects`](#shutterstocksound_effectssearch_sound_effects)
  * [`shutterstock.test.echo_text`](#shutterstocktestecho_text)
  * [`shutterstock.test.input_validation`](#shutterstocktestinput_validation)
  * [`shutterstock.users.get_access_token_details`](#shutterstockusersget_access_token_details)
  * [`shutterstock.users.get_user_details`](#shutterstockusersget_user_details)
  * [`shutterstock.users.list_subscriptions`](#shutterstockuserslist_subscriptions)
  * [`shutterstock.videos.add_to_collection_items`](#shutterstockvideosadd_to_collection_items)
  * [`shutterstock.videos.collection_details_get`](#shutterstockvideoscollection_details_get)
  * [`shutterstock.videos.collection_details_get_0`](#shutterstockvideoscollection_details_get_0)
  * [`shutterstock.videos.create_video_collections`](#shutterstockvideoscreate_video_collections)
  * [`shutterstock.videos.delete_collection`](#shutterstockvideosdelete_collection)
  * [`shutterstock.videos.find_similar`](#shutterstockvideosfind_similar)
  * [`shutterstock.videos.get_collection_items`](#shutterstockvideosget_collection_items)
  * [`shutterstock.videos.get_featured_collection_items`](#shutterstockvideosget_featured_collection_items)
  * [`shutterstock.videos.license_videos`](#shutterstockvideoslicense_videos)
  * [`shutterstock.videos.list_categories`](#shutterstockvideoslist_categories)
  * [`shutterstock.videos.list_collections`](#shutterstockvideoslist_collections)
  * [`shutterstock.videos.list_featured_video_collections`](#shutterstockvideoslist_featured_video_collections)
  * [`shutterstock.videos.list_licenses`](#shutterstockvideoslist_licenses)
  * [`shutterstock.videos.list_updated_videos`](#shutterstockvideoslist_updated_videos)
  * [`shutterstock.videos.list_video`](#shutterstockvideoslist_video)
  * [`shutterstock.videos.redownload_downloads`](#shutterstockvideosredownload_downloads)
  * [`shutterstock.videos.remove_from_collection`](#shutterstockvideosremove_from_collection)
  * [`shutterstock.videos.search_suggestions`](#shutterstockvideossearch_suggestions)
  * [`shutterstock.videos.search_video`](#shutterstockvideossearch_video)
  * [`shutterstock.videos.set_new_name`](#shutterstockvideosset_new_name)
  * [`shutterstock.videos.video_details`](#shutterstockvideosvideo_details)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Shutterstock&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from shutterstock_python_sdk import Shutterstock, ApiException

shutterstock = Shutterstock(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Add audio tracks to collections
    shutterstock.audio.add_tracks_to_collection(
        items=[
            {
                "added_time": "2020-05-29T17:10:22Z",
                "id": "297886754",
                "media_type": "image",
            }
        ],
        id="48433115",
    )
except ApiException as e:
    print("Exception when calling AudioApi.add_tracks_to_collection: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from shutterstock_python_sdk import Shutterstock, ApiException

shutterstock = Shutterstock(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        # Add audio tracks to collections
        await shutterstock.audio.aadd_tracks_to_collection(
            items=[
                {
                    "added_time": "2020-05-29T17:10:22Z",
                    "id": "297886754",
                    "media_type": "image",
                }
            ],
            id="48433115",
        )
    except ApiException as e:
        print("Exception when calling AudioApi.add_tracks_to_collection: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from shutterstock_python_sdk import Shutterstock, ApiException

shutterstock = Shutterstock(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Add audio tracks to collections
    add_tracks_to_collection_response = shutterstock.audio.raw.add_tracks_to_collection(
        items=[
            {
                "added_time": "2020-05-29T17:10:22Z",
                "id": "297886754",
                "media_type": "image",
            }
        ],
        id="48433115",
    )
    pprint(add_tracks_to_collection_response.headers)
    pprint(add_tracks_to_collection_response.status)
    pprint(add_tracks_to_collection_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AudioApi.add_tracks_to_collection: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `shutterstock.audio.add_tracks_to_collection`<a id="shutterstockaudioadd_tracks_to_collection"></a>

This endpoint adds one or more tracks to a collection by track IDs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.audio.add_tracks_to_collection(
    items=[
        {
            "added_time": "2020-05-29T17:10:22Z",
            "id": "297886754",
            "media_type": "image",
        }
    ],
    id="48433115",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: List[`CollectionItem`]<a id="items-listcollectionitem"></a>

List of items

##### id: `str`<a id="id-str"></a>

Collection ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionItemRequest`](./shutterstock_python_sdk/type/collection_item_request.py)
List of items to add to collection

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/collections/{id}/items` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.create_collections`<a id="shutterstockaudiocreate_collections"></a>

This endpoint creates one or more collections (soundboxes). To add tracks, use `POST /v2/audio/collections/{id}/items`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_collections_response = shutterstock.audio.create_collections(
    name="Test Collection 19cf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the collection

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionCreateRequest`](./shutterstock_python_sdk/type/collection_create_request.py)
Collection metadata

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionCreateResponse`](./shutterstock_python_sdk/pydantic/collection_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/collections` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.delete_collection`<a id="shutterstockaudiodelete_collection"></a>

This endpoint deletes a collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.audio.delete_collection(
    id="48433111",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/collections/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.get_collection_details`<a id="shutterstockaudioget_collection_details"></a>

This endpoint gets more detailed information about a collection, including the number of items in it and when it was last updated. To get the tracks in collections, use `GET /v2/audio/collections/{id}/items`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_details_response = shutterstock.audio.get_collection_details(
    id="48433107",
    embed=["string_example"],
    share_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### embed: List[`str`]<a id="embed-liststr"></a>

Which sharing information to include in the response, such as a URL to the collection

##### share_code: `str`<a id="share_code-str"></a>

Code to retrieve a shared collection

#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./shutterstock_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/collections/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.get_track_details`<a id="shutterstockaudioget_track_details"></a>

This endpoint shows information about a track, including its genres, instruments, and other attributes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_track_details_response = shutterstock.audio.get_track_details(
    id=442583,
    view="full",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Audio track ID

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`Audio`](./shutterstock_python_sdk/pydantic/audio.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.license_tracks`<a id="shutterstockaudiolicense_tracks"></a>

This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
license_tracks_response = shutterstock.audio.license_tracks(
    audio=[
        {
            "audio_id": "123456789",
            "license": "audio_platform",
            "search_id": "987654321",
        }
    ],
    license="audio_platform",
    search_id="p5S6QwRikdFJTHXwsoiqTg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audio: List[`LicenseAudio`]<a id="audio-listlicenseaudio"></a>

List of audio tracks to license

##### license: `str`<a id="license-str"></a>

License type

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that led to licensing this track

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LicenseAudioRequest`](./shutterstock_python_sdk/type/license_audio_request.py)
Tracks to license

#### 🔄 Return<a id="🔄-return"></a>

[`LicenseAudioResultDataList`](./shutterstock_python_sdk/pydantic/license_audio_result_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/licenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.list_audio_licenses`<a id="shutterstockaudiolist_audio_licenses"></a>

This endpoint lists existing licenses. You can filter the results according to the track ID to see if you have an existing license for a specific track.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_audio_licenses_response = shutterstock.audio.list_audio_licenses(
    audio_id="1",
    license="48433107",
    page=1,
    per_page=20,
    sort="newest",
    username="aUniqueUsername",
    start_date="2021-03-29T13:25:13.521Z",
    end_date="2021-03-29T13:25:13.521Z",
    download_availability="all",
    team_history=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audio_id: `str`<a id="audio_id-str"></a>

Show licenses for the specified track ID

##### license: `str`<a id="license-str"></a>

Restrict results by license. Prepending a `-` sign will exclude results by license

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort order

##### username: `str`<a id="username-str"></a>

Filter licenses by username of licensee

##### start_date: `datetime`<a id="start_date-datetime"></a>

Show licenses created on or after the specified date

##### end_date: `datetime`<a id="end_date-datetime"></a>

Show licenses created before the specified date

##### download_availability: `str`<a id="download_availability-str"></a>

Filter licenses by download availability

##### team_history: `bool`<a id="team_history-bool"></a>

Set to true to see license history for all members of your team.

#### 🔄 Return<a id="🔄-return"></a>

[`DownloadHistoryDataList`](./shutterstock_python_sdk/pydantic/download_history_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/licenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.list_collection_items`<a id="shutterstockaudiolist_collection_items"></a>

This endpoint lists the IDs of tracks in a collection and the date that each was added.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collection_items_response = shutterstock.audio.list_collection_items(
    id="126351027",
    page=1,
    per_page=100,
    share_code="string_example",
    sort="oldest",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### share_code: `str`<a id="share_code-str"></a>

Code to retrieve the contents of a shared collection

##### sort: `str`<a id="sort-str"></a>

Sort order

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionItemDataList`](./shutterstock_python_sdk/pydantic/collection_item_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/collections/{id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.list_collections`<a id="shutterstockaudiolist_collections"></a>

This endpoint lists your collections of audio tracks and their basic attributes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collections_response = shutterstock.audio.list_collections(
    page=1,
    per_page=100,
    embed=["share_code"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### embed: List[`str`]<a id="embed-liststr"></a>

Which sharing information to include in the response, such as a URL to the collection

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionDataList`](./shutterstock_python_sdk/pydantic/collection_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.list_genres`<a id="shutterstockaudiolist_genres"></a>

This endpoint returns a list of all audio genres.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_genres_response = shutterstock.audio.list_genres(
    language="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### language: `str`<a id="language-str"></a>

Which language the genres will be returned

#### 🔄 Return<a id="🔄-return"></a>

[`GenreList`](./shutterstock_python_sdk/pydantic/genre_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/genres` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.list_instruments`<a id="shutterstockaudiolist_instruments"></a>

This endpoint returns a list of all audio instruments.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_instruments_response = shutterstock.audio.list_instruments(
    language="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### language: `str`<a id="language-str"></a>

Which language the instruments will be returned in

#### 🔄 Return<a id="🔄-return"></a>

[`InstrumentList`](./shutterstock_python_sdk/pydantic/instrument_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/instruments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.list_moods`<a id="shutterstockaudiolist_moods"></a>

This endpoint returns a list of all audio moods.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_moods_response = shutterstock.audio.list_moods(
    language="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### language: `str`<a id="language-str"></a>

Which language the moods will be returned in

#### 🔄 Return<a id="🔄-return"></a>

[`MoodList`](./shutterstock_python_sdk/pydantic/mood_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/moods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.list_tracks`<a id="shutterstockaudiolist_tracks"></a>

This endpoint lists information about one or more audio tracks, including the description and publication date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tracks_response = shutterstock.audio.list_tracks(
    id=["442583", "434750"],
    view="full",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

One or more audio IDs

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`AudioDataList`](./shutterstock_python_sdk/pydantic/audio_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.redownload_tracks`<a id="shutterstockaudioredownload_tracks"></a>

This endpoint redownloads tracks that you have already received a license for. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
redownload_tracks_response = shutterstock.audio.redownload_tracks(
    id="e123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

License ID

#### 🔄 Return<a id="🔄-return"></a>

[`AudioUrl`](./shutterstock_python_sdk/pydantic/audio_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/licenses/{id}/downloads` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.remove_tracks_from_collection`<a id="shutterstockaudioremove_tracks_from_collection"></a>

This endpoint removes one or more tracks from a collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.audio.remove_tracks_from_collection(
    id="48433119",
    item_id=["76688182", "40005859"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### item_id: List[`str`]<a id="item_id-liststr"></a>

One or more item IDs to remove from the collection

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/collections/{id}/items` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.search_tracks`<a id="shutterstockaudiosearch_tracks"></a>

This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_tracks_response = shutterstock.audio.search_tracks(
    artists=["string_example"],
    bpm=1,
    bpm_from=80,
    bpm_to=120,
    duration=180,
    duration_from=30,
    duration_to=180,
    genre=["Classical", "Holiday"],
    is_instrumental=True,
    instruments=["Trumpet", "Percussion"],
    moods=["Confident", "Playful"],
    page=1,
    per_page=1,
    query="drum",
    sort="score",
    sort_order="desc",
    vocal_description="female",
    view="full",
    fields="string_example",
    library="premier",
    language="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### artists: List[`str`]<a id="artists-liststr"></a>

Show tracks with one of the specified artist names or IDs

##### bpm: `int`<a id="bpm-int"></a>

(Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute

##### bpm_from: `int`<a id="bpm_from-int"></a>

Show tracks with the specified beats per minute or faster

##### bpm_to: `int`<a id="bpm_to-int"></a>

Show tracks with the specified beats per minute or slower

##### duration: `int`<a id="duration-int"></a>

Show tracks with the specified duration in seconds

##### duration_from: `int`<a id="duration_from-int"></a>

Show tracks with the specified duration or longer in seconds

##### duration_to: `int`<a id="duration_to-int"></a>

Show tracks with the specified duration or shorter in seconds

##### genre: List[`str`]<a id="genre-liststr"></a>

Show tracks with each of the specified genres; to get the list of genres, use `GET /v2/audio/genres`

##### is_instrumental: `bool`<a id="is_instrumental-bool"></a>

Show instrumental music only

##### instruments: List[`str`]<a id="instruments-liststr"></a>

Show tracks with each of the specified instruments; to get the list of instruments, use `GET /v2/audio/instruments`

##### moods: List[`str`]<a id="moods-liststr"></a>

Show tracks with each of the specified moods; to get the list of moods, use `GET /v2/audio/moods`

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### query: `str`<a id="query-str"></a>

One or more search terms separated by spaces

##### sort: `str`<a id="sort-str"></a>

Sort by

##### sort_order: `str`<a id="sort_order-str"></a>

Sort order

##### vocal_description: `str`<a id="vocal_description-str"></a>

Show tracks with the specified vocal description (male, female)

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### fields: `str`<a id="fields-str"></a>

Fields to display in the response; see the documentation for the fields parameter in the overview section

##### library: `str`<a id="library-str"></a>

Which library to search

##### language: `str`<a id="language-str"></a>

Which language to search in

#### 🔄 Return<a id="🔄-return"></a>

[`AudioSearchResults`](./shutterstock_python_sdk/pydantic/audio_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.audio.set_collection_name`<a id="shutterstockaudioset_collection_name"></a>

This endpoint sets a new name for a collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.audio.set_collection_name(
    name="My collection with a new name",
    id="48433107",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The new name of the collection

##### id: `str`<a id="id-str"></a>

Collection ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionUpdateRequest`](./shutterstock_python_sdk/type/collection_update_request.py)
Collection changes

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/audio/collections/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.catalog.add_to_collection_items`<a id="shutterstockcatalogadd_to_collection_items"></a>

This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user's account's catalog.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_collection_items_response = shutterstock.catalog.add_to_collection_items(
    items=[
        {
            "asset": {
                "id": "1690105108X",
                "type": "image",
            },
        }
    ],
    collection_id="126351028",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: List[`CreateCatalogCollectionItem`]<a id="items-listcreatecatalogcollectionitem"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

The ID of the collection to add assets to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCatalogCollectionItems`](./shutterstock_python_sdk/type/create_catalog_collection_items.py)
Collection item attributes to add to collection

#### 🔄 Return<a id="🔄-return"></a>

[`CatalogCollection`](./shutterstock_python_sdk/pydantic/catalog_collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/catalog/collections/{collection_id}/items` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.catalog.create_collection`<a id="shutterstockcatalogcreate_collection"></a>

This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later, use `PATCH /v2/catalog/collections/{collection_id}/items`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_collection_response = shutterstock.catalog.create_collection(
    name="New Collection",
    items=[
        {
            "asset": {
                "id": "1690105108X",
                "type": "image",
            },
        }
    ],
    visibility="private",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### items: List[`CreateCatalogCollectionItem`]<a id="items-listcreatecatalogcollectionitem"></a>

##### visibility: `str`<a id="visibility-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCatalogCollection`](./shutterstock_python_sdk/type/create_catalog_collection.py)
Create a catalog collection and, optionally, add items.

#### 🔄 Return<a id="🔄-return"></a>

[`CatalogCollection`](./shutterstock_python_sdk/pydantic/catalog_collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/catalog/collections` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.catalog.delete_collection`<a id="shutterstockcatalogdelete_collection"></a>

This endpoint deletes a catalog collection. It does not remove the assets from the user's account's catalog.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.catalog.delete_collection(
    collection_id="126351028",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

The ID of the collection to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/catalog/collections/{collection_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.catalog.list_collections`<a id="shutterstockcataloglist_collections"></a>

This endpoint returns a list of catalog collections.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collections_response = shutterstock.catalog.list_collections(
    page=1,
    per_page=20,
    sort="newest",
    shared=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort by

##### shared: `bool`<a id="shared-bool"></a>

Set to true to omit collections that you own and return only collections  that are shared with you

#### 🔄 Return<a id="🔄-return"></a>

[`CatalogCollectionDataList`](./shutterstock_python_sdk/pydantic/catalog_collection_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/catalog/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.catalog.remove_items_from_collection`<a id="shutterstockcatalogremove_items_from_collection"></a>

This endpoint removes assets from a catalog collection. It does not remove the assets from the user's account's catalog.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_items_from_collection_response = (
    shutterstock.catalog.remove_items_from_collection(
        items=[
            {
                "id": "123X",
            }
        ],
        collection_id="126351028",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: List[`RemoveCatalogCollectionItem`]<a id="items-listremovecatalogcollectionitem"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

The ID of the collection to remove assets from

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RemoveCatalogCollectionItems`](./shutterstock_python_sdk/type/remove_catalog_collection_items.py)
Items to remove from the collection

#### 🔄 Return<a id="🔄-return"></a>

[`CatalogCollection`](./shutterstock_python_sdk/pydantic/catalog_collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/catalog/collections/{collection_id}/items` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.catalog.search_assets`<a id="shutterstockcatalogsearch_assets"></a>

This endpoint searches for assets in the account's catalog. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_assets_response = shutterstock.catalog.search_assets(
    sort="newest",
    page=1,
    per_page=50,
    query="dogs on the beach",
    collection_id=["123456", "456789", "13579"],
    asset_type=["image", "editorial-image"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sort by

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### query: `str`<a id="query-str"></a>

One or more search terms separated by spaces

##### collection_id: List[`str`]<a id="collection_id-liststr"></a>

Filter by collection id

##### asset_type: List[`str`]<a id="asset_type-liststr"></a>

Filter by asset type

#### 🔄 Return<a id="🔄-return"></a>

[`CatalogCollectionItemDataList`](./shutterstock_python_sdk/pydantic/catalog_collection_item_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/catalog/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.catalog.update_collection_metadata`<a id="shutterstockcatalogupdate_collection_metadata"></a>

This endpoint updates the metadata of a catalog collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_collection_metadata_response = shutterstock.catalog.update_collection_metadata(
    collection_id="126351028",
    cover_asset={
        "id": "123X",
    },
    name="My Collection",
    visibility="public",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

ID of collection that needs to be modified

##### cover_asset: [`UpdateCatalogCollectionCoverAsset`](./shutterstock_python_sdk/type/update_catalog_collection_cover_asset.py)<a id="cover_asset-updatecatalogcollectioncoverassetshutterstock_python_sdktypeupdate_catalog_collection_cover_assetpy"></a>


##### name: `str`<a id="name-str"></a>

##### visibility: `str`<a id="visibility-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCatalogCollection`](./shutterstock_python_sdk/type/update_catalog_collection.py)
Collections Metadata to update

#### 🔄 Return<a id="🔄-return"></a>

[`CatalogCollection`](./shutterstock_python_sdk/pydantic/catalog_collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/catalog/collections/{collection_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.computer_vision.list_similar_images`<a id="shutterstockcomputer_visionlist_similar_images"></a>

This endpoint returns images that are visually similar to an image that you specify or upload.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_similar_images_response = shutterstock.computer_vision.list_similar_images(
    asset_id="U6ba16262e3bc2db470b8e3cfa8aaab25",
    license=["commercial"],
    safe=True,
    language="es",
    page=1,
    per_page=20,
    view="minimal",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_id: `str`<a id="asset_id-str"></a>

The asset ID or upload ID to find similar images for

##### license: List[`str`]<a id="license-liststr"></a>

Show only images with the specified license

##### safe: `bool`<a id="safe-bool"></a>

Enable or disable safe search

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

#### 🔄 Return<a id="🔄-return"></a>

[`ImageSearchResults`](./shutterstock_python_sdk/pydantic/image_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/cv/similar/images` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.computer_vision.list_similar_videos`<a id="shutterstockcomputer_visionlist_similar_videos"></a>

This endpoint returns videos that are visually similar to an image that you specify or upload.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_similar_videos_response = shutterstock.computer_vision.list_similar_videos(
    asset_id="U6ba16262e3bc2db470b8e3cfa8aaab25",
    license=["commercial"],
    safe=True,
    language="es",
    page=1,
    per_page=20,
    view="minimal",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_id: `str`<a id="asset_id-str"></a>

The asset ID or upload ID to find similar videos for

##### license: List[`str`]<a id="license-liststr"></a>

Show only videos with the specified license

##### safe: `bool`<a id="safe-bool"></a>

Enable or disable safe search

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

#### 🔄 Return<a id="🔄-return"></a>

[`VideoSearchResults`](./shutterstock_python_sdk/pydantic/video_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/cv/similar/videos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.computer_vision.list_suggested_keywords`<a id="shutterstockcomputer_visionlist_suggested_keywords"></a>

This endpoint returns a list of suggested keywords for a media item that you specify or upload.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_suggested_keywords_response = shutterstock.computer_vision.list_suggested_keywords(
    asset_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_id: Union[`str`, `str`]<a id="asset_id-unionstr-str"></a>


The asset ID or upload ID to suggest keywords for

#### 🔄 Return<a id="🔄-return"></a>

[`KeywordDataList`](./shutterstock_python_sdk/pydantic/keyword_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/cv/keywords` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.computer_vision.upload_image`<a id="shutterstockcomputer_visionupload_image"></a>

This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_image_response = shutterstock.computer_vision.upload_image(
    base64_image="R0lGODlhgACAAPcAAEwiBLyaLOzNUNmWFNjOrNSuN7x6PPzqeOTMgfKSDMyuTPzwsdi2dHwuBPzbVu",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base64_image: `str`<a id="base64_image-str"></a>

A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImageCreateRequest`](./shutterstock_python_sdk/type/image_create_request.py)
A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height

#### 🔄 Return<a id="🔄-return"></a>

[`ComputerVisionImageCreateResponse`](./shutterstock_python_sdk/pydantic/computer_vision_image_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/cv/images` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.computer_vision.upload_image_ephemeral`<a id="shutterstockcomputer_visionupload_image_ephemeral"></a>

Deprecated; use `POST /v2/cv/images` instead. This endpoint uploads an image for reverse image search. The image must be in JPEG or PNG format. To get the search results, pass the ID that this endpoint returns to the `GET /v2/images/{id}/similar` endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_image_ephemeral_response = shutterstock.computer_vision.upload_image_ephemeral(
    base64_image="R0lGODlhgACAAPcAAEwiBLyaLOzNUNmWFNjOrNSuN7x6PPzqeOTMgfKSDMyuTPzwsdi2dHwuBPzbVu",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base64_image: `str`<a id="base64_image-str"></a>

A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImageCreateRequest`](./shutterstock_python_sdk/type/image_create_request.py)
The image data in JPEG or PNG format

#### 🔄 Return<a id="🔄-return"></a>

[`ImageCreateResponse`](./shutterstock_python_sdk/pydantic/image_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.contributors.get_collection_details`<a id="shutterstockcontributorsget_collection_details"></a>

This endpoint gets more detailed information about a contributor's collection, including its cover image, timestamps for its creation, and most recent update. To get the items in collections, use GET /v2/contributors/{contributor_id}/collections/{id}/items.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_details_response = shutterstock.contributors.get_collection_details(
    contributor_id="800506",
    id="1991678",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contributor_id: `str`<a id="contributor_id-str"></a>

Contributor ID

##### id: `str`<a id="id-str"></a>

Collection ID that belongs to the contributor

#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./shutterstock_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/contributors/{contributor_id}/collections/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.contributors.get_collection_items`<a id="shutterstockcontributorsget_collection_items"></a>

This endpoint lists the IDs of items in a contributor's collection and the date that each was added.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_items_response = shutterstock.contributors.get_collection_items(
    contributor_id="800506",
    id="1991678",
    page=1,
    per_page=20,
    sort="newest",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contributor_id: `str`<a id="contributor_id-str"></a>

Contributor ID

##### id: `str`<a id="id-str"></a>

Collection ID that belongs to the contributor

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort order

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionItemDataList`](./shutterstock_python_sdk/pydantic/collection_item_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/contributors/{contributor_id}/collections/{id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.contributors.get_details`<a id="shutterstockcontributorsget_details"></a>

This endpoint shows information about a single contributor, including contributor type, equipment they use, and other attributes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = shutterstock.contributors.get_details(
    contributor_id="1653538",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contributor_id: `str`<a id="contributor_id-str"></a>

Contributor ID

#### 🔄 Return<a id="🔄-return"></a>

[`ContributorProfile`](./shutterstock_python_sdk/pydantic/contributor_profile.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/contributors/{contributor_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.contributors.get_details_multiple`<a id="shutterstockcontributorsget_details_multiple"></a>

This endpoint lists information about one or more contributors, including contributor type, equipment they use and other attributes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_multiple_response = shutterstock.contributors.get_details_multiple(
    id=[800506, 1653538],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

One or more contributor IDs

#### 🔄 Return<a id="🔄-return"></a>

[`ContributorProfileDataList`](./shutterstock_python_sdk/pydantic/contributor_profile_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/contributors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.contributors.list_collections`<a id="shutterstockcontributorslist_collections"></a>

This endpoint lists collections based on contributor ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collections_response = shutterstock.contributors.list_collections(
    contributor_id="800506",
    sort="newest",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contributor_id: `str`<a id="contributor_id-str"></a>

Contributor ID

##### sort: `str`<a id="sort-str"></a>

Sort order

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionDataList`](./shutterstock_python_sdk/pydantic/collection_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/contributors/{contributor_id}/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.custom_music.create_rendered_audio`<a id="shutterstockcustom_musiccreate_rendered_audio"></a>

This endpoint creates rendered audio from timeline data. It returns a render ID that you can use to download the finished audio when it is ready. The render ID is valid for up to 48 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_rendered_audio_response = shutterstock.custom_music.create_rendered_audio(
    audio_renders=[
        {
            "filename": "My Project.mp3",
            "preset": "MASTER_MP3",
            "timeline": {},
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audio_renders: List[`CreateAudioRender`]<a id="audio_renders-listcreateaudiorender"></a>

Parameters to create computer audio renders

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateAudioRendersRequest`](./shutterstock_python_sdk/type/create_audio_renders_request.py)
Parameters for the audio, including the timeline and information about the output file

#### 🔄 Return<a id="🔄-return"></a>

[`AudioRendersListResults`](./shutterstock_python_sdk/pydantic/audio_renders_list_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/ai/audio/renders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.custom_music.get_audio_renders_details`<a id="shutterstockcustom_musicget_audio_renders_details"></a>

This endpoint shows the status of one or more audio renders, including download links for completed audio.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_audio_renders_details_response = (
    shutterstock.custom_music.get_audio_renders_details(
        id=["L2w7h9VNFlkzpllSUunSYayenKjN", "BeHx3UNXzMBB4dGsC9aa6VxnpcWl"],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

One or more render IDs

#### 🔄 Return<a id="🔄-return"></a>

[`AudioRendersListResults`](./shutterstock_python_sdk/pydantic/audio_renders_list_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/ai/audio/renders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.custom_music.list_audio_descriptors`<a id="shutterstockcustom_musiclist_audio_descriptors"></a>

This endpoint lists the descriptors that you can use in the audio regions in an audio render.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_audio_descriptors_response = shutterstock.custom_music.list_audio_descriptors(
    render_speed_over=5,
    band_id="Corporate Folk Bonfire Band 1",
    band_name="Documentary Underscore Heartfelt Band 1",
    page=1,
    per_page=1,
    id=["documentary_underscore_heartfelt"],
    instrument_name="Precision Bass - Full",
    instrument_id="direct_fluorescent_synth_lead",
    tempo=90,
    tempo_to=120,
    tempo_from=60,
    name="Corporate Pop Inspirational High Energy",
    tag="Cinematic",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### render_speed_over: `Union[int, float]`<a id="render_speed_over-unionint-float"></a>

Show descriptors with an average render speed that is greater than or equal to the specified value

##### band_id: `str`<a id="band_id-str"></a>

Show descriptors that contain the specified band (case-sentsitive)

##### band_name: `str`<a id="band_name-str"></a>

Show descriptors with the specified band name (case-sensitive)

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### id: List[`str`]<a id="id-liststr"></a>

Show descriptors with the specified IDs (case-sensitive)

##### instrument_name: `str`<a id="instrument_name-str"></a>

Show descriptors with the specified instrument name (case-sensitive)

##### instrument_id: `str`<a id="instrument_id-str"></a>

Show descriptors with the specified instrument ID (case-sensitive)

##### tempo: `Union[int, float]`<a id="tempo-unionint-float"></a>

Show descriptors whose tempo range includes the specified tempo in beats per minute

##### tempo_to: `Union[int, float]`<a id="tempo_to-unionint-float"></a>

Show descriptors with a tempo that is less than or equal to the specified number

##### tempo_from: `Union[int, float]`<a id="tempo_from-unionint-float"></a>

Show descriptors that have a tempo range that includes the specified tempo in beats per minute

##### name: `str`<a id="name-str"></a>

Show descriptors with the specified name (case-sensitive)

##### tag: `str`<a id="tag-str"></a>

Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive)

#### 🔄 Return<a id="🔄-return"></a>

[`DescriptorsListResult`](./shutterstock_python_sdk/pydantic/descriptors_list_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/ai/audio/descriptors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.custom_music.list_computer_audio_instruments`<a id="shutterstockcustom_musiclist_computer_audio_instruments"></a>

This endpoint lists the instruments that you can include in computer audio. If you specify more than one search parameter, the API uses an AND condition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_computer_audio_instruments_response = (
    shutterstock.custom_music.list_computer_audio_instruments(
        id=["wood_blocks"],
        per_page=1,
        page=1,
        name="Precision Bass - Full",
        tag="Percussion",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

Show instruments with the specified ID

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### page: `int`<a id="page-int"></a>

Page number

##### name: `str`<a id="name-str"></a>

Show instruments with the specified name (case-sensitive)

##### tag: `str`<a id="tag-str"></a>

Show instruments with the specified tag, such as Percussion or Strings (case-sensitive)

#### 🔄 Return<a id="🔄-return"></a>

[`InstrumentsListResult`](./shutterstock_python_sdk/pydantic/instruments_list_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/ai/audio/instruments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.get_details`<a id="shutterstockeditorial_imagesget_details"></a>

Deprecated; use `GET /v2/editorial/images/{id}` instead to show information about an editorial image, including a URL to a preview image and the sizes that it is available in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = shutterstock.editorial_images.get_details(
    id="9926131a",
    country="USA",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Editorial ID

##### country: `str`<a id="country-str"></a>

Returns only if the content is available for distribution in a certain country

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialContent`](./shutterstock_python_sdk/pydantic/editorial_content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.get_image_details`<a id="shutterstockeditorial_imagesget_image_details"></a>

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_image_details_response = shutterstock.editorial_images.get_image_details(
    id="9926131a",
    country="USA",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Editorial ID

##### country: `str`<a id="country-str"></a>

Returns only if the content is available for distribution in a certain country

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialContent`](./shutterstock_python_sdk/pydantic/editorial_content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.get_livefeed_images`<a id="shutterstockeditorial_imagesget_livefeed_images"></a>

Get editorial livefeed

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_livefeed_images_response = shutterstock.editorial_images.get_livefeed_images(
    id="2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London",
    country="USA",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Editorial livefeed ID; must be an URI encoded string

##### country: `str`<a id="country-str"></a>

Returns only if the livefeed is available for distribution in a certain country

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialImageLivefeed`](./shutterstock_python_sdk/pydantic/editorial_image_livefeed.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/livefeeds/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.get_livefeed_items`<a id="shutterstockeditorial_imagesget_livefeed_items"></a>

Get editorial livefeed items

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_livefeed_items_response = shutterstock.editorial_images.get_livefeed_items(
    id="2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London",
    country="USA",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Editorial livefeed ID; must be an URI encoded string

##### country: `str`<a id="country-str"></a>

Returns only if the livefeed items are available for distribution in a certain country

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialImageContentDataList`](./shutterstock_python_sdk/pydantic/editorial_image_content_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/livefeeds/{id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.get_livefeed_items_0`<a id="shutterstockeditorial_imagesget_livefeed_items_0"></a>

Deprecated: use `GET /v2/editorial/images/livefeeds/{id}` instead to get an editorial livefeed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_livefeed_items_0_response = shutterstock.editorial_images.get_livefeed_items_0(
    id="2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London",
    country="USA",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Editorial livefeed ID; must be an URI encoded string

##### country: `str`<a id="country-str"></a>

Returns only if the livefeed is available for distribution in a certain country

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialLivefeed`](./shutterstock_python_sdk/pydantic/editorial_livefeed.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/livefeeds/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.get_livefeed_items_1`<a id="shutterstockeditorial_imagesget_livefeed_items_1"></a>

Deprecated; use `GET /v2/editorial/images/livefeeds/{id}/items` instead to get editorial livefeed items.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_livefeed_items_1_response = shutterstock.editorial_images.get_livefeed_items_1(
    id="2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London",
    country="USA",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Editorial livefeed ID; must be an URI encoded string

##### country: `str`<a id="country-str"></a>

Returns only if the livefeed items are available for distribution in a certain country

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialContentDataList`](./shutterstock_python_sdk/pydantic/editorial_content_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/livefeeds/{id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.get_livefeed_list`<a id="shutterstockeditorial_imagesget_livefeed_list"></a>

Deprecated; use `GET /v2/editorial/images/livefeeds` instead to get a list of editorial livefeeds.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_livefeed_list_response = shutterstock.editorial_images.get_livefeed_list(
    country="USA",
    page=1,
    per_page=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

Returns only livefeeds that are available for distribution in a certain country

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialLivefeedList`](./shutterstock_python_sdk/pydantic/editorial_livefeed_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/livefeeds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.license_content`<a id="shutterstockeditorial_imageslicense_content"></a>

This endpoint gets licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
license_content_response = shutterstock.editorial_images.license_content(
    country=None,
    editorial=[
        {
            "editorial_id": "10687730b",
            "license": "premier_editorial_comp",
            "size": "original",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `ISOCountryCode`<a id="country-isocountrycode"></a>

##### editorial: List[`LicenseEditorialContent`]<a id="editorial-listlicenseeditorialcontent"></a>

Editorial content to license

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LicenseEditorialContentRequest`](./shutterstock_python_sdk/type/license_editorial_content_request.py)
License editorial content

#### 🔄 Return<a id="🔄-return"></a>

[`LicenseEditorialContentResults`](./shutterstock_python_sdk/pydantic/license_editorial_content_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/licenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.license_content_0`<a id="shutterstockeditorial_imageslicense_content_0"></a>

Deprecated; use `POST /v2/editorial/images/licenses` instead to get licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
license_content_0_response = shutterstock.editorial_images.license_content_0(
    country=None,
    editorial=[
        {
            "editorial_id": "10687730b",
            "license": "premier_editorial_comp",
            "size": "original",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `ISOCountryCode`<a id="country-isocountrycode"></a>

##### editorial: List[`LicenseEditorialContent`]<a id="editorial-listlicenseeditorialcontent"></a>

Editorial content to license

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LicenseEditorialContentRequest`](./shutterstock_python_sdk/type/license_editorial_content_request.py)
License editorial content

#### 🔄 Return<a id="🔄-return"></a>

[`LicenseEditorialContentResults`](./shutterstock_python_sdk/pydantic/license_editorial_content_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/licenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.list_categories`<a id="shutterstockeditorial_imageslist_categories"></a>

Deprecated; use `GET /v2/editorial/images/categories` instead. This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_categories_response = shutterstock.editorial_images.list_categories()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialCategoryResults`](./shutterstock_python_sdk/pydantic/editorial_category_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.list_categories_0`<a id="shutterstockeditorial_imageslist_categories_0"></a>

This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_categories_0_response = shutterstock.editorial_images.list_categories_0()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialImageCategoryResults`](./shutterstock_python_sdk/pydantic/editorial_image_category_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.list_licenses`<a id="shutterstockeditorial_imageslist_licenses"></a>

This endpoint lists existing editorial image licenses.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_licenses_response = shutterstock.editorial_images.list_licenses(
    image_id="12345678",
    license="premier_editorial_all_digital",
    page=1,
    per_page=20,
    sort="newest",
    username="aUniqueUsername",
    start_date="2021-03-29T13:25:13.521Z",
    end_date="2021-03-29T13:25:13.521Z",
    download_availability="all",
    team_history=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### image_id: `str`<a id="image_id-str"></a>

Show licenses for the specified editorial image ID

##### license: `str`<a id="license-str"></a>

Show editorial images that are available with the specified license name

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort order

##### username: `str`<a id="username-str"></a>

Filter licenses by username of licensee

##### start_date: `datetime`<a id="start_date-datetime"></a>

Show licenses created on or after the specified date

##### end_date: `datetime`<a id="end_date-datetime"></a>

Show licenses created before the specified date

##### download_availability: `str`<a id="download_availability-str"></a>

Filter licenses by download availability

##### team_history: `bool`<a id="team_history-bool"></a>

Set to true to see license history for all members of your team.

#### 🔄 Return<a id="🔄-return"></a>

[`DownloadHistoryDataList`](./shutterstock_python_sdk/pydantic/download_history_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/licenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.list_livefeed_images`<a id="shutterstockeditorial_imageslist_livefeed_images"></a>

Get editorial livefeed list

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_livefeed_images_response = shutterstock.editorial_images.list_livefeed_images(
    country="USA",
    page=1,
    per_page=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

Returns only livefeeds that are available for distribution in a certain country

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialImageLivefeedList`](./shutterstock_python_sdk/pydantic/editorial_image_livefeed_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/livefeeds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.list_updated_content`<a id="shutterstockeditorial_imageslist_updated_content"></a>

This endpoint lists editorial images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was taken.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_updated_content_response = shutterstock.editorial_images.list_updated_content(
    type="edit",
    date_updated_start="2021-03-29T13:25:13.521Z",
    date_updated_end="2021-03-29T13:25:13.521Z",
    country="USA",
    date_taken_start="2020-02-04T00:00:00.000Z",
    date_taken_end="2020-02-05T00:00:00.000Z",
    cursor="eyJ2IjoxLCJzIjoyfQ==",
    sort="newest",
    supplier_code=["ABC"],
    per_page=200,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted

##### date_updated_start: `datetime`<a id="date_updated_start-datetime"></a>

Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.

##### date_updated_end: `datetime`<a id="date_updated_end-datetime"></a>

Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.

##### country: `str`<a id="country-str"></a>

Show only editorial content that is available for distribution in a certain country

##### date_taken_start: `date`<a id="date_taken_start-date"></a>

Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets

##### date_taken_end: `date`<a id="date_taken_end-date"></a>

Show images that were taken before the specified date

##### cursor: `str`<a id="cursor-str"></a>

The cursor of the page with which to start fetching results; this cursor is returned from previous requests

##### sort: `str`<a id="sort-str"></a>

Sort by

##### supplier_code: List[`str`]<a id="supplier_code-liststr"></a>

Show only editorial content from certain suppliers

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialUpdatedResults`](./shutterstock_python_sdk/pydantic/editorial_updated_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/updated` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.list_updated_content_0`<a id="shutterstockeditorial_imageslist_updated_content_0"></a>

Deprecated; use `GET /v2/editorial/images/updated` instead to get recently updated items.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_updated_content_0_response = shutterstock.editorial_images.list_updated_content_0(
    type="edit",
    date_updated_start="2021-03-29T13:25:13.521Z",
    date_updated_end="2021-03-29T13:25:13.521Z",
    country="USA",
    date_taken_start="2020-02-04T00:00:00.000Z",
    date_taken_end="2020-02-05T00:00:00.000Z",
    cursor="eyJ2IjoxLCJzIjoyfQ==",
    sort="newest",
    supplier_code=["ABC"],
    per_page=200,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted

##### date_updated_start: `datetime`<a id="date_updated_start-datetime"></a>

Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.

##### date_updated_end: `datetime`<a id="date_updated_end-datetime"></a>

Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.

##### country: `str`<a id="country-str"></a>

Show only editorial content that is available for distribution in a certain country

##### date_taken_start: `date`<a id="date_taken_start-date"></a>

Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets

##### date_taken_end: `date`<a id="date_taken_end-date"></a>

Show images that were taken before the specified date

##### cursor: `str`<a id="cursor-str"></a>

The cursor of the page with which to start fetching results; this cursor is returned from previous requests

##### sort: `str`<a id="sort-str"></a>

Sort by

##### supplier_code: List[`str`]<a id="supplier_code-liststr"></a>

Show only editorial content from certain suppliers

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialUpdatedResults`](./shutterstock_python_sdk/pydantic/editorial_updated_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/updated` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.search`<a id="shutterstockeditorial_imagessearch"></a>

This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the `category` parameter to "Alone,Performing" and also specify a `query` parameter, the results include only images that match the query and are in both the Alone and Performing categories. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_response = shutterstock.editorial_images.search(
    country="USA",
    query="The Academy Awards",
    sort="relevant",
    category="Alone,Performing",
    supplier_code=["string_example"],
    date_start="2020-05-29T00:00:00.000Z",
    date_end="2021-05-29T00:00:00.000Z",
    per_page=20,
    cursor="eyJ2IjoxLCJzIjoxfQ==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

Show only editorial content that is available for distribution in a certain country

##### query: `str`<a id="query-str"></a>

One or more search terms separated by spaces

##### sort: `str`<a id="sort-str"></a>

Sort by

##### category: `str`<a id="category-str"></a>

Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list

##### supplier_code: List[`str`]<a id="supplier_code-liststr"></a>

Show only editorial content from certain suppliers

##### date_start: `date`<a id="date_start-date"></a>

Show only editorial content generated on or after a specific date

##### date_end: `date`<a id="date_end-date"></a>

Show only editorial content generated on or before a specific date

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### cursor: `str`<a id="cursor-str"></a>

The cursor of the page with which to start fetching results; this cursor is returned from previous requests

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialSearchResults`](./shutterstock_python_sdk/pydantic/editorial_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/images/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_images.search_content`<a id="shutterstockeditorial_imagessearch_content"></a>

Deprecated; use `GET /v2/editorial/images/search` instead to search for editorial images.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_content_response = shutterstock.editorial_images.search_content(
    country="USA",
    query="string_example",
    sort="relevant",
    category="string_example",
    supplier_code=["string_example"],
    date_start="1970-01-01",
    date_end="1970-01-01",
    per_page=20,
    cursor="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

Show only editorial content that is available for distribution in a certain country

##### query: `str`<a id="query-str"></a>

One or more search terms separated by spaces

##### sort: `str`<a id="sort-str"></a>

Sort by

##### category: `str`<a id="category-str"></a>

Show editorial content within a certain editorial category; specify by category name

##### supplier_code: List[`str`]<a id="supplier_code-liststr"></a>

Show only editorial content from certain suppliers

##### date_start: `date`<a id="date_start-date"></a>

Show only editorial content generated on or after a specific date

##### date_end: `date`<a id="date_end-date"></a>

Show only editorial content generated on or before a specific date

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### cursor: `str`<a id="cursor-str"></a>

The cursor of the page with which to start fetching results; this cursor is returned from previous requests

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialSearchResults`](./shutterstock_python_sdk/pydantic/editorial_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_video.get_content_details`<a id="shutterstockeditorial_videoget_content_details"></a>

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_details_response = shutterstock.editorial_video.get_content_details(
    id="9926131a",
    country="USA",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Editorial ID

##### country: `str`<a id="country-str"></a>

Returns only if the content is available for distribution in a certain country

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialVideoContent`](./shutterstock_python_sdk/pydantic/editorial_video_content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/videos/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_video.license_videos`<a id="shutterstockeditorial_videolicense_videos"></a>

This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more editorial videos to license. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
license_videos_response = shutterstock.editorial_video.license_videos(
    country=None,
    editorial=[
        {
            "editorial_id": "10679854a",
            "license": "premier_editorial_video_digital_only",
            "size": "original",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `ISOCountryCode`<a id="country-isocountrycode"></a>

##### editorial: List[`LicenseEditorialVideoContent`]<a id="editorial-listlicenseeditorialvideocontent"></a>

Editorial content to license

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LicenseEditorialVideoContentRequest`](./shutterstock_python_sdk/type/license_editorial_video_content_request.py)
License editorial video content

#### 🔄 Return<a id="🔄-return"></a>

[`LicenseEditorialContentResults`](./shutterstock_python_sdk/pydantic/license_editorial_content_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/videos/licenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_video.list_video_categories`<a id="shutterstockeditorial_videolist_video_categories"></a>

This endpoint lists the categories that editorial videos can belong to, which are separate from the categories that other types of assets can belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_video_categories_response = shutterstock.editorial_video.list_video_categories()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialVideoCategoryResults`](./shutterstock_python_sdk/pydantic/editorial_video_category_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/videos/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_video.list_video_licenses`<a id="shutterstockeditorial_videolist_video_licenses"></a>

This endpoint lists existing editorial video licenses.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_video_licenses_response = shutterstock.editorial_video.list_video_licenses(
    video_id="12345678",
    license="premier_editorial_all_media",
    page=1,
    per_page=20,
    sort="newest",
    username="aUniqueUsername",
    start_date="2021-03-29T13:25:13.521Z",
    end_date="2021-03-29T13:25:13.521Z",
    download_availability="all",
    team_history=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

Show licenses for the specified editorial video ID

##### license: `str`<a id="license-str"></a>

Show editorial videos that are available with the specified license name

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort order

##### username: `str`<a id="username-str"></a>

Filter licenses by username of licensee

##### start_date: `datetime`<a id="start_date-datetime"></a>

Show licenses created on or after the specified date

##### end_date: `datetime`<a id="end_date-datetime"></a>

Show licenses created before the specified date

##### download_availability: `str`<a id="download_availability-str"></a>

Filter licenses by download availability

##### team_history: `bool`<a id="team_history-bool"></a>

Set to true to see license history for all members of your team.

#### 🔄 Return<a id="🔄-return"></a>

[`DownloadHistoryDataList`](./shutterstock_python_sdk/pydantic/download_history_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/videos/licenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.editorial_video.search_video_content`<a id="shutterstockeditorial_videosearch_video_content"></a>

This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the `category` parameter to "Alone,Performing" and also specify a `query` parameter, the results include only videos that match the query and are in both the Alone and Performing categories.  You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_video_content_response = shutterstock.editorial_video.search_video_content(
    country="USA",
    query="The Academy Awards",
    sort="relevant",
    category="Alone,Performing",
    supplier_code=["string_example"],
    date_start="2020-05-29T00:00:00.000Z",
    date_end="2021-05-29T00:00:00.000Z",
    resolution="4k",
    fps=24,
    per_page=20,
    cursor="eyJ2IjoxLCJzIjoxfQ==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

Show only editorial video content that is available for distribution in a certain country

##### query: `str`<a id="query-str"></a>

One or more search terms separated by spaces

##### sort: `str`<a id="sort-str"></a>

Sort by

##### category: `str`<a id="category-str"></a>

Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list

##### supplier_code: List[`str`]<a id="supplier_code-liststr"></a>

Show only editorial video content from certain suppliers

##### date_start: `date`<a id="date_start-date"></a>

Show only editorial video content generated on or after a specific date

##### date_end: `date`<a id="date_end-date"></a>

Show only editorial video content generated on or before a specific date

##### resolution: `str`<a id="resolution-str"></a>

Show only editorial video content with specific resolution

##### fps: `Union[int, float]`<a id="fps-unionint-float"></a>

Show only editorial video content generated with specific frames per second

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### cursor: `str`<a id="cursor-str"></a>

The cursor of the page with which to start fetching results; this cursor is returned from previous requests

#### 🔄 Return<a id="🔄-return"></a>

[`EditorialVideoSearchResults`](./shutterstock_python_sdk/pydantic/editorial_video_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/editorial/videos/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.add_to_collection_items`<a id="shutterstockimagesadd_to_collection_items"></a>

This endpoint adds one or more images to a collection by image IDs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.images.add_to_collection_items(
    items=[
        {
            "added_time": "2020-05-29T17:10:22Z",
            "id": "297886754",
            "media_type": "image",
        }
    ],
    id="126351027",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: List[`CollectionItem`]<a id="items-listcollectionitem"></a>

List of items

##### id: `str`<a id="id-str"></a>

Collection ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionItemRequest`](./shutterstock_python_sdk/type/collection_item_request.py)
Array of image IDs to add to the collection

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/{id}/items` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.create_collection`<a id="shutterstockimagescreate_collection"></a>

This endpoint creates one or more image collections (lightboxes). To add images to the collections, use `POST /v2/images/collections/{id}/items`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_collection_response = shutterstock.images.create_collection(
    name="Test Collection 19cf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the collection

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionCreateRequest`](./shutterstock_python_sdk/type/collection_create_request.py)
The names of the new collections

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionCreateResponse`](./shutterstock_python_sdk/pydantic/collection_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.delete_collection`<a id="shutterstockimagesdelete_collection"></a>

This endpoint deletes an image collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.images.delete_collection(
    id="136351027",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.extract_keywords_from_text`<a id="shutterstockimagesextract_keywords_from_text"></a>

This endpoint returns up to 10 important keywords from a block of plain text.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
extract_keywords_from_text_response = shutterstock.images.extract_keywords_from_text(
    text="Planting flowers is a great way to make springtime more beautiful.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### text: `str`<a id="text-str"></a>

Plain text to extract keywords from

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SearchEntitiesRequest`](./shutterstock_python_sdk/type/search_entities_request.py)
Plain text to extract keywords from

#### 🔄 Return<a id="🔄-return"></a>

[`SearchEntitiesResponse`](./shutterstock_python_sdk/pydantic/search_entities_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/search/suggestions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.featured_collection_details`<a id="shutterstockimagesfeatured_collection_details"></a>

This endpoint gets more detailed information about a featured collection, including its cover image and timestamps for its creation and most recent update. To get the images, use `GET /v2/images/collections/featured/{id}/items`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
featured_collection_details_response = shutterstock.images.featured_collection_details(
    id="136351027",
    embed="share_url",
    asset_hint="1x",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### embed: `str`<a id="embed-str"></a>

Which sharing information to include in the response, such as a URL to the collection

##### asset_hint: `str`<a id="asset_hint-str"></a>

Cover image size

#### 🔄 Return<a id="🔄-return"></a>

[`FeaturedCollection`](./shutterstock_python_sdk/pydantic/featured_collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/featured/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.get_collection_details`<a id="shutterstockimagesget_collection_details"></a>

This endpoint gets more detailed information about a collection, including its cover image and timestamps for its creation and most recent update. To get the images in collections, use `GET /v2/images/collections/{id}/items`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_details_response = shutterstock.images.get_collection_details(
    id="126351027",
    embed=["string_example"],
    share_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### embed: List[`str`]<a id="embed-liststr"></a>

Which sharing information to include in the response, such as a URL to the collection

##### share_code: `str`<a id="share_code-str"></a>

Code to retrieve a shared collection

#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./shutterstock_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.get_collection_items`<a id="shutterstockimagesget_collection_items"></a>

This endpoint lists the IDs of images in a featured collection and the date that each was added.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_items_response = shutterstock.images.get_collection_items(
    id="136351027",
    page=1,
    per_page=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionItemDataList`](./shutterstock_python_sdk/pydantic/collection_item_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/featured/{id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.get_collection_items_0`<a id="shutterstockimagesget_collection_items_0"></a>

This endpoint lists the IDs of images in a collection and the date that each was added.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_items_0_response = shutterstock.images.get_collection_items_0(
    id="126351027",
    page=1,
    per_page=100,
    share_code="string_example",
    sort="oldest",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### share_code: `str`<a id="share_code-str"></a>

Code to retrieve the contents of a shared collection

##### sort: `str`<a id="sort-str"></a>

Sort order

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionItemDataList`](./shutterstock_python_sdk/pydantic/collection_item_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/{id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.get_details`<a id="shutterstockimagesget_details"></a>

This endpoint shows information about an image, including a URL to a preview image and the sizes that it is available in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = shutterstock.images.get_details(
    id="465011609",
    language="es",
    view="full",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Image ID

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`Image`](./shutterstock_python_sdk/pydantic/image.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.get_search_suggestions`<a id="shutterstockimagesget_search_suggestions"></a>

This endpoint provides autocomplete suggestions for partial search terms.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_search_suggestions_response = shutterstock.images.get_search_suggestions(
    query="cats",
    limit=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

Search term for which you want keyword suggestions

##### limit: `int`<a id="limit-int"></a>

Limit the number of suggestions

#### 🔄 Return<a id="🔄-return"></a>

[`Suggestions`](./shutterstock_python_sdk/pydantic/suggestions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/search/suggestions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.license_images_for_multiple`<a id="shutterstockimageslicense_images_for_multiple"></a>

This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and other details like the format, size, and subscription ID either in the query parameter or with each image ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
license_images_for_multiple_response = shutterstock.images.license_images_for_multiple(
    images=[
        {
            "editorial_acknowledgement": True,
            "format": "jpg",
            "image_id": "123456789",
            "price": 12.34,
            "show_modal": True,
            "size": "small",
            "subscription_id": "s12345678",
        }
    ],
    subscription_id="string_example",
    format="eps",
    size="huge",
    search_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### images: [`LicenseImageRequestImages`](./shutterstock_python_sdk/type/license_image_request_images.py)<a id="images-licenseimagerequestimagesshutterstock_python_sdktypelicense_image_request_imagespy"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription ID to use to license the image

##### format: `str`<a id="format-str"></a>

(Deprecated) Image format

##### size: `str`<a id="size-str"></a>

Image size

##### search_id: `str`<a id="search_id-str"></a>

Search ID that was provided in the results of an image search

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LicenseImageRequest`](./shutterstock_python_sdk/type/license_image_request.py)
List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters

#### 🔄 Return<a id="🔄-return"></a>

[`LicenseImageResultDataList`](./shutterstock_python_sdk/pydantic/license_image_result_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/licenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.list_categories`<a id="shutterstockimageslist_categories"></a>

This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_categories_response = shutterstock.images.list_categories(
    language="es",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

#### 🔄 Return<a id="🔄-return"></a>

[`CategoryDataList`](./shutterstock_python_sdk/pydantic/category_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.list_collections`<a id="shutterstockimageslist_collections"></a>

This endpoint lists your collections of images and their basic attributes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collections_response = shutterstock.images.list_collections(
    embed=["share_code"],
    page=1,
    per_page=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### embed: List[`str`]<a id="embed-liststr"></a>

Which sharing information to include in the response, such as a URL to the collection

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionDataList`](./shutterstock_python_sdk/pydantic/collection_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.list_featured_collections`<a id="shutterstockimageslist_featured_collections"></a>

This endpoint lists featured collections of specific types and a name and cover image for each collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_featured_collections_response = shutterstock.images.list_featured_collections(
    embed="share_url",
    type=["photo"],
    asset_hint="1x",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### embed: `str`<a id="embed-str"></a>

Which sharing information to include in the response, such as a URL to the collection

##### type: List[`str`]<a id="type-liststr"></a>

The types of collections to return

##### asset_hint: `str`<a id="asset_hint-str"></a>

Cover image size

#### 🔄 Return<a id="🔄-return"></a>

[`FeaturedCollectionDataList`](./shutterstock_python_sdk/pydantic/featured_collection_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/featured` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.list_info`<a id="shutterstockimageslist_info"></a>

This endpoint lists information about one or more images, including the available sizes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_info_response = shutterstock.images.list_info(
    id=["1110335168", "465011609"],
    view="minimal",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

One or more image IDs

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`ImageDataList`](./shutterstock_python_sdk/pydantic/image_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.list_licenses`<a id="shutterstockimageslist_licenses"></a>

This endpoint lists existing licenses.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_licenses_response = shutterstock.images.list_licenses(
    image_id="12345678",
    license="standard",
    page=1,
    per_page=20,
    sort="newest",
    username="aUniqueUsername",
    start_date="2021-03-29T13:25:13.521Z",
    end_date="2021-03-29T13:25:13.521Z",
    download_availability="all",
    team_history=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### image_id: `str`<a id="image_id-str"></a>

Show licenses for the specified image ID

##### license: `str`<a id="license-str"></a>

Show images that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort order

##### username: `str`<a id="username-str"></a>

Filter licenses by username of licensee

##### start_date: `datetime`<a id="start_date-datetime"></a>

Show licenses created on or after the specified date

##### end_date: `datetime`<a id="end_date-datetime"></a>

Show licenses created before the specified date

##### download_availability: `str`<a id="download_availability-str"></a>

Filter licenses by download availability

##### team_history: `bool`<a id="team_history-bool"></a>

Set to true to see license history for all members of your team.

#### 🔄 Return<a id="🔄-return"></a>

[`DownloadHistoryDataList`](./shutterstock_python_sdk/pydantic/download_history_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/licenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.list_recommended_images`<a id="shutterstockimageslist_recommended_images"></a>

This endpoint returns images that customers put in the same collection as the specified image IDs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_recommended_images_response = shutterstock.images.list_recommended_images(
    id=[465011609],
    max_items=20,
    safe=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

Image IDs

##### max_items: `int`<a id="max_items-int"></a>

Maximum number of results returned in the response

##### safe: `bool`<a id="safe-bool"></a>

Restrict results to safe images

#### 🔄 Return<a id="🔄-return"></a>

[`RecommendationDataList`](./shutterstock_python_sdk/pydantic/recommendation_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/recommendations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.list_similar_images`<a id="shutterstockimageslist_similar_images"></a>

This endpoint returns images that are visually similar to an image that you specify.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_similar_images_response = shutterstock.images.list_similar_images(
    id="465011609",
    language="es",
    page=1,
    per_page=20,
    view="minimal",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Image ID

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

#### 🔄 Return<a id="🔄-return"></a>

[`ImageSearchResults`](./shutterstock_python_sdk/pydantic/image_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/{id}/similar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.list_updated_content`<a id="shutterstockimageslist_updated_content"></a>

This endpoint lists images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the `interval` parameter to show images that were updated recently, but you can also use the `start_date` and `end_date` parameters to specify a range of no more than three days. Do not use the `interval` parameter with either `start_date` or `end_date`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_updated_content_response = shutterstock.images.list_updated_content(
    type=["addition"],
    start_date="2021-03-29T00:00:00.000Z",
    end_date="2021-03-29T00:00:00.000Z",
    interval="1 HOUR",
    page=1,
    per_page=100,
    sort="newest",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: List[`str`]<a id="type-liststr"></a>

Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways

##### start_date: `date`<a id="start_date-date"></a>

Show images updated on or after the specified date

##### end_date: `date`<a id="end_date-date"></a>

Show images updated before the specified date

##### interval: `str`<a id="interval-str"></a>

Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort order

#### 🔄 Return<a id="🔄-return"></a>

[`UpdatedMediaDataList`](./shutterstock_python_sdk/pydantic/updated_media_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/updated` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.redownload_license`<a id="shutterstockimagesredownload_license"></a>

This endpoint redownloads images that you have already received a license for. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
redownload_license_response = shutterstock.images.redownload_license(
    id="e123",
    auth_cookie={
        "name": "The name of the cookie",
        "value": "The value of the cookie",
    },
    show_modal=True,
    size="small",
    verification_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

License ID

##### auth_cookie: [`Cookie`](./shutterstock_python_sdk/type/cookie.py)<a id="auth_cookie-cookieshutterstock_python_sdktypecookiepy"></a>


##### show_modal: `bool`<a id="show_modal-bool"></a>

(Deprecated)

##### size: `str`<a id="size-str"></a>

Size of the image

##### verification_code: `str`<a id="verification_code-str"></a>

(Deprecated)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RedownloadImage`](./shutterstock_python_sdk/type/redownload_image.py)
Information about the images to redownload

#### 🔄 Return<a id="🔄-return"></a>

[`Url`](./shutterstock_python_sdk/pydantic/url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/licenses/{id}/downloads` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.remove_from_collection`<a id="shutterstockimagesremove_from_collection"></a>

This endpoint removes one or more images from a collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.images.remove_from_collection(
    id="126351027",
    item_id=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### item_id: List[`str`]<a id="item_id-liststr"></a>

One or more image IDs to remove from the collection

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/{id}/items` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.rename_collection`<a id="shutterstockimagesrename_collection"></a>

This endpoint sets a new name for an image collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.images.rename_collection(
    name="My collection with a new name",
    id="126351027",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The new name of the collection

##### id: `str`<a id="id-str"></a>

Collection ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionUpdateRequest`](./shutterstock_python_sdk/type/collection_update_request.py)
The new name for the collection

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/collections/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.run_multiple_searches`<a id="shutterstockimagesrun_multiple_searches"></a>

This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You can provide global search parameters in the query parameters and override them for each search in the body parameter. The query and body parameters are the same as in the `GET /v2/images/search` endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
run_multiple_searches_response = shutterstock.images.run_multiple_searches(
    body=["#/components/schemas/BulkImageSearchRequest/example"],
    added_date="2021-03-29T00:00:00.000Z",
    added_date_start="2021-03-29T00:00:00.000Z",
    aspect_ratio_min=1.7778,
    aspect_ratio_max=1.7778,
    aspect_ratio=1.7778,
    added_date_end="2021-03-29T00:00:00.000Z",
    category="string_example",
    color="4F21EA",
    contributor=["123456"],
    contributor_country=None,
    fields="string_example",
    height=1,
    height_from=1080,
    height_to=1080,
    image_type=["photo"],
    keyword_safe_search=True,
    language="fr",
    license=["string_example"],
    model=["12345", "67890"],
    orientation="vertical",
    page=1,
    per_page=10,
    people_model_released=True,
    people_age="20s",
    people_ethnicity=["hispanic"],
    people_gender="both",
    people_number=2,
    region="US",
    safe=True,
    sort="popular",
    spellcheck_query=True,
    view="minimal",
    width=1,
    width_from=1920,
    width_to=1920,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### added_date: `date`<a id="added_date-date"></a>

Show images added on the specified date

##### added_date_start: `date`<a id="added_date_start-date"></a>

Show images added on or after the specified date

##### aspect_ratio_min: `Union[int, float]`<a id="aspect_ratio_min-unionint-float"></a>

Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image

##### aspect_ratio_max: `Union[int, float]`<a id="aspect_ratio_max-unionint-float"></a>

Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image

##### aspect_ratio: `Union[int, float]`<a id="aspect_ratio-unionint-float"></a>

Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image

##### added_date_end: `date`<a id="added_date_end-date"></a>

Show images added before the specified date

##### category: `str`<a id="category-str"></a>

Show images with the specified Shutterstock-defined category; specify a category name or ID

##### color: `str`<a id="color-str"></a>

Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors

##### contributor: List[`str`]<a id="contributor-liststr"></a>

Show images with the specified contributor names or IDs, allows multiple

##### contributor_country: Union[`List[str]`, `List[str]`]<a id="contributor_country-unionliststr-liststr"></a>


Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search

##### fields: `str`<a id="fields-str"></a>

Fields to display in the response; see the documentation for the fields parameter in the overview section

##### height: `int`<a id="height-int"></a>

(Deprecated; use height_from and height_to instead) Show images with the specified height

##### height_from: `int`<a id="height_from-int"></a>

Show images with the specified height or larger, in pixels

##### height_to: `int`<a id="height_to-int"></a>

Show images with the specified height or smaller, in pixels

##### image_type: List[`str`]<a id="image_type-liststr"></a>

Show images of the specified type

##### keyword_safe_search: `bool`<a id="keyword_safe_search-bool"></a>

Hide results with potentially unsafe keywords

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Set query and result language (uses Accept-Language header if not set)

##### license: List[`str`]<a id="license-liststr"></a>

Show only images with the specified license

##### model: List[`str`]<a id="model-liststr"></a>

Show image results with the specified model IDs

##### orientation: `str`<a id="orientation-str"></a>

Show image results with horizontal or vertical orientation

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### people_model_released: `bool`<a id="people_model_released-bool"></a>

Show images of people with a signed model release

##### people_age: `str`<a id="people_age-str"></a>

Show images that feature people of the specified age category

##### people_ethnicity: List[`str`]<a id="people_ethnicity-liststr"></a>

Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities

##### people_gender: `str`<a id="people_gender-str"></a>

Show images with people of the specified gender

##### people_number: `int`<a id="people_number-int"></a>

Show images with the specified number of people

##### region: Union[`str`, `str`]<a id="region-unionstr-str"></a>


Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country

##### safe: `bool`<a id="safe-bool"></a>

Enable or disable safe search

##### sort: `str`<a id="sort-str"></a>

Sort by

##### spellcheck_query: `bool`<a id="spellcheck_query-bool"></a>

Spellcheck the search query and return results on suggested spellings

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### width: `int`<a id="width-int"></a>

(Deprecated; use width_from and width_to instead) Show images with the specified width

##### width_from: `int`<a id="width_from-int"></a>

Show images with the specified width or larger, in pixels

##### width_to: `int`<a id="width_to-int"></a>

Show images with the specified width or smaller, in pixels

##### requestBody: [`BulkImageSearchRequest`](./shutterstock_python_sdk/type/bulk_image_search_request.py)<a id="requestbody-bulkimagesearchrequestshutterstock_python_sdktypebulk_image_search_requestpy"></a>

List of queries to request results for and filters to apply per query; these values override the defaults in the query parameters

#### 🔄 Return<a id="🔄-return"></a>

[`BulkImageSearchResults`](./shutterstock_python_sdk/pydantic/bulk_image_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/bulk_search/images` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.images.search_images`<a id="shutterstockimagessearch_images"></a>

This endpoint searches for images. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media, not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_images_response = shutterstock.images.search_images(
    added_date="2021-03-29T00:00:00.000Z",
    added_date_start="2021-03-29T00:00:00.000Z",
    aspect_ratio_min=1.7778,
    aspect_ratio_max=1.7778,
    aspect_ratio=1.7778,
    ai_search=True,
    ai_labels_limit=20,
    ai_industry="automotive",
    ai_objective="awareness",
    added_date_end="2021-03-29T00:00:00.000Z",
    category="string_example",
    color="4F21EA",
    contributor=["123456"],
    contributor_country=None,
    fields="string_example",
    height=1,
    height_from=1080,
    height_to=1080,
    image_type=["photo"],
    keyword_safe_search=True,
    language="fr",
    license=["string_example"],
    model=["12345", "67890"],
    orientation="vertical",
    page=1,
    per_page=50,
    people_model_released=True,
    people_age="20s",
    people_ethnicity=["hispanic"],
    people_gender="both",
    people_number=2,
    query="dogs on the beach",
    region="US",
    safe=True,
    sort="popular",
    spellcheck_query=True,
    view="minimal",
    width=1,
    width_from=1920,
    width_to=1920,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### added_date: `date`<a id="added_date-date"></a>

Show images added on the specified date

##### added_date_start: `date`<a id="added_date_start-date"></a>

Show images added on or after the specified date

##### aspect_ratio_min: `Union[int, float]`<a id="aspect_ratio_min-unionint-float"></a>

Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image

##### aspect_ratio_max: `Union[int, float]`<a id="aspect_ratio_max-unionint-float"></a>

Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image

##### aspect_ratio: `Union[int, float]`<a id="aspect_ratio-unionint-float"></a>

Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image

##### ai_search: `bool`<a id="ai_search-bool"></a>

Set to true and specify the `ai_objective` and `ai_industry` parameters to use AI-powered search; the API returns information about how well images meet the objective for the industry 

##### ai_labels_limit: `int`<a id="ai_labels_limit-int"></a>

For AI-powered search, specify the maximum number of labels to return

##### ai_industry: `str`<a id="ai_industry-str"></a>

For AI-powered search, specify the industry to target; requires that the `ai_search` parameter is set to true

##### ai_objective: `str`<a id="ai_objective-str"></a>

For AI-powered search, specify the goal of the media; requires that the `ai_search` parameter is set to true

##### added_date_end: `date`<a id="added_date_end-date"></a>

Show images added before the specified date

##### category: `str`<a id="category-str"></a>

Show images with the specified Shutterstock-defined category; specify a category name or ID

##### color: `str`<a id="color-str"></a>

Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors

##### contributor: List[`str`]<a id="contributor-liststr"></a>

Show images with the specified contributor names or IDs, allows multiple

##### contributor_country: Union[`List[str]`, `List[str]`]<a id="contributor_country-unionliststr-liststr"></a>


Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search

##### fields: `str`<a id="fields-str"></a>

Fields to display in the response; see the documentation for the fields parameter in the overview section

##### height: `int`<a id="height-int"></a>

(Deprecated; use height_from and height_to instead) Show images with the specified height

##### height_from: `int`<a id="height_from-int"></a>

Show images with the specified height or larger, in pixels

##### height_to: `int`<a id="height_to-int"></a>

Show images with the specified height or smaller, in pixels

##### image_type: List[`str`]<a id="image_type-liststr"></a>

Show images of the specified type

##### keyword_safe_search: `bool`<a id="keyword_safe_search-bool"></a>

Hide results with potentially unsafe keywords

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Set query and result language (uses Accept-Language header if not set)

##### license: List[`str`]<a id="license-liststr"></a>

Show only images with the specified license

##### model: List[`str`]<a id="model-liststr"></a>

Show image results with the specified model IDs

##### orientation: `str`<a id="orientation-str"></a>

Show image results with horizontal or vertical orientation

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### people_model_released: `bool`<a id="people_model_released-bool"></a>

Show images of people with a signed model release

##### people_age: `str`<a id="people_age-str"></a>

Show images that feature people of the specified age category

##### people_ethnicity: List[`str`]<a id="people_ethnicity-liststr"></a>

Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities

##### people_gender: `str`<a id="people_gender-str"></a>

Show images with people of the specified gender

##### people_number: `int`<a id="people_number-int"></a>

Show images with the specified number of people

##### query: `str`<a id="query-str"></a>

One or more search terms separated by spaces; you can use NOT to filter out images that match a term

##### region: Union[`str`, `str`]<a id="region-unionstr-str"></a>


Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country

##### safe: `bool`<a id="safe-bool"></a>

Enable or disable safe search

##### sort: `str`<a id="sort-str"></a>

Sort by

##### spellcheck_query: `bool`<a id="spellcheck_query-bool"></a>

Spellcheck the search query and return results on suggested spellings

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### width: `int`<a id="width-int"></a>

(Deprecated; use width_from and width_to instead) Show images with the specified width

##### width_from: `int`<a id="width_from-int"></a>

Show images with the specified width or larger, in pixels

##### width_to: `int`<a id="width_to-int"></a>

Show images with the specified width or smaller, in pixels

#### 🔄 Return<a id="🔄-return"></a>

[`ImageSearchResults`](./shutterstock_python_sdk/pydantic/image_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/images/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.oauth.authorize_applications`<a id="shutterstockoauthauthorize_applications"></a>

This endpoint returns a redirect URI (in the 'Location' header) that the customer uses to authorize your application and, together with POST /v2/oauth/access_token, generate an access token that represents that authorization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.oauth.authorize_applications(
    client_id="6d097450b209c6dcd859",
    redirect_uri="localhost",
    response_type="code",
    state="1540290465000",
    realm="customer",
    scope="user.view",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Client ID (Consumer Key) of your application

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The callback URI to send the request to after authorization; must use a host name that is registered with your application

##### response_type: `str`<a id="response_type-str"></a>

Type of temporary authorization code that will be used to generate an access code; the only valid value is 'code'

##### state: `str`<a id="state-str"></a>

Unique value used by the calling app to verify the request

##### realm: `str`<a id="realm-str"></a>

User type to be authorized (usually 'customer')

##### scope: `str`<a id="scope-str"></a>

Space-separated list of scopes to be authorized

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/oauth/authorize` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.oauth.get_user_access_token`<a id="shutterstockoauthget_user_access_token"></a>

This endpoint returns an access token for the specified user and with the specified scopes. The token does not expire until the user changes their password. The body parameters must be encoded as form data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_access_token_response = shutterstock.oauth.get_user_access_token(
    client_id="string_example",
    grant_type="authorization_code",
    client_secret="string_example",
    code="string_example",
    expires=False,
    realm="customer",
    refresh_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Client ID (Consumer Key) of your application

##### grant_type: `str`<a id="grant_type-str"></a>

Grant type: authorization_code generates user tokens, client_credentials generates short-lived client grants

##### client_secret: `str`<a id="client_secret-str"></a>

Client Secret (Consumer Secret) of your application

##### code: `str`<a id="code-str"></a>

Response code from the /oauth/authorize flow; required if grant_type=authorization_code

##### expires: `bool`<a id="expires-bool"></a>

Whether or not the token expires, expiring tokens come with a refresh_token to renew the access_token

##### realm: `str`<a id="realm-str"></a>

User type to be authorized (usually 'customer')

##### refresh_token: `str`<a id="refresh_token-str"></a>

Pass this along with grant_type=refresh_token to get a fresh access token

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OauthGetUserAccessTokenRequest`](./shutterstock_python_sdk/type/oauth_get_user_access_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OauthAccessTokenResponse`](./shutterstock_python_sdk/pydantic/oauth_access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/oauth/access_token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.sound_effects.get_details`<a id="shutterstocksound_effectsget_details"></a>

This endpoint shows information about a sound effect.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = shutterstock.sound_effects.get_details(
    id=442583,
    language="cs",
    view="full",
    library="shutterstock",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Audio track ID

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### library: `str`<a id="library-str"></a>

Which library to fetch from

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`SFX`](./shutterstock_python_sdk/pydantic/sfx.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/sfx/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.sound_effects.license_assets`<a id="shutterstocksound_effectslicense_assets"></a>

This endpoint licenses sounds effect assets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
license_assets_response = shutterstock.sound_effects.license_assets(
    sound_effects=[
        {
            "audio_layout": "ambisonic",
            "format": "wav",
            "sfx_id": "123456789",
            "subscription_id": "s12345678",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sound_effects: List[`LicenseSFX`]<a id="sound_effects-listlicensesfx"></a>

Sound effects to license for

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LicenseSFXRequest`](./shutterstock_python_sdk/type/license_sfx_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LicenseSFXResultDataList`](./shutterstock_python_sdk/pydantic/license_sfx_result_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/sfx/licenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.sound_effects.list_details`<a id="shutterstocksound_effectslist_details"></a>

This endpoint shows information about sound effects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_details_response = shutterstock.sound_effects.list_details(
    id=["1110335168", "465011609"],
    view="minimal",
    language="cs",
    library="shutterstock",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

One or more sound effect IDs

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

##### library: `str`<a id="library-str"></a>

Which library to fetch from

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`SFXDataList`](./shutterstock_python_sdk/pydantic/sfx_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/sfx` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.sound_effects.list_licenses`<a id="shutterstocksound_effectslist_licenses"></a>

This endpoint lists existing licenses.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_licenses_response = shutterstock.sound_effects.list_licenses(
    sfx_id="12345678",
    license="standard",
    page=1,
    per_page=20,
    sort="newest",
    username="aUniqueUsername",
    start_date="2021-03-29T13:25:13.521Z",
    end_date="2021-03-29T13:25:13.521Z",
    license_id="j",
    download_availability="all",
    team_history=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sfx_id: `str`<a id="sfx_id-str"></a>

Show licenses for the specified sound effects ID

##### license: `str`<a id="license-str"></a>

Show sound effects that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort order

##### username: `str`<a id="username-str"></a>

Filter licenses by username of licensee

##### start_date: `datetime`<a id="start_date-datetime"></a>

Show licenses created on or after the specified date

##### end_date: `datetime`<a id="end_date-datetime"></a>

Show licenses created before the specified date

##### license_id: `str`<a id="license_id-str"></a>

Filter by the license ID

##### download_availability: `str`<a id="download_availability-str"></a>

Filter licenses by download availability

##### team_history: `bool`<a id="team_history-bool"></a>

Set to true to see license history for all members of your team.

#### 🔄 Return<a id="🔄-return"></a>

[`DownloadHistoryDataList`](./shutterstock_python_sdk/pydantic/download_history_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/sfx/licenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.sound_effects.redownload_licenses`<a id="shutterstocksound_effectsredownload_licenses"></a>

This endpoint redownloads sound effects that you have already received a license for. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
redownload_licenses_response = shutterstock.sound_effects.redownload_licenses(
    id="123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

License ID

#### 🔄 Return<a id="🔄-return"></a>

[`SfxUrl`](./shutterstock_python_sdk/pydantic/sfx_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/sfx/licenses/{id}/downloads` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.sound_effects.search_sound_effects`<a id="shutterstocksound_effectssearch_sound_effects"></a>

This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND condition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_sound_effects_response = shutterstock.sound_effects.search_sound_effects(
    added_date="2022-09-23T00:00:00.000Z",
    added_date_start="2021-03-29T00:00:00.000Z",
    added_date_end="2021-03-29T00:00:00.000Z",
    duration=180,
    duration_from=30,
    duration_to=180,
    page=1,
    per_page=1,
    query="drum",
    safe=True,
    sort="popular",
    view="full",
    language="cs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### added_date: `date`<a id="added_date-date"></a>

Show sound effects added on the specified date

##### added_date_start: `date`<a id="added_date_start-date"></a>

Show sound effects added on or after the specified date

##### added_date_end: `date`<a id="added_date_end-date"></a>

Show sound effects added before the specified date

##### duration: `int`<a id="duration-int"></a>

Show sound effects with the specified duration in seconds

##### duration_from: `int`<a id="duration_from-int"></a>

Show sound effects with the specified duration or longer in seconds

##### duration_to: `int`<a id="duration_to-int"></a>

Show sound effects with the specified duration or shorter in seconds

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### query: `str`<a id="query-str"></a>

One or more search terms separated by spaces

##### safe: `bool`<a id="safe-bool"></a>

Enable or disable safe search

##### sort: `str`<a id="sort-str"></a>

Sort by

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Set query and result language (uses Accept-Language header if not set)

#### 🔄 Return<a id="🔄-return"></a>

[`SFXSearchResults`](./shutterstock_python_sdk/pydantic/sfx_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/sfx/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.test.echo_text`<a id="shutterstocktestecho_text"></a>

Echo text

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
echo_text_response = shutterstock.test.echo_text(
    text="ok",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### text: `str`<a id="text-str"></a>

Text to echo

#### 🔄 Return<a id="🔄-return"></a>

[`TestEcho`](./shutterstock_python_sdk/pydantic/test_echo.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/test` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.test.input_validation`<a id="shutterstocktestinput_validation"></a>

Validate input

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
input_validation_response = shutterstock.test.input_validation(
    id=123,
    tag=["string_example"],
    user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Integer ID

##### tag: List[`str`]<a id="tag-liststr"></a>

List of tags

##### user_agent: `str`<a id="user_agent-str"></a>

User agent

#### 🔄 Return<a id="🔄-return"></a>

[`TestValidate`](./shutterstock_python_sdk/pydantic/test_validate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/test/validate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.users.get_access_token_details`<a id="shutterstockusersget_access_token_details"></a>

Get access token details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_access_token_details_response = shutterstock.users.get_access_token_details()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AccessTokenDetails`](./shutterstock_python_sdk/pydantic/access_token_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/user/access_token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.users.get_user_details`<a id="shutterstockusersget_user_details"></a>

Get user details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_details_response = shutterstock.users.get_user_details()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserDetails`](./shutterstock_python_sdk/pydantic/user_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/user` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.users.list_subscriptions`<a id="shutterstockuserslist_subscriptions"></a>

List user subscriptions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscriptions_response = shutterstock.users.list_subscriptions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SubscriptionDataList`](./shutterstock_python_sdk/pydantic/subscription_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/user/subscriptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.add_to_collection_items`<a id="shutterstockvideosadd_to_collection_items"></a>

This endpoint adds one or more videos to a collection by video IDs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.videos.add_to_collection_items(
    items=[
        {
            "added_time": "2020-05-29T17:10:22Z",
            "id": "297886754",
            "media_type": "image",
        }
    ],
    id="17555176",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: List[`CollectionItem`]<a id="items-listcollectionitem"></a>

List of items

##### id: `str`<a id="id-str"></a>

The ID of the collection to which items should be added

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionItemRequest`](./shutterstock_python_sdk/type/collection_item_request.py)
Array of video IDs to add to the collection

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/{id}/items` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.collection_details_get`<a id="shutterstockvideoscollection_details_get"></a>

This endpoint gets more detailed information about a featured video collection, including its cover video and timestamps for its creation and most recent update. To get the videos, use `GET /v2/videos/collections/featured/{id}/items`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
collection_details_get_response = shutterstock.videos.collection_details_get(
    id="136351027",
    embed="share_url",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### embed: `str`<a id="embed-str"></a>

What information to include in the response, such as a URL to the collection

#### 🔄 Return<a id="🔄-return"></a>

[`FeaturedCollection`](./shutterstock_python_sdk/pydantic/featured_collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/featured/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.collection_details_get_0`<a id="shutterstockvideoscollection_details_get_0"></a>

This endpoint gets more detailed information about a collection, including the timestamp for its creation and the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
collection_details_get_0_response = shutterstock.videos.collection_details_get_0(
    id="17555176",
    embed=["string_example"],
    share_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the collection to return

##### embed: List[`str`]<a id="embed-liststr"></a>

Which sharing information to include in the response, such as a URL to the collection

##### share_code: `str`<a id="share_code-str"></a>

Code to retrieve a shared collection

#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./shutterstock_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.create_video_collections`<a id="shutterstockvideoscreate_video_collections"></a>

This endpoint creates one or more collections (clipboxes). To add videos to collections, use `POST /v2/videos/collections/{id}/items`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_video_collections_response = shutterstock.videos.create_video_collections(
    name="Test Collection 19cf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the collection

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionCreateRequest`](./shutterstock_python_sdk/type/collection_create_request.py)
Collection metadata

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionCreateResponse`](./shutterstock_python_sdk/pydantic/collection_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.delete_collection`<a id="shutterstockvideosdelete_collection"></a>

This endpoint deletes a collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.videos.delete_collection(
    id="17555176",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the collection to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.find_similar`<a id="shutterstockvideosfind_similar"></a>

This endpoint searches for videos that are similar to a video that you specify.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_similar_response = shutterstock.videos.find_similar(
    id="2140697",
    language="es",
    page=1,
    per_page=20,
    view="minimal",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of a video for which similar videos should be returned

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

#### 🔄 Return<a id="🔄-return"></a>

[`VideoSearchResults`](./shutterstock_python_sdk/pydantic/video_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/{id}/similar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.get_collection_items`<a id="shutterstockvideosget_collection_items"></a>

This endpoint lists the IDs of videos in a collection and the date that each was added.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_items_response = shutterstock.videos.get_collection_items(
    id="17555176",
    page=1,
    per_page=100,
    share_code="string_example",
    sort="oldest",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### share_code: `str`<a id="share_code-str"></a>

Code to retrieve the contents of a shared collection

##### sort: `str`<a id="sort-str"></a>

Sort order

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionItemDataList`](./shutterstock_python_sdk/pydantic/collection_item_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/{id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.get_featured_collection_items`<a id="shutterstockvideosget_featured_collection_items"></a>

This endpoint lists the IDs of videos in a featured collection and the date that each was added.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_featured_collection_items_response = (
    shutterstock.videos.get_featured_collection_items(
        id="136351027",
        page=1,
        per_page=100,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Collection ID

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`VideoCollectionItemDataList`](./shutterstock_python_sdk/pydantic/video_collection_item_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/featured/{id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.license_videos`<a id="shutterstockvideoslicense_videos"></a>

This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
license_videos_response = shutterstock.videos.license_videos(
    videos=[
        {
            "size": "hd",
            "subscription_id": "s12345678",
            "video_id": "2140697",
        }
    ],
    subscription_id="s12345678",
    size="web",
    search_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### videos: List[`LicenseVideo`]<a id="videos-listlicensevideo"></a>

Videos to license

##### subscription_id: `str`<a id="subscription_id-str"></a>

The subscription ID to use for licensing

##### size: `str`<a id="size-str"></a>

The size of the video to license

##### search_id: `str`<a id="search_id-str"></a>

The Search ID that led to this licensing event

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LicenseVideoRequest`](./shutterstock_python_sdk/type/license_video_request.py)
List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters

#### 🔄 Return<a id="🔄-return"></a>

[`LicenseVideoResultDataList`](./shutterstock_python_sdk/pydantic/license_video_result_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/licenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.list_categories`<a id="shutterstockvideoslist_categories"></a>

This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_categories_response = shutterstock.videos.list_categories(
    language="es",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

#### 🔄 Return<a id="🔄-return"></a>

[`CategoryDataList`](./shutterstock_python_sdk/pydantic/category_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.list_collections`<a id="shutterstockvideoslist_collections"></a>

This endpoint lists your collections of videos and their basic attributes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collections_response = shutterstock.videos.list_collections(
    page=1,
    per_page=100,
    embed=["share_code"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### embed: List[`str`]<a id="embed-liststr"></a>

Which sharing information to include in the response, such as a URL to the collection

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionDataList`](./shutterstock_python_sdk/pydantic/collection_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.list_featured_video_collections`<a id="shutterstockvideoslist_featured_video_collections"></a>

This endpoint lists featured video collections and a name and cover video for each collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_featured_video_collections_response = (
    shutterstock.videos.list_featured_video_collections(
        embed="share_url",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### embed: `str`<a id="embed-str"></a>

What information to include in the response, such as a URL to the collection

#### 🔄 Return<a id="🔄-return"></a>

[`FeaturedCollectionDataList`](./shutterstock_python_sdk/pydantic/featured_collection_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/featured` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.list_licenses`<a id="shutterstockvideoslist_licenses"></a>

This endpoint lists existing licenses.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_licenses_response = shutterstock.videos.list_licenses(
    video_id="12345678",
    license="standard",
    page=1,
    per_page=20,
    sort="newest",
    username="aUniqueUsername",
    start_date="2021-03-29T13:25:13.521Z",
    end_date="2021-03-29T13:25:13.521Z",
    download_availability="all",
    team_history=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

Show licenses for the specified video ID

##### license: `str`<a id="license-str"></a>

Show videos that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort by oldest or newest videos first

##### username: `str`<a id="username-str"></a>

Filter licenses by username of licensee

##### start_date: `datetime`<a id="start_date-datetime"></a>

Show licenses created on or after the specified date

##### end_date: `datetime`<a id="end_date-datetime"></a>

Show licenses created before the specified date

##### download_availability: `str`<a id="download_availability-str"></a>

Filter licenses by download availability

##### team_history: `bool`<a id="team_history-bool"></a>

Set to true to see license history for all members of your team.

#### 🔄 Return<a id="🔄-return"></a>

[`DownloadHistoryDataList`](./shutterstock_python_sdk/pydantic/download_history_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/licenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.list_updated_videos`<a id="shutterstockvideoslist_updated_videos"></a>

This endpoint lists videos that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the `interval` parameter to show videos that were updated recently, but you can also use the `start_date` and `end_date` parameters to specify a range of no more than three days. Do not use the `interval` parameter with either `start_date` or `end_date`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_updated_videos_response = shutterstock.videos.list_updated_videos(
    start_date="2020-05-29T00:00:00.000Z",
    end_date="2021-05-29T00:00:00.000Z",
    interval="1 HOUR",
    page=1,
    per_page=100,
    sort="newest",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `date`<a id="start_date-date"></a>

Show videos updated on or after the specified date

##### end_date: `date`<a id="end_date-date"></a>

Show videos updated before the specified date

##### interval: `str`<a id="interval-str"></a>

Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### sort: `str`<a id="sort-str"></a>

Sort by oldest or newest videos first

#### 🔄 Return<a id="🔄-return"></a>

[`UpdatedMediaDataList`](./shutterstock_python_sdk/pydantic/updated_media_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/updated` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.list_video`<a id="shutterstockvideoslist_video"></a>

This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_video_response = shutterstock.videos.list_video(
    id=["639703", "993721"],
    view="minimal",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: List[`str`]<a id="id-liststr"></a>

One or more video IDs

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`VideoDataList`](./shutterstock_python_sdk/pydantic/video_data_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.redownload_downloads`<a id="shutterstockvideosredownload_downloads"></a>

This endpoint redownloads videos that you have already received a license for.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
redownload_downloads_response = shutterstock.videos.redownload_downloads(
    id="e123",
    auth_cookie={
        "name": "The name of the cookie",
        "value": "The value of the cookie",
    },
    show_modal=True,
    size="web",
    verification_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The license ID of the item to (re)download. The download links in the response are valid for 8 hours.

##### auth_cookie: [`Cookie`](./shutterstock_python_sdk/type/cookie.py)<a id="auth_cookie-cookieshutterstock_python_sdktypecookiepy"></a>


##### show_modal: `bool`<a id="show_modal-bool"></a>

(Deprecated)

##### size: `str`<a id="size-str"></a>

Size of the video

##### verification_code: `str`<a id="verification_code-str"></a>

(Deprecated)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RedownloadVideo`](./shutterstock_python_sdk/type/redownload_video.py)
Information about the videos to redownload

#### 🔄 Return<a id="🔄-return"></a>

[`Url`](./shutterstock_python_sdk/pydantic/url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/licenses/{id}/downloads` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.remove_from_collection`<a id="shutterstockvideosremove_from_collection"></a>

This endpoint removes one or more videos from a collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.videos.remove_from_collection(
    id="17555176",
    item_id=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Collection from which items will be deleted

##### item_id: List[`str`]<a id="item_id-liststr"></a>

One or more video IDs to remove from the collection

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/{id}/items` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.search_suggestions`<a id="shutterstockvideossearch_suggestions"></a>

This endpoint provides autocomplete suggestions for partial search terms.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_suggestions_response = shutterstock.videos.search_suggestions(
    query="cats",
    limit=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

Search term for which you want keyword suggestions

##### limit: `int`<a id="limit-int"></a>

Limit the number of the suggestions

#### 🔄 Return<a id="🔄-return"></a>

[`Suggestions`](./shutterstock_python_sdk/pydantic/suggestions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/search/suggestions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.search_video`<a id="shutterstockvideossearch_video"></a>

This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_video_response = shutterstock.videos.search_video(
    added_date="2020-05-29T00:00:00.000Z",
    added_date_start="2020-05-29T00:00:00.000Z",
    added_date_end="2020-05-29T00:00:00.000Z",
    aspect_ratio="43",
    category="string_example",
    contributor=["[12345678]"],
    contributor_country=["US"],
    duration=1,
    duration_from=60,
    duration_to=180,
    fps=3.14,
    fps_from=24,
    fps_to=60,
    keyword_safe_search=True,
    language="cs",
    license=["commercial", "editorial"],
    model=["442583", "434750"],
    page=1,
    per_page=20,
    people_age="20s",
    people_ethnicity=["hispanic"],
    people_gender="female",
    people_number=2,
    people_model_released=True,
    query="dogs running on the beach",
    resolution="4k",
    safe=True,
    sort="popular",
    view="minimal",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### added_date: `date`<a id="added_date-date"></a>

Show videos added on the specified date

##### added_date_start: `date`<a id="added_date_start-date"></a>

Show videos added on or after the specified date

##### added_date_end: `date`<a id="added_date_end-date"></a>

Show videos added before the specified date

##### aspect_ratio: `str`<a id="aspect_ratio-str"></a>

Show videos with the specified aspect ratio

##### category: `str`<a id="category-str"></a>

Show videos with the specified Shutterstock-defined category; specify a category name or ID

##### contributor: List[`str`]<a id="contributor-liststr"></a>

Show videos with the specified artist names or IDs

##### contributor_country: List[`str`]<a id="contributor_country-liststr"></a>

Show videos from contributors in one or more specified countries

##### duration: `int`<a id="duration-int"></a>

(Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in seconds

##### duration_from: `int`<a id="duration_from-int"></a>

Show videos with the specified duration or longer in seconds

##### duration_to: `int`<a id="duration_to-int"></a>

Show videos with the specified duration or shorter in seconds

##### fps: `Union[int, float]`<a id="fps-unionint-float"></a>

(Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second

##### fps_from: `Union[int, float]`<a id="fps_from-unionint-float"></a>

Show videos with the specified frames per second or more

##### fps_to: `Union[int, float]`<a id="fps_to-unionint-float"></a>

Show videos with the specified frames per second or fewer

##### keyword_safe_search: `bool`<a id="keyword_safe_search-bool"></a>

Hide results with potentially unsafe keywords

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Set query and result language (uses Accept-Language header if not set)

##### license: List[`str`]<a id="license-liststr"></a>

Show only videos with the specified license or licenses

##### model: List[`str`]<a id="model-liststr"></a>

Show videos with each of the specified models

##### page: `int`<a id="page-int"></a>

Page number

##### per_page: `int`<a id="per_page-int"></a>

Number of results per page

##### people_age: `str`<a id="people_age-str"></a>

Show videos that feature people of the specified age range

##### people_ethnicity: List[`str`]<a id="people_ethnicity-liststr"></a>

Show videos with people of the specified ethnicities

##### people_gender: `str`<a id="people_gender-str"></a>

Show videos with people with the specified gender

##### people_number: `int`<a id="people_number-int"></a>

Show videos with the specified number of people

##### people_model_released: `bool`<a id="people_model_released-bool"></a>

Show only videos of people with a signed model release

##### query: `str`<a id="query-str"></a>

One or more search terms separated by spaces; you can use NOT to filter out videos that match a term

##### resolution: `str`<a id="resolution-str"></a>

Show videos with the specified resolution

##### safe: `bool`<a id="safe-bool"></a>

Enable or disable safe search

##### sort: `str`<a id="sort-str"></a>

Sort by one of these categories

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

#### 🔄 Return<a id="🔄-return"></a>

[`VideoSearchResults`](./shutterstock_python_sdk/pydantic/video_search_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.set_new_name`<a id="shutterstockvideosset_new_name"></a>

This endpoint sets a new name for a collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shutterstock.videos.set_new_name(
    name="My collection with a new name",
    id="17555176",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The new name of the collection

##### id: `str`<a id="id-str"></a>

The ID of the collection to rename

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollectionUpdateRequest`](./shutterstock_python_sdk/type/collection_update_request.py)
The new name for the collection

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/collections/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `shutterstock.videos.video_details`<a id="shutterstockvideosvideo_details"></a>

This endpoint shows information about a video, including URLs to previews and the sizes that it is available in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
video_details_response = shutterstock.videos.video_details(
    id="639703",
    language="es",
    view="full",
    search_id="00000000-0000-0000-0000-000000000000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Video ID

##### language: [`Language`](./shutterstock_python_sdk/type/.py)<a id="language-languageshutterstock_python_sdktypepy"></a>

Language for the keywords and categories in the response

##### view: `str`<a id="view-str"></a>

Amount of detail to render in the response

##### search_id: `str`<a id="search_id-str"></a>

The ID of the search that is related to this request

#### 🔄 Return<a id="🔄-return"></a>

[`Video`](./shutterstock_python_sdk/pydantic/video.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
