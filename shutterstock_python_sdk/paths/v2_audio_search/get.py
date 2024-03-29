# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from shutterstock_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from shutterstock_python_sdk.api_response import AsyncGeneratorResponse
from shutterstock_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from shutterstock_python_sdk import schemas  # noqa: F401

from shutterstock_python_sdk.model.audio_search_results import AudioSearchResults as AudioSearchResultsSchema

from shutterstock_python_sdk.type.audio_search_results import AudioSearchResults

from ...api_client import Dictionary
from shutterstock_python_sdk.pydantic.audio_search_results import AudioSearchResults as AudioSearchResultsPydantic

from . import path

# Query params


class ArtistsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = False
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ArtistsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class BpmSchema(
    schemas.IntSchema
):


    class MetaOapg:


class BpmFromSchema(
    schemas.IntSchema
):


    class MetaOapg:


class BpmToSchema(
    schemas.IntSchema
):


    class MetaOapg:


class DurationSchema(
    schemas.IntSchema
):


    class MetaOapg:


class DurationFromSchema(
    schemas.IntSchema
):


    class MetaOapg:


class DurationToSchema(
    schemas.IntSchema
):


    class MetaOapg:


class GenreSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = False
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'GenreSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
IsInstrumentalSchema = schemas.BoolSchema


class InstrumentsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = False
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InstrumentsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class MoodsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = False
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MoodsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class PageSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_minimum = 1


class PerPageSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 500
        inclusive_minimum = 0


class QuerySchema(
    schemas.StrSchema
):


    class MetaOapg:


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "score": "SCORE",
            "ranking_all": "RANKING_ALL",
            "artist": "ARTIST",
            "title": "TITLE",
            "bpm": "BPM",
            "freshness": "FRESHNESS",
            "duration": "DURATION",
        }
    
    @schemas.classproperty
    def SCORE(cls):
        return cls("score")
    
    @schemas.classproperty
    def RANKING_ALL(cls):
        return cls("ranking_all")
    
    @schemas.classproperty
    def ARTIST(cls):
        return cls("artist")
    
    @schemas.classproperty
    def TITLE(cls):
        return cls("title")
    
    @schemas.classproperty
    def BPM(cls):
        return cls("bpm")
    
    @schemas.classproperty
    def FRESHNESS(cls):
        return cls("freshness")
    
    @schemas.classproperty
    def DURATION(cls):
        return cls("duration")


class SortOrderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "asc": "ASC",
            "desc": "DESC",
        }
    
    @schemas.classproperty
    def ASC(cls):
        return cls("asc")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("desc")


class VocalDescriptionSchema(
    schemas.StrSchema
):


    class MetaOapg:


class ViewSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "minimal": "MINIMAL",
            "full": "FULL",
        }
    
    @schemas.classproperty
    def MINIMAL(cls):
        return cls("minimal")
    
    @schemas.classproperty
    def FULL(cls):
        return cls("full")


class FieldsSchema(
    schemas.StrSchema
):


    class MetaOapg:


class LibrarySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "shutterstock": "SHUTTERSTOCK",
            "premier": "PREMIER",
        }
    
    @schemas.classproperty
    def SHUTTERSTOCK(cls):
        return cls("shutterstock")
    
    @schemas.classproperty
    def PREMIER(cls):
        return cls("premier")
LanguageSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'artists': typing.Union[ArtistsSchema, list, tuple, ],
        'bpm': typing.Union[BpmSchema, decimal.Decimal, int, ],
        'bpm_from': typing.Union[BpmFromSchema, decimal.Decimal, int, ],
        'bpm_to': typing.Union[BpmToSchema, decimal.Decimal, int, ],
        'duration': typing.Union[DurationSchema, decimal.Decimal, int, ],
        'duration_from': typing.Union[DurationFromSchema, decimal.Decimal, int, ],
        'duration_to': typing.Union[DurationToSchema, decimal.Decimal, int, ],
        'genre': typing.Union[GenreSchema, list, tuple, ],
        'is_instrumental': typing.Union[IsInstrumentalSchema, bool, ],
        'instruments': typing.Union[InstrumentsSchema, list, tuple, ],
        'moods': typing.Union[MoodsSchema, list, tuple, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, ],
        'query': typing.Union[QuerySchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
        'sort_order': typing.Union[SortOrderSchema, str, ],
        'vocal_description': typing.Union[VocalDescriptionSchema, str, ],
        'view': typing.Union[ViewSchema, str, ],
        'fields': typing.Union[FieldsSchema, str, ],
        'library': typing.Union[LibrarySchema, str, ],
        'language': typing.Union[LanguageSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_artists = api_client.QueryParameter(
    name="artists",
    style=api_client.ParameterStyle.FORM,
    schema=ArtistsSchema,
    explode=True,
)
request_query_bpm = api_client.QueryParameter(
    name="bpm",
    style=api_client.ParameterStyle.FORM,
    schema=BpmSchema,
    explode=True,
)
request_query_bpm_from = api_client.QueryParameter(
    name="bpm_from",
    style=api_client.ParameterStyle.FORM,
    schema=BpmFromSchema,
    explode=True,
)
request_query_bpm_to = api_client.QueryParameter(
    name="bpm_to",
    style=api_client.ParameterStyle.FORM,
    schema=BpmToSchema,
    explode=True,
)
request_query_duration = api_client.QueryParameter(
    name="duration",
    style=api_client.ParameterStyle.FORM,
    schema=DurationSchema,
    explode=True,
)
request_query_duration_from = api_client.QueryParameter(
    name="duration_from",
    style=api_client.ParameterStyle.FORM,
    schema=DurationFromSchema,
    explode=True,
)
request_query_duration_to = api_client.QueryParameter(
    name="duration_to",
    style=api_client.ParameterStyle.FORM,
    schema=DurationToSchema,
    explode=True,
)
request_query_genre = api_client.QueryParameter(
    name="genre",
    style=api_client.ParameterStyle.FORM,
    schema=GenreSchema,
    explode=True,
)
request_query_is_instrumental = api_client.QueryParameter(
    name="is_instrumental",
    style=api_client.ParameterStyle.FORM,
    schema=IsInstrumentalSchema,
    explode=True,
)
request_query_instruments = api_client.QueryParameter(
    name="instruments",
    style=api_client.ParameterStyle.FORM,
    schema=InstrumentsSchema,
    explode=True,
)
request_query_moods = api_client.QueryParameter(
    name="moods",
    style=api_client.ParameterStyle.FORM,
    schema=MoodsSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_per_page = api_client.QueryParameter(
    name="per_page",
    style=api_client.ParameterStyle.FORM,
    schema=PerPageSchema,
    explode=True,
)
request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_sort_order = api_client.QueryParameter(
    name="sort_order",
    style=api_client.ParameterStyle.FORM,
    schema=SortOrderSchema,
    explode=True,
)
request_query_vocal_description = api_client.QueryParameter(
    name="vocal_description",
    style=api_client.ParameterStyle.FORM,
    schema=VocalDescriptionSchema,
    explode=True,
)
request_query_view = api_client.QueryParameter(
    name="view",
    style=api_client.ParameterStyle.FORM,
    schema=ViewSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_library = api_client.QueryParameter(
    name="library",
    style=api_client.ParameterStyle.FORM,
    schema=LibrarySchema,
    explode=True,
)
request_query_language = api_client.QueryParameter(
    name="language",
    style=api_client.ParameterStyle.FORM,
    schema=LanguageSchema,
    explode=True,
)
_auth = [
    'basic',
    'customer_accessCode',
]
SchemaFor200ResponseBodyApplicationJson = AudioSearchResultsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AudioSearchResults


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AudioSearchResults


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _search_tracks_mapped_args(
        self,
        artists: typing.Optional[typing.List[str]] = None,
        bpm: typing.Optional[int] = None,
        bpm_from: typing.Optional[int] = None,
        bpm_to: typing.Optional[int] = None,
        duration: typing.Optional[int] = None,
        duration_from: typing.Optional[int] = None,
        duration_to: typing.Optional[int] = None,
        genre: typing.Optional[typing.List[str]] = None,
        is_instrumental: typing.Optional[bool] = None,
        instruments: typing.Optional[typing.List[str]] = None,
        moods: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        vocal_description: typing.Optional[str] = None,
        view: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        library: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if artists is not None:
            _query_params["artists"] = artists
        if bpm is not None:
            _query_params["bpm"] = bpm
        if bpm_from is not None:
            _query_params["bpm_from"] = bpm_from
        if bpm_to is not None:
            _query_params["bpm_to"] = bpm_to
        if duration is not None:
            _query_params["duration"] = duration
        if duration_from is not None:
            _query_params["duration_from"] = duration_from
        if duration_to is not None:
            _query_params["duration_to"] = duration_to
        if genre is not None:
            _query_params["genre"] = genre
        if is_instrumental is not None:
            _query_params["is_instrumental"] = is_instrumental
        if instruments is not None:
            _query_params["instruments"] = instruments
        if moods is not None:
            _query_params["moods"] = moods
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        if query is not None:
            _query_params["query"] = query
        if sort is not None:
            _query_params["sort"] = sort
        if sort_order is not None:
            _query_params["sort_order"] = sort_order
        if vocal_description is not None:
            _query_params["vocal_description"] = vocal_description
        if view is not None:
            _query_params["view"] = view
        if fields is not None:
            _query_params["fields"] = fields
        if library is not None:
            _query_params["library"] = library
        if language is not None:
            _query_params["language"] = language
        args.query = _query_params
        return args

    async def _asearch_tracks_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Search for tracks
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_artists,
            request_query_bpm,
            request_query_bpm_from,
            request_query_bpm_to,
            request_query_duration,
            request_query_duration_from,
            request_query_duration_to,
            request_query_genre,
            request_query_is_instrumental,
            request_query_instruments,
            request_query_moods,
            request_query_page,
            request_query_per_page,
            request_query_query,
            request_query_sort,
            request_query_sort_order,
            request_query_vocal_description,
            request_query_view,
            request_query_fields,
            request_query_library,
            request_query_language,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/audio/search',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _search_tracks_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Search for tracks
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_artists,
            request_query_bpm,
            request_query_bpm_from,
            request_query_bpm_to,
            request_query_duration,
            request_query_duration_from,
            request_query_duration_to,
            request_query_genre,
            request_query_is_instrumental,
            request_query_instruments,
            request_query_moods,
            request_query_page,
            request_query_per_page,
            request_query_query,
            request_query_sort,
            request_query_sort_order,
            request_query_vocal_description,
            request_query_view,
            request_query_fields,
            request_query_library,
            request_query_language,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/audio/search',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class SearchTracksRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_tracks(
        self,
        artists: typing.Optional[typing.List[str]] = None,
        bpm: typing.Optional[int] = None,
        bpm_from: typing.Optional[int] = None,
        bpm_to: typing.Optional[int] = None,
        duration: typing.Optional[int] = None,
        duration_from: typing.Optional[int] = None,
        duration_to: typing.Optional[int] = None,
        genre: typing.Optional[typing.List[str]] = None,
        is_instrumental: typing.Optional[bool] = None,
        instruments: typing.Optional[typing.List[str]] = None,
        moods: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        vocal_description: typing.Optional[str] = None,
        view: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        library: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_tracks_mapped_args(
            artists=artists,
            bpm=bpm,
            bpm_from=bpm_from,
            bpm_to=bpm_to,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            genre=genre,
            is_instrumental=is_instrumental,
            instruments=instruments,
            moods=moods,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            sort_order=sort_order,
            vocal_description=vocal_description,
            view=view,
            fields=fields,
            library=library,
            language=language,
        )
        return await self._asearch_tracks_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def search_tracks(
        self,
        artists: typing.Optional[typing.List[str]] = None,
        bpm: typing.Optional[int] = None,
        bpm_from: typing.Optional[int] = None,
        bpm_to: typing.Optional[int] = None,
        duration: typing.Optional[int] = None,
        duration_from: typing.Optional[int] = None,
        duration_to: typing.Optional[int] = None,
        genre: typing.Optional[typing.List[str]] = None,
        is_instrumental: typing.Optional[bool] = None,
        instruments: typing.Optional[typing.List[str]] = None,
        moods: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        vocal_description: typing.Optional[str] = None,
        view: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        library: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_tracks_mapped_args(
            artists=artists,
            bpm=bpm,
            bpm_from=bpm_from,
            bpm_to=bpm_to,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            genre=genre,
            is_instrumental=is_instrumental,
            instruments=instruments,
            moods=moods,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            sort_order=sort_order,
            vocal_description=vocal_description,
            view=view,
            fields=fields,
            library=library,
            language=language,
        )
        return self._search_tracks_oapg(
            query_params=args.query,
        )

class SearchTracks(BaseApi):

    async def asearch_tracks(
        self,
        artists: typing.Optional[typing.List[str]] = None,
        bpm: typing.Optional[int] = None,
        bpm_from: typing.Optional[int] = None,
        bpm_to: typing.Optional[int] = None,
        duration: typing.Optional[int] = None,
        duration_from: typing.Optional[int] = None,
        duration_to: typing.Optional[int] = None,
        genre: typing.Optional[typing.List[str]] = None,
        is_instrumental: typing.Optional[bool] = None,
        instruments: typing.Optional[typing.List[str]] = None,
        moods: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        vocal_description: typing.Optional[str] = None,
        view: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        library: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AudioSearchResultsPydantic:
        raw_response = await self.raw.asearch_tracks(
            artists=artists,
            bpm=bpm,
            bpm_from=bpm_from,
            bpm_to=bpm_to,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            genre=genre,
            is_instrumental=is_instrumental,
            instruments=instruments,
            moods=moods,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            sort_order=sort_order,
            vocal_description=vocal_description,
            view=view,
            fields=fields,
            library=library,
            language=language,
            **kwargs,
        )
        if validate:
            return AudioSearchResultsPydantic(**raw_response.body)
        return api_client.construct_model_instance(AudioSearchResultsPydantic, raw_response.body)
    
    
    def search_tracks(
        self,
        artists: typing.Optional[typing.List[str]] = None,
        bpm: typing.Optional[int] = None,
        bpm_from: typing.Optional[int] = None,
        bpm_to: typing.Optional[int] = None,
        duration: typing.Optional[int] = None,
        duration_from: typing.Optional[int] = None,
        duration_to: typing.Optional[int] = None,
        genre: typing.Optional[typing.List[str]] = None,
        is_instrumental: typing.Optional[bool] = None,
        instruments: typing.Optional[typing.List[str]] = None,
        moods: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        vocal_description: typing.Optional[str] = None,
        view: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        library: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AudioSearchResultsPydantic:
        raw_response = self.raw.search_tracks(
            artists=artists,
            bpm=bpm,
            bpm_from=bpm_from,
            bpm_to=bpm_to,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            genre=genre,
            is_instrumental=is_instrumental,
            instruments=instruments,
            moods=moods,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            sort_order=sort_order,
            vocal_description=vocal_description,
            view=view,
            fields=fields,
            library=library,
            language=language,
        )
        if validate:
            return AudioSearchResultsPydantic(**raw_response.body)
        return api_client.construct_model_instance(AudioSearchResultsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        artists: typing.Optional[typing.List[str]] = None,
        bpm: typing.Optional[int] = None,
        bpm_from: typing.Optional[int] = None,
        bpm_to: typing.Optional[int] = None,
        duration: typing.Optional[int] = None,
        duration_from: typing.Optional[int] = None,
        duration_to: typing.Optional[int] = None,
        genre: typing.Optional[typing.List[str]] = None,
        is_instrumental: typing.Optional[bool] = None,
        instruments: typing.Optional[typing.List[str]] = None,
        moods: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        vocal_description: typing.Optional[str] = None,
        view: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        library: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_tracks_mapped_args(
            artists=artists,
            bpm=bpm,
            bpm_from=bpm_from,
            bpm_to=bpm_to,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            genre=genre,
            is_instrumental=is_instrumental,
            instruments=instruments,
            moods=moods,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            sort_order=sort_order,
            vocal_description=vocal_description,
            view=view,
            fields=fields,
            library=library,
            language=language,
        )
        return await self._asearch_tracks_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        artists: typing.Optional[typing.List[str]] = None,
        bpm: typing.Optional[int] = None,
        bpm_from: typing.Optional[int] = None,
        bpm_to: typing.Optional[int] = None,
        duration: typing.Optional[int] = None,
        duration_from: typing.Optional[int] = None,
        duration_to: typing.Optional[int] = None,
        genre: typing.Optional[typing.List[str]] = None,
        is_instrumental: typing.Optional[bool] = None,
        instruments: typing.Optional[typing.List[str]] = None,
        moods: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        vocal_description: typing.Optional[str] = None,
        view: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        library: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_tracks_mapped_args(
            artists=artists,
            bpm=bpm,
            bpm_from=bpm_from,
            bpm_to=bpm_to,
            duration=duration,
            duration_from=duration_from,
            duration_to=duration_to,
            genre=genre,
            is_instrumental=is_instrumental,
            instruments=instruments,
            moods=moods,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            sort_order=sort_order,
            vocal_description=vocal_description,
            view=view,
            fields=fields,
            library=library,
            language=language,
        )
        return self._search_tracks_oapg(
            query_params=args.query,
        )

