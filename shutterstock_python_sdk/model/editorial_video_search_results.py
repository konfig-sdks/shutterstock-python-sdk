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


class EditorialVideoSearchResults(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Editorial search results
    """


    class MetaOapg:
        required = {
            "data",
            "total_count",
        }
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EditorialVideoContent']:
                        return EditorialVideoContent
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EditorialVideoContent'], typing.List['EditorialVideoContent']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EditorialVideoContent':
                    return super().__getitem__(i)
            total_count = schemas.IntSchema
            message = schemas.StrSchema
            next = schemas.StrSchema
            page = schemas.IntSchema
            per_page = schemas.IntSchema
            prev = schemas.StrSchema
            search_id = schemas.StrSchema
            __annotations__ = {
                "data": data,
                "total_count": total_count,
                "message": message,
                "next": next,
                "page": page,
                "per_page": per_page,
                "prev": prev,
                "search_id": search_id,
            }
    
    data: MetaOapg.properties.data
    total_count: MetaOapg.properties.total_count
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next"]) -> MetaOapg.properties.next: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_page"]) -> MetaOapg.properties.per_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prev"]) -> MetaOapg.properties.prev: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["search_id"]) -> MetaOapg.properties.search_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "total_count", "message", "next", "page", "per_page", "prev", "search_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next"]) -> typing.Union[MetaOapg.properties.next, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_page"]) -> typing.Union[MetaOapg.properties.per_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prev"]) -> typing.Union[MetaOapg.properties.prev, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["search_id"]) -> typing.Union[MetaOapg.properties.search_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "total_count", "message", "next", "page", "per_page", "prev", "search_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, ],
        total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        next: typing.Union[MetaOapg.properties.next, str, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        per_page: typing.Union[MetaOapg.properties.per_page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        prev: typing.Union[MetaOapg.properties.prev, str, schemas.Unset] = schemas.unset,
        search_id: typing.Union[MetaOapg.properties.search_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditorialVideoSearchResults':
        return super().__new__(
            cls,
            *args,
            data=data,
            total_count=total_count,
            message=message,
            next=next,
            page=page,
            per_page=per_page,
            prev=prev,
            search_id=search_id,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.editorial_video_content import EditorialVideoContent
