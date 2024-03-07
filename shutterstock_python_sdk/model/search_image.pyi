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


class SearchImage(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Data required to search for an image
    """


    class MetaOapg:
        
        class properties:
            added_date = schemas.DateSchema
            added_date_end = schemas.DateSchema
            added_date_start = schemas.DateSchema
            aspect_ratio = schemas.NumberSchema
            
            
            class aspect_ratio_max(
                schemas.NumberSchema
            ):
                pass
            
            
            class aspect_ratio_min(
                schemas.NumberSchema
            ):
                pass
            authentic = schemas.BoolSchema
            category = schemas.StrSchema
            color = schemas.StrSchema
        
            @staticmethod
            def contributor() -> typing.Type['SearchImageContributor']:
                return SearchImageContributor
            
            
            class contributor_country(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class one_of_0(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_0':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class one_of_1(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_1':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'contributor_country':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class fields(
                schemas.StrSchema
            ):
                pass
            height = schemas.IntSchema
            height_from = schemas.IntSchema
            height_to = schemas.IntSchema
        
            @staticmethod
            def image_type() -> typing.Type['SearchImageImageType']:
                return SearchImageImageType
            keyword_safe_search = schemas.BoolSchema
        
            @staticmethod
            def language() -> typing.Type['Language']:
                return Language
        
            @staticmethod
            def license() -> typing.Type['SearchImageLicense']:
                return SearchImageLicense
        
            @staticmethod
            def model() -> typing.Type['SearchImageModel']:
                return SearchImageModel
            
            
            class orientation(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def HORIZONTAL(cls):
                    return cls("horizontal")
                
                @schemas.classproperty
                def VERTICAL(cls):
                    return cls("vertical")
            
            
            class page(
                schemas.IntSchema
            ):
                pass
            
            
            class people_age(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INFANTS(cls):
                    return cls("infants")
                
                @schemas.classproperty
                def CHILDREN(cls):
                    return cls("children")
                
                @schemas.classproperty
                def TEENAGERS(cls):
                    return cls("teenagers")
                
                @schemas.classproperty
                def _20S(cls):
                    return cls("20s")
                
                @schemas.classproperty
                def _30S(cls):
                    return cls("30s")
                
                @schemas.classproperty
                def _40S(cls):
                    return cls("40s")
                
                @schemas.classproperty
                def _50S(cls):
                    return cls("50s")
                
                @schemas.classproperty
                def _60S(cls):
                    return cls("60s")
                
                @schemas.classproperty
                def OLDER(cls):
                    return cls("older")
        
            @staticmethod
            def people_ethnicity() -> typing.Type['SearchImagePeopleEthnicity']:
                return SearchImagePeopleEthnicity
            
            
            class people_gender(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("male")
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("female")
                
                @schemas.classproperty
                def BOTH(cls):
                    return cls("both")
            people_model_released = schemas.BoolSchema
            
            
            class people_number(
                schemas.IntSchema
            ):
                pass
            
            
            class per_page(
                schemas.IntSchema
            ):
                pass
            query = schemas.StrSchema
            
            
            class region(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_0 = schemas.StrSchema
                    any_of_1 = schemas.StrSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'region':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            safe = schemas.BoolSchema
            
            
            class sort(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NEWEST(cls):
                    return cls("newest")
                
                @schemas.classproperty
                def POPULAR(cls):
                    return cls("popular")
                
                @schemas.classproperty
                def RELEVANCE(cls):
                    return cls("relevance")
                
                @schemas.classproperty
                def RANDOM(cls):
                    return cls("random")
            spellcheck_query = schemas.BoolSchema
            
            
            class view(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MINIMAL(cls):
                    return cls("minimal")
                
                @schemas.classproperty
                def FULL(cls):
                    return cls("full")
            width = schemas.IntSchema
            width_from = schemas.IntSchema
            width_to = schemas.IntSchema
            __annotations__ = {
                "added_date": added_date,
                "added_date_end": added_date_end,
                "added_date_start": added_date_start,
                "aspect_ratio": aspect_ratio,
                "aspect_ratio_max": aspect_ratio_max,
                "aspect_ratio_min": aspect_ratio_min,
                "authentic": authentic,
                "category": category,
                "color": color,
                "contributor": contributor,
                "contributor_country": contributor_country,
                "fields": fields,
                "height": height,
                "height_from": height_from,
                "height_to": height_to,
                "image_type": image_type,
                "keyword_safe_search": keyword_safe_search,
                "language": language,
                "license": license,
                "model": model,
                "orientation": orientation,
                "page": page,
                "people_age": people_age,
                "people_ethnicity": people_ethnicity,
                "people_gender": people_gender,
                "people_model_released": people_model_released,
                "people_number": people_number,
                "per_page": per_page,
                "query": query,
                "region": region,
                "safe": safe,
                "sort": sort,
                "spellcheck_query": spellcheck_query,
                "view": view,
                "width": width,
                "width_from": width_from,
                "width_to": width_to,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_date"]) -> MetaOapg.properties.added_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_date_end"]) -> MetaOapg.properties.added_date_end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_date_start"]) -> MetaOapg.properties.added_date_start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aspect_ratio"]) -> MetaOapg.properties.aspect_ratio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aspect_ratio_max"]) -> MetaOapg.properties.aspect_ratio_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aspect_ratio_min"]) -> MetaOapg.properties.aspect_ratio_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentic"]) -> MetaOapg.properties.authentic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributor"]) -> 'SearchImageContributor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributor_country"]) -> MetaOapg.properties.contributor_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height_from"]) -> MetaOapg.properties.height_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height_to"]) -> MetaOapg.properties.height_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_type"]) -> 'SearchImageImageType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyword_safe_search"]) -> MetaOapg.properties.keyword_safe_search: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> 'Language': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license"]) -> 'SearchImageLicense': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> 'SearchImageModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orientation"]) -> MetaOapg.properties.orientation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["people_age"]) -> MetaOapg.properties.people_age: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["people_ethnicity"]) -> 'SearchImagePeopleEthnicity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["people_gender"]) -> MetaOapg.properties.people_gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["people_model_released"]) -> MetaOapg.properties.people_model_released: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["people_number"]) -> MetaOapg.properties.people_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_page"]) -> MetaOapg.properties.per_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["safe"]) -> MetaOapg.properties.safe: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spellcheck_query"]) -> MetaOapg.properties.spellcheck_query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width_from"]) -> MetaOapg.properties.width_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width_to"]) -> MetaOapg.properties.width_to: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["added_date", "added_date_end", "added_date_start", "aspect_ratio", "aspect_ratio_max", "aspect_ratio_min", "authentic", "category", "color", "contributor", "contributor_country", "fields", "height", "height_from", "height_to", "image_type", "keyword_safe_search", "language", "license", "model", "orientation", "page", "people_age", "people_ethnicity", "people_gender", "people_model_released", "people_number", "per_page", "query", "region", "safe", "sort", "spellcheck_query", "view", "width", "width_from", "width_to", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_date"]) -> typing.Union[MetaOapg.properties.added_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_date_end"]) -> typing.Union[MetaOapg.properties.added_date_end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_date_start"]) -> typing.Union[MetaOapg.properties.added_date_start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aspect_ratio"]) -> typing.Union[MetaOapg.properties.aspect_ratio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aspect_ratio_max"]) -> typing.Union[MetaOapg.properties.aspect_ratio_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aspect_ratio_min"]) -> typing.Union[MetaOapg.properties.aspect_ratio_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentic"]) -> typing.Union[MetaOapg.properties.authentic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributor"]) -> typing.Union['SearchImageContributor', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributor_country"]) -> typing.Union[MetaOapg.properties.contributor_country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union[MetaOapg.properties.fields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height_from"]) -> typing.Union[MetaOapg.properties.height_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height_to"]) -> typing.Union[MetaOapg.properties.height_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_type"]) -> typing.Union['SearchImageImageType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyword_safe_search"]) -> typing.Union[MetaOapg.properties.keyword_safe_search, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union['Language', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license"]) -> typing.Union['SearchImageLicense', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> typing.Union['SearchImageModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orientation"]) -> typing.Union[MetaOapg.properties.orientation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["people_age"]) -> typing.Union[MetaOapg.properties.people_age, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["people_ethnicity"]) -> typing.Union['SearchImagePeopleEthnicity', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["people_gender"]) -> typing.Union[MetaOapg.properties.people_gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["people_model_released"]) -> typing.Union[MetaOapg.properties.people_model_released, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["people_number"]) -> typing.Union[MetaOapg.properties.people_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_page"]) -> typing.Union[MetaOapg.properties.per_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["safe"]) -> typing.Union[MetaOapg.properties.safe, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union[MetaOapg.properties.sort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spellcheck_query"]) -> typing.Union[MetaOapg.properties.spellcheck_query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> typing.Union[MetaOapg.properties.view, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width_from"]) -> typing.Union[MetaOapg.properties.width_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width_to"]) -> typing.Union[MetaOapg.properties.width_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["added_date", "added_date_end", "added_date_start", "aspect_ratio", "aspect_ratio_max", "aspect_ratio_min", "authentic", "category", "color", "contributor", "contributor_country", "fields", "height", "height_from", "height_to", "image_type", "keyword_safe_search", "language", "license", "model", "orientation", "page", "people_age", "people_ethnicity", "people_gender", "people_model_released", "people_number", "per_page", "query", "region", "safe", "sort", "spellcheck_query", "view", "width", "width_from", "width_to", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        added_date: typing.Union[MetaOapg.properties.added_date, str, date, schemas.Unset] = schemas.unset,
        added_date_end: typing.Union[MetaOapg.properties.added_date_end, str, date, schemas.Unset] = schemas.unset,
        added_date_start: typing.Union[MetaOapg.properties.added_date_start, str, date, schemas.Unset] = schemas.unset,
        aspect_ratio: typing.Union[MetaOapg.properties.aspect_ratio, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        aspect_ratio_max: typing.Union[MetaOapg.properties.aspect_ratio_max, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        aspect_ratio_min: typing.Union[MetaOapg.properties.aspect_ratio_min, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        authentic: typing.Union[MetaOapg.properties.authentic, bool, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        contributor: typing.Union['SearchImageContributor', schemas.Unset] = schemas.unset,
        contributor_country: typing.Union[MetaOapg.properties.contributor_country, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        fields: typing.Union[MetaOapg.properties.fields, str, schemas.Unset] = schemas.unset,
        height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        height_from: typing.Union[MetaOapg.properties.height_from, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        height_to: typing.Union[MetaOapg.properties.height_to, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        image_type: typing.Union['SearchImageImageType', schemas.Unset] = schemas.unset,
        keyword_safe_search: typing.Union[MetaOapg.properties.keyword_safe_search, bool, schemas.Unset] = schemas.unset,
        language: typing.Union['Language', schemas.Unset] = schemas.unset,
        license: typing.Union['SearchImageLicense', schemas.Unset] = schemas.unset,
        model: typing.Union['SearchImageModel', schemas.Unset] = schemas.unset,
        orientation: typing.Union[MetaOapg.properties.orientation, str, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        people_age: typing.Union[MetaOapg.properties.people_age, str, schemas.Unset] = schemas.unset,
        people_ethnicity: typing.Union['SearchImagePeopleEthnicity', schemas.Unset] = schemas.unset,
        people_gender: typing.Union[MetaOapg.properties.people_gender, str, schemas.Unset] = schemas.unset,
        people_model_released: typing.Union[MetaOapg.properties.people_model_released, bool, schemas.Unset] = schemas.unset,
        people_number: typing.Union[MetaOapg.properties.people_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        per_page: typing.Union[MetaOapg.properties.per_page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        safe: typing.Union[MetaOapg.properties.safe, bool, schemas.Unset] = schemas.unset,
        sort: typing.Union[MetaOapg.properties.sort, str, schemas.Unset] = schemas.unset,
        spellcheck_query: typing.Union[MetaOapg.properties.spellcheck_query, bool, schemas.Unset] = schemas.unset,
        view: typing.Union[MetaOapg.properties.view, str, schemas.Unset] = schemas.unset,
        width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        width_from: typing.Union[MetaOapg.properties.width_from, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        width_to: typing.Union[MetaOapg.properties.width_to, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SearchImage':
        return super().__new__(
            cls,
            *args,
            added_date=added_date,
            added_date_end=added_date_end,
            added_date_start=added_date_start,
            aspect_ratio=aspect_ratio,
            aspect_ratio_max=aspect_ratio_max,
            aspect_ratio_min=aspect_ratio_min,
            authentic=authentic,
            category=category,
            color=color,
            contributor=contributor,
            contributor_country=contributor_country,
            fields=fields,
            height=height,
            height_from=height_from,
            height_to=height_to,
            image_type=image_type,
            keyword_safe_search=keyword_safe_search,
            language=language,
            license=license,
            model=model,
            orientation=orientation,
            page=page,
            people_age=people_age,
            people_ethnicity=people_ethnicity,
            people_gender=people_gender,
            people_model_released=people_model_released,
            people_number=people_number,
            per_page=per_page,
            query=query,
            region=region,
            safe=safe,
            sort=sort,
            spellcheck_query=spellcheck_query,
            view=view,
            width=width,
            width_from=width_from,
            width_to=width_to,
            _configuration=_configuration,
            **kwargs,
        )

from shutterstock_python_sdk.model.language import Language
from shutterstock_python_sdk.model.search_image_contributor import SearchImageContributor
from shutterstock_python_sdk.model.search_image_image_type import SearchImageImageType
from shutterstock_python_sdk.model.search_image_license import SearchImageLicense
from shutterstock_python_sdk.model.search_image_model import SearchImageModel
from shutterstock_python_sdk.model.search_image_people_ethnicity import SearchImagePeopleEthnicity
