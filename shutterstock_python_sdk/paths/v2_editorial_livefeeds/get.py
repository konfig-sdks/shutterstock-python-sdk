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

from shutterstock_python_sdk.model.editorial_livefeed_list import EditorialLivefeedList as EditorialLivefeedListSchema

from shutterstock_python_sdk.type.editorial_livefeed_list import EditorialLivefeedList

from ...api_client import Dictionary
from shutterstock_python_sdk.pydantic.editorial_livefeed_list import EditorialLivefeedList as EditorialLivefeedListPydantic

from . import path

# Query params
CountrySchema = schemas.StrSchema


class PageSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_minimum = 1


class PerPageSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 50
        inclusive_minimum = 1
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'country': typing.Union[CountrySchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_country = api_client.QueryParameter(
    name="country",
    style=api_client.ParameterStyle.FORM,
    schema=CountrySchema,
    required=True,
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
_auth = [
    'basic',
    'customer_accessCode',
]
SchemaFor200ResponseBodyApplicationJson = EditorialLivefeedListSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EditorialLivefeedList


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EditorialLivefeedList


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


@dataclass
class ApiResponseFor406(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor406Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_406 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor406,
    response_cls_async=ApiResponseFor406Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '406': _response_for_406,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_livefeed_list_mapped_args(
        self,
        country: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if country is not None:
            _query_params["country"] = country
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        args.query = _query_params
        return args

    async def _aget_livefeed_list_oapg(
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
        (Deprecated) Get editorial livefeed list
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_country,
            request_query_page,
            request_query_per_page,
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
            path_template='/v2/editorial/livefeeds',
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


    def _get_livefeed_list_oapg(
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
        (Deprecated) Get editorial livefeed list
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_country,
            request_query_page,
            request_query_per_page,
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
            path_template='/v2/editorial/livefeeds',
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


class GetLivefeedListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    async def aget_livefeed_list(
        self,
        country: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_livefeed_list_mapped_args(
            country=country,
            page=page,
            per_page=per_page,
        )
        return await self._aget_livefeed_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    def get_livefeed_list(
        self,
        country: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_livefeed_list_mapped_args(
            country=country,
            page=page,
            per_page=per_page,
        )
        return self._get_livefeed_list_oapg(
            query_params=args.query,
        )

class GetLivefeedList(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    async def aget_livefeed_list(
        self,
        country: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> EditorialLivefeedListPydantic:
        raw_response = await self.raw.aget_livefeed_list(
            country=country,
            page=page,
            per_page=per_page,
            **kwargs,
        )
        if validate:
            return EditorialLivefeedListPydantic(**raw_response.body)
        return api_client.construct_model_instance(EditorialLivefeedListPydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    def get_livefeed_list(
        self,
        country: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> EditorialLivefeedListPydantic:
        raw_response = self.raw.get_livefeed_list(
            country=country,
            page=page,
            per_page=per_page,
        )
        if validate:
            return EditorialLivefeedListPydantic(**raw_response.body)
        return api_client.construct_model_instance(EditorialLivefeedListPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    async def aget(
        self,
        country: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_livefeed_list_mapped_args(
            country=country,
            page=page,
            per_page=per_page,
        )
        return await self._aget_livefeed_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    def get(
        self,
        country: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_livefeed_list_mapped_args(
            country=country,
            page=page,
            per_page=per_page,
        )
        return self._get_livefeed_list_oapg(
            query_params=args.query,
        )

