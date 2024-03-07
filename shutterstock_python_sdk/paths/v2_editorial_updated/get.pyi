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

from shutterstock_python_sdk.model.editorial_updated_results import EditorialUpdatedResults as EditorialUpdatedResultsSchema

from shutterstock_python_sdk.type.editorial_updated_results import EditorialUpdatedResults

from ...api_client import Dictionary
from shutterstock_python_sdk.pydantic.editorial_updated_results import EditorialUpdatedResults as EditorialUpdatedResultsPydantic

# Query params


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def EDIT(cls):
        return cls("edit")
    
    @schemas.classproperty
    def ADDITION(cls):
        return cls("addition")
DateUpdatedStartSchema = schemas.DateTimeSchema
DateUpdatedEndSchema = schemas.DateTimeSchema
DateTakenStartSchema = schemas.DateSchema
DateTakenEndSchema = schemas.DateSchema
CursorSchema = schemas.StrSchema


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def NEWEST(cls):
        return cls("newest")
    
    @schemas.classproperty
    def OLDEST(cls):
        return cls("oldest")


class SupplierCodeSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.StrSchema
        ):
            pass

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SupplierCodeSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
CountrySchema = schemas.StrSchema


class PerPageSchema(
    schemas.IntSchema
):
    pass
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'type': typing.Union[TypeSchema, str, ],
        'date_updated_start': typing.Union[DateUpdatedStartSchema, str, datetime, ],
        'date_updated_end': typing.Union[DateUpdatedEndSchema, str, datetime, ],
        'country': typing.Union[CountrySchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'date_taken_start': typing.Union[DateTakenStartSchema, str, date, ],
        'date_taken_end': typing.Union[DateTakenEndSchema, str, date, ],
        'cursor': typing.Union[CursorSchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
        'supplier_code': typing.Union[SupplierCodeSchema, list, tuple, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    required=True,
    explode=True,
)
request_query_date_updated_start = api_client.QueryParameter(
    name="date_updated_start",
    style=api_client.ParameterStyle.FORM,
    schema=DateUpdatedStartSchema,
    required=True,
    explode=True,
)
request_query_date_updated_end = api_client.QueryParameter(
    name="date_updated_end",
    style=api_client.ParameterStyle.FORM,
    schema=DateUpdatedEndSchema,
    required=True,
    explode=True,
)
request_query_date_taken_start = api_client.QueryParameter(
    name="date_taken_start",
    style=api_client.ParameterStyle.FORM,
    schema=DateTakenStartSchema,
    explode=True,
)
request_query_date_taken_end = api_client.QueryParameter(
    name="date_taken_end",
    style=api_client.ParameterStyle.FORM,
    schema=DateTakenEndSchema,
    explode=True,
)
request_query_cursor = api_client.QueryParameter(
    name="cursor",
    style=api_client.ParameterStyle.FORM,
    schema=CursorSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_supplier_code = api_client.QueryParameter(
    name="supplier_code",
    style=api_client.ParameterStyle.FORM,
    schema=SupplierCodeSchema,
    explode=True,
)
request_query_country = api_client.QueryParameter(
    name="country",
    style=api_client.ParameterStyle.FORM,
    schema=CountrySchema,
    required=True,
    explode=True,
)
request_query_per_page = api_client.QueryParameter(
    name="per_page",
    style=api_client.ParameterStyle.FORM,
    schema=PerPageSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = EditorialUpdatedResultsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EditorialUpdatedResults


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EditorialUpdatedResults


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_updated_content_0_mapped_args(
        self,
        type: str,
        date_updated_start: datetime,
        date_updated_end: datetime,
        country: str,
        date_taken_start: typing.Optional[date] = None,
        date_taken_end: typing.Optional[date] = None,
        cursor: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        supplier_code: typing.Optional[typing.List[str]] = None,
        per_page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if type is not None:
            _query_params["type"] = type
        if date_updated_start is not None:
            _query_params["date_updated_start"] = date_updated_start
        if date_updated_end is not None:
            _query_params["date_updated_end"] = date_updated_end
        if date_taken_start is not None:
            _query_params["date_taken_start"] = date_taken_start
        if date_taken_end is not None:
            _query_params["date_taken_end"] = date_taken_end
        if cursor is not None:
            _query_params["cursor"] = cursor
        if sort is not None:
            _query_params["sort"] = sort
        if supplier_code is not None:
            _query_params["supplier_code"] = supplier_code
        if country is not None:
            _query_params["country"] = country
        if per_page is not None:
            _query_params["per_page"] = per_page
        args.query = _query_params
        return args

    async def _alist_updated_content_0_oapg(
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
        (Deprecated) List updated content
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_type,
            request_query_date_updated_start,
            request_query_date_updated_end,
            request_query_date_taken_start,
            request_query_date_taken_end,
            request_query_cursor,
            request_query_sort,
            request_query_supplier_code,
            request_query_country,
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
            path_template='/v2/editorial/updated',
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


    def _list_updated_content_0_oapg(
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
        (Deprecated) List updated content
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_type,
            request_query_date_updated_start,
            request_query_date_updated_end,
            request_query_date_taken_start,
            request_query_date_taken_end,
            request_query_cursor,
            request_query_sort,
            request_query_supplier_code,
            request_query_country,
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
            path_template='/v2/editorial/updated',
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


class ListUpdatedContent0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    async def alist_updated_content_0(
        self,
        type: str,
        date_updated_start: datetime,
        date_updated_end: datetime,
        country: str,
        date_taken_start: typing.Optional[date] = None,
        date_taken_end: typing.Optional[date] = None,
        cursor: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        supplier_code: typing.Optional[typing.List[str]] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_updated_content_0_mapped_args(
            type=type,
            date_updated_start=date_updated_start,
            date_updated_end=date_updated_end,
            country=country,
            date_taken_start=date_taken_start,
            date_taken_end=date_taken_end,
            cursor=cursor,
            sort=sort,
            supplier_code=supplier_code,
            per_page=per_page,
        )
        return await self._alist_updated_content_0_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    def list_updated_content_0(
        self,
        type: str,
        date_updated_start: datetime,
        date_updated_end: datetime,
        country: str,
        date_taken_start: typing.Optional[date] = None,
        date_taken_end: typing.Optional[date] = None,
        cursor: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        supplier_code: typing.Optional[typing.List[str]] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_updated_content_0_mapped_args(
            type=type,
            date_updated_start=date_updated_start,
            date_updated_end=date_updated_end,
            country=country,
            date_taken_start=date_taken_start,
            date_taken_end=date_taken_end,
            cursor=cursor,
            sort=sort,
            supplier_code=supplier_code,
            per_page=per_page,
        )
        return self._list_updated_content_0_oapg(
            query_params=args.query,
        )

class ListUpdatedContent0(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    async def alist_updated_content_0(
        self,
        type: str,
        date_updated_start: datetime,
        date_updated_end: datetime,
        country: str,
        date_taken_start: typing.Optional[date] = None,
        date_taken_end: typing.Optional[date] = None,
        cursor: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        supplier_code: typing.Optional[typing.List[str]] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> EditorialUpdatedResultsPydantic:
        raw_response = await self.raw.alist_updated_content_0(
            type=type,
            date_updated_start=date_updated_start,
            date_updated_end=date_updated_end,
            country=country,
            date_taken_start=date_taken_start,
            date_taken_end=date_taken_end,
            cursor=cursor,
            sort=sort,
            supplier_code=supplier_code,
            per_page=per_page,
            **kwargs,
        )
        if validate:
            return EditorialUpdatedResultsPydantic(**raw_response.body)
        return api_client.construct_model_instance(EditorialUpdatedResultsPydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    def list_updated_content_0(
        self,
        type: str,
        date_updated_start: datetime,
        date_updated_end: datetime,
        country: str,
        date_taken_start: typing.Optional[date] = None,
        date_taken_end: typing.Optional[date] = None,
        cursor: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        supplier_code: typing.Optional[typing.List[str]] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> EditorialUpdatedResultsPydantic:
        raw_response = self.raw.list_updated_content_0(
            type=type,
            date_updated_start=date_updated_start,
            date_updated_end=date_updated_end,
            country=country,
            date_taken_start=date_taken_start,
            date_taken_end=date_taken_end,
            cursor=cursor,
            sort=sort,
            supplier_code=supplier_code,
            per_page=per_page,
        )
        if validate:
            return EditorialUpdatedResultsPydantic(**raw_response.body)
        return api_client.construct_model_instance(EditorialUpdatedResultsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    async def aget(
        self,
        type: str,
        date_updated_start: datetime,
        date_updated_end: datetime,
        country: str,
        date_taken_start: typing.Optional[date] = None,
        date_taken_end: typing.Optional[date] = None,
        cursor: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        supplier_code: typing.Optional[typing.List[str]] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_updated_content_0_mapped_args(
            type=type,
            date_updated_start=date_updated_start,
            date_updated_end=date_updated_end,
            country=country,
            date_taken_start=date_taken_start,
            date_taken_end=date_taken_end,
            cursor=cursor,
            sort=sort,
            supplier_code=supplier_code,
            per_page=per_page,
        )
        return await self._alist_updated_content_0_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="editorial_images")
    def get(
        self,
        type: str,
        date_updated_start: datetime,
        date_updated_end: datetime,
        country: str,
        date_taken_start: typing.Optional[date] = None,
        date_taken_end: typing.Optional[date] = None,
        cursor: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        supplier_code: typing.Optional[typing.List[str]] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_updated_content_0_mapped_args(
            type=type,
            date_updated_start=date_updated_start,
            date_updated_end=date_updated_end,
            country=country,
            date_taken_start=date_taken_start,
            date_taken_end=date_taken_end,
            cursor=cursor,
            sort=sort,
            supplier_code=supplier_code,
            per_page=per_page,
        )
        return self._list_updated_content_0_oapg(
            query_params=args.query,
        )

