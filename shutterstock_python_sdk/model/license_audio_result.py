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


class LicenseAudioResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The response to a licensing request for an audio track
    """


    class MetaOapg:
        required = {
            "audio_id",
        }
        
        class properties:
            audio_id = schemas.StrSchema
            allotment_charge = schemas.NumberSchema
        
            @staticmethod
            def download() -> typing.Type['AudioUrl']:
                return AudioUrl
            error = schemas.StrSchema
            license_id = schemas.StrSchema
            __annotations__ = {
                "audio_id": audio_id,
                "allotment_charge": allotment_charge,
                "download": download,
                "error": error,
                "license_id": license_id,
            }
    
    audio_id: MetaOapg.properties.audio_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audio_id"]) -> MetaOapg.properties.audio_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allotment_charge"]) -> MetaOapg.properties.allotment_charge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["download"]) -> 'AudioUrl': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license_id"]) -> MetaOapg.properties.license_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["audio_id", "allotment_charge", "download", "error", "license_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audio_id"]) -> MetaOapg.properties.audio_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allotment_charge"]) -> typing.Union[MetaOapg.properties.allotment_charge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["download"]) -> typing.Union['AudioUrl', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license_id"]) -> typing.Union[MetaOapg.properties.license_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["audio_id", "allotment_charge", "download", "error", "license_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        audio_id: typing.Union[MetaOapg.properties.audio_id, str, ],
        allotment_charge: typing.Union[MetaOapg.properties.allotment_charge, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        download: typing.Union['AudioUrl', schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        license_id: typing.Union[MetaOapg.properties.license_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LicenseAudioResult':
        return super().__new__(
            cls,
            *args,
            audio_id=audio_id,
            allotment_charge=allotment_charge,
            download=download,
            error=error,
            license_id=license_id,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.audio_url import AudioUrl
