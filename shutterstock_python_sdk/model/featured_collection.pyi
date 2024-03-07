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


class FeaturedCollection(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Metadata about a featured collection
    """


    class MetaOapg:
        required = {
            "name",
            "id",
            "total_item_count",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            total_item_count = schemas.IntSchema
        
            @staticmethod
            def cover_item() -> typing.Type['FeaturedCollectionCoverItem']:
                return FeaturedCollectionCoverItem
            created_time = schemas.DateTimeSchema
        
            @staticmethod
            def hero_item() -> typing.Type['FeaturedCollectionCoverItem']:
                return FeaturedCollectionCoverItem
            items_updated_time = schemas.DateTimeSchema
            share_url = schemas.StrSchema
            updated_time = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "total_item_count": total_item_count,
                "cover_item": cover_item,
                "created_time": created_time,
                "hero_item": hero_item,
                "items_updated_time": items_updated_time,
                "share_url": share_url,
                "updated_time": updated_time,
            }
    
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    total_item_count: MetaOapg.properties.total_item_count
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_item_count"]) -> MetaOapg.properties.total_item_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover_item"]) -> 'FeaturedCollectionCoverItem': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_time"]) -> MetaOapg.properties.created_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hero_item"]) -> 'FeaturedCollectionCoverItem': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items_updated_time"]) -> MetaOapg.properties.items_updated_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["share_url"]) -> MetaOapg.properties.share_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_time"]) -> MetaOapg.properties.updated_time: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "total_item_count", "cover_item", "created_time", "hero_item", "items_updated_time", "share_url", "updated_time", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_item_count"]) -> MetaOapg.properties.total_item_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover_item"]) -> typing.Union['FeaturedCollectionCoverItem', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_time"]) -> typing.Union[MetaOapg.properties.created_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hero_item"]) -> typing.Union['FeaturedCollectionCoverItem', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items_updated_time"]) -> typing.Union[MetaOapg.properties.items_updated_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["share_url"]) -> typing.Union[MetaOapg.properties.share_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_time"]) -> typing.Union[MetaOapg.properties.updated_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "total_item_count", "cover_item", "created_time", "hero_item", "items_updated_time", "share_url", "updated_time", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        total_item_count: typing.Union[MetaOapg.properties.total_item_count, decimal.Decimal, int, ],
        cover_item: typing.Union['FeaturedCollectionCoverItem', schemas.Unset] = schemas.unset,
        created_time: typing.Union[MetaOapg.properties.created_time, str, datetime, schemas.Unset] = schemas.unset,
        hero_item: typing.Union['FeaturedCollectionCoverItem', schemas.Unset] = schemas.unset,
        items_updated_time: typing.Union[MetaOapg.properties.items_updated_time, str, datetime, schemas.Unset] = schemas.unset,
        share_url: typing.Union[MetaOapg.properties.share_url, str, schemas.Unset] = schemas.unset,
        updated_time: typing.Union[MetaOapg.properties.updated_time, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FeaturedCollection':
        return super().__new__(
            cls,
            *args,
            name=name,
            id=id,
            total_item_count=total_item_count,
            cover_item=cover_item,
            created_time=created_time,
            hero_item=hero_item,
            items_updated_time=items_updated_time,
            share_url=share_url,
            updated_time=updated_time,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.featured_collection_cover_item import FeaturedCollectionCoverItem