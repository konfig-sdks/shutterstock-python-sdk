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


class AudioRenderTimelineSpanRegion(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A period of music or silence, measured in beats
    """


    class MetaOapg:
        required = {
            "beat",
            "descriptor",
            "id",
            "region",
        }
        
        class properties:
            beat = schemas.IntSchema
            descriptor = schemas.StrSchema
            id = schemas.NumberSchema
            
            
            class region(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "music": "MUSIC",
                        "silence": "SILENCE",
                    }
                
                @schemas.classproperty
                def MUSIC(cls):
                    return cls("music")
                
                @schemas.classproperty
                def SILENCE(cls):
                    return cls("silence")
        
            @staticmethod
            def end_type() -> typing.Type['AudioRenderTimelineSpanRegionEndType']:
                return AudioRenderTimelineSpanRegionEndType
        
            @staticmethod
            def key() -> typing.Type['AudioRenderTimelineSpanRegionKey']:
                return AudioRenderTimelineSpanRegionKey
            __annotations__ = {
                "beat": beat,
                "descriptor": descriptor,
                "id": id,
                "region": region,
                "end_type": end_type,
                "key": key,
            }
    
    beat: MetaOapg.properties.beat
    descriptor: MetaOapg.properties.descriptor
    id: MetaOapg.properties.id
    region: MetaOapg.properties.region
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beat"]) -> MetaOapg.properties.beat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_type"]) -> 'AudioRenderTimelineSpanRegionEndType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> 'AudioRenderTimelineSpanRegionKey': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["beat", "descriptor", "id", "region", "end_type", "key", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beat"]) -> MetaOapg.properties.beat: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_type"]) -> typing.Union['AudioRenderTimelineSpanRegionEndType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union['AudioRenderTimelineSpanRegionKey', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["beat", "descriptor", "id", "region", "end_type", "key", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        beat: typing.Union[MetaOapg.properties.beat, decimal.Decimal, int, ],
        descriptor: typing.Union[MetaOapg.properties.descriptor, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        region: typing.Union[MetaOapg.properties.region, str, ],
        end_type: typing.Union['AudioRenderTimelineSpanRegionEndType', schemas.Unset] = schemas.unset,
        key: typing.Union['AudioRenderTimelineSpanRegionKey', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AudioRenderTimelineSpanRegion':
        return super().__new__(
            cls,
            *args,
            beat=beat,
            descriptor=descriptor,
            id=id,
            region=region,
            end_type=end_type,
            key=key,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.audio_render_timeline_span_region_end_type import AudioRenderTimelineSpanRegionEndType
from shutterstock_python_sdk.model.audio_render_timeline_span_region_key import AudioRenderTimelineSpanRegionKey
