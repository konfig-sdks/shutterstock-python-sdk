# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

    The version of the OpenAPI document: 1.1.32
    Generated by: https://konfigthis.com
"""

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


class TestValidate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Validation results
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def header() -> typing.Type['TestValidateHeader']:
                return TestValidateHeader
        
            @staticmethod
            def query() -> typing.Type['TestValidateQuery']:
                return TestValidateQuery
            __annotations__ = {
                "header": header,
                "query": query,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["header"]) -> 'TestValidateHeader': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> 'TestValidateQuery': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["header", "query", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["header"]) -> typing.Union['TestValidateHeader', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union['TestValidateQuery', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["header", "query", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        header: typing.Union['TestValidateHeader', schemas.Unset] = schemas.unset,
        query: typing.Union['TestValidateQuery', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TestValidate':
        return super().__new__(
            cls,
            *args,
            header=header,
            query=query,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.test_validate_header import TestValidateHeader
from shutterstock_python_sdk.model.test_validate_query import TestValidateQuery