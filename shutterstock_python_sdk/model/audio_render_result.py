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


class AudioRenderResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The output of an audio render in WAV or MP3 format
    """


    class MetaOapg:
        required = {
            "timeline",
            "id",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "WAITING_COMPOSE": "WAITING_COMPOSE",
                        "RUNNING_COMPOSE": "RUNNING_COMPOSE",
                        "WAITING_RENDER": "WAITING_RENDER",
                        "RUNNING_RENDER": "RUNNING_RENDER",
                        "CREATED": "CREATED",
                        "FAILED_CREATE": "FAILED_CREATE",
                    }
                
                @schemas.classproperty
                def WAITING_COMPOSE(cls):
                    return cls("WAITING_COMPOSE")
                
                @schemas.classproperty
                def RUNNING_COMPOSE(cls):
                    return cls("RUNNING_COMPOSE")
                
                @schemas.classproperty
                def WAITING_RENDER(cls):
                    return cls("WAITING_RENDER")
                
                @schemas.classproperty
                def RUNNING_RENDER(cls):
                    return cls("RUNNING_RENDER")
                
                @schemas.classproperty
                def CREATED(cls):
                    return cls("CREATED")
                
                @schemas.classproperty
                def FAILED_CREATE(cls):
                    return cls("FAILED_CREATE")
        
            @staticmethod
            def timeline() -> typing.Type['AudioRenderTimeline']:
                return AudioRenderTimeline
            created_date = schemas.DateTimeSchema
            
            
            class files(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AudioRendersFilesList']:
                        return AudioRendersFilesList
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AudioRendersFilesList'], typing.List['AudioRendersFilesList']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'files':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AudioRendersFilesList':
                    return super().__getitem__(i)
            
            
            class preset(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "MASTER_MP3": "MASTER_MP3",
                        "MASTER_WAV": "MASTER_WAV",
                        "STEMS_WAV": "STEMS_WAV",
                    }
                
                @schemas.classproperty
                def MASTER_MP3(cls):
                    return cls("MASTER_MP3")
                
                @schemas.classproperty
                def MASTER_WAV(cls):
                    return cls("MASTER_WAV")
                
                @schemas.classproperty
                def STEMS_WAV(cls):
                    return cls("STEMS_WAV")
            progress_percent = schemas.IntSchema
            updated_date = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "status": status,
                "timeline": timeline,
                "created_date": created_date,
                "files": files,
                "preset": preset,
                "progress_percent": progress_percent,
                "updated_date": updated_date,
            }
    
    timeline: 'AudioRenderTimeline'
    id: MetaOapg.properties.id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeline"]) -> 'AudioRenderTimeline': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_date"]) -> MetaOapg.properties.created_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preset"]) -> MetaOapg.properties.preset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["progress_percent"]) -> MetaOapg.properties.progress_percent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_date"]) -> MetaOapg.properties.updated_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "status", "timeline", "created_date", "files", "preset", "progress_percent", "updated_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeline"]) -> 'AudioRenderTimeline': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_date"]) -> typing.Union[MetaOapg.properties.created_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> typing.Union[MetaOapg.properties.files, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preset"]) -> typing.Union[MetaOapg.properties.preset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["progress_percent"]) -> typing.Union[MetaOapg.properties.progress_percent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_date"]) -> typing.Union[MetaOapg.properties.updated_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "status", "timeline", "created_date", "files", "preset", "progress_percent", "updated_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        timeline: 'AudioRenderTimeline',
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        created_date: typing.Union[MetaOapg.properties.created_date, str, datetime, schemas.Unset] = schemas.unset,
        files: typing.Union[MetaOapg.properties.files, list, tuple, schemas.Unset] = schemas.unset,
        preset: typing.Union[MetaOapg.properties.preset, str, schemas.Unset] = schemas.unset,
        progress_percent: typing.Union[MetaOapg.properties.progress_percent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updated_date: typing.Union[MetaOapg.properties.updated_date, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AudioRenderResult':
        return super().__new__(
            cls,
            *args,
            timeline=timeline,
            id=id,
            status=status,
            created_date=created_date,
            files=files,
            preset=preset,
            progress_percent=progress_percent,
            updated_date=updated_date,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.audio_render_timeline import AudioRenderTimeline
from shutterstock_python_sdk.model.audio_renders_files_list import AudioRendersFilesList
