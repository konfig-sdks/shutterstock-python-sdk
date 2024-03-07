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


class AudioRenderTimelineSpanRegionKey(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The key signature active at the beginning of the region
    """


    class MetaOapg:
        
        class properties:
            
            
            class tonic_accidental(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "double flat": "DOUBLE_FLAT",
                        "flat": "FLAT",
                        "natural": "NATURAL",
                        "sharp": "SHARP",
                        "double sharp": "DOUBLE_SHARP",
                    }
                
                @schemas.classproperty
                def DOUBLE_FLAT(cls):
                    return cls("double flat")
                
                @schemas.classproperty
                def FLAT(cls):
                    return cls("flat")
                
                @schemas.classproperty
                def NATURAL(cls):
                    return cls("natural")
                
                @schemas.classproperty
                def SHARP(cls):
                    return cls("sharp")
                
                @schemas.classproperty
                def DOUBLE_SHARP(cls):
                    return cls("double sharp")
            
            
            class tonic_note(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "c": "C",
                        "d": "D",
                        "e": "E",
                        "f": "F",
                        "g": "G",
                        "a": "A",
                        "b": "B",
                    }
                
                @schemas.classproperty
                def C(cls):
                    return cls("c")
                
                @schemas.classproperty
                def D(cls):
                    return cls("d")
                
                @schemas.classproperty
                def E(cls):
                    return cls("e")
                
                @schemas.classproperty
                def F(cls):
                    return cls("f")
                
                @schemas.classproperty
                def G(cls):
                    return cls("g")
                
                @schemas.classproperty
                def A(cls):
                    return cls("a")
                
                @schemas.classproperty
                def B(cls):
                    return cls("b")
            
            
            class tonic_quality(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "major": "MAJOR",
                        "natural_minor": "NATURAL_MINOR",
                        "harmonic_minor": "HARMONIC_MINOR",
                        "melodic_minor": "MELODIC_MINOR",
                        "ionian": "IONIAN",
                        "dorian": "DORIAN",
                        "phrygian": "PHRYGIAN",
                        "lydian": "LYDIAN",
                        "mixolydian": "MIXOLYDIAN",
                        "aeolian": "AEOLIAN",
                        "locrian": "LOCRIAN",
                    }
                
                @schemas.classproperty
                def MAJOR(cls):
                    return cls("major")
                
                @schemas.classproperty
                def NATURAL_MINOR(cls):
                    return cls("natural_minor")
                
                @schemas.classproperty
                def HARMONIC_MINOR(cls):
                    return cls("harmonic_minor")
                
                @schemas.classproperty
                def MELODIC_MINOR(cls):
                    return cls("melodic_minor")
                
                @schemas.classproperty
                def IONIAN(cls):
                    return cls("ionian")
                
                @schemas.classproperty
                def DORIAN(cls):
                    return cls("dorian")
                
                @schemas.classproperty
                def PHRYGIAN(cls):
                    return cls("phrygian")
                
                @schemas.classproperty
                def LYDIAN(cls):
                    return cls("lydian")
                
                @schemas.classproperty
                def MIXOLYDIAN(cls):
                    return cls("mixolydian")
                
                @schemas.classproperty
                def AEOLIAN(cls):
                    return cls("aeolian")
                
                @schemas.classproperty
                def LOCRIAN(cls):
                    return cls("locrian")
            __annotations__ = {
                "tonic_accidental": tonic_accidental,
                "tonic_note": tonic_note,
                "tonic_quality": tonic_quality,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tonic_accidental"]) -> MetaOapg.properties.tonic_accidental: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tonic_note"]) -> MetaOapg.properties.tonic_note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tonic_quality"]) -> MetaOapg.properties.tonic_quality: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tonic_accidental", "tonic_note", "tonic_quality", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tonic_accidental"]) -> typing.Union[MetaOapg.properties.tonic_accidental, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tonic_note"]) -> typing.Union[MetaOapg.properties.tonic_note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tonic_quality"]) -> typing.Union[MetaOapg.properties.tonic_quality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tonic_accidental", "tonic_note", "tonic_quality", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tonic_accidental: typing.Union[MetaOapg.properties.tonic_accidental, str, schemas.Unset] = schemas.unset,
        tonic_note: typing.Union[MetaOapg.properties.tonic_note, str, schemas.Unset] = schemas.unset,
        tonic_quality: typing.Union[MetaOapg.properties.tonic_quality, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AudioRenderTimelineSpanRegionKey':
        return super().__new__(
            cls,
            *args,
            tonic_accidental=tonic_accidental,
            tonic_note=tonic_note,
            tonic_quality=tonic_quality,
            _configuration=_configuration,
            **kwargs,
        )
