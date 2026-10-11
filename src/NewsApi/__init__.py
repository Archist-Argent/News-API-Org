__title__ = "NewsApi"
__author__ = "Archist"

from typing import Optional

from .URLs import Url as _Url
from .ParamConstraintsConsts import API_KEY as _key, CATEGORY as _cat, PAGE as _p, LANG as _lang\
    ,COUNTRY as _country, SOURCES as _sources, QUERY as _q, PAGE_SIZE as _page_size, SEARCH_IN as _search_in\
    ,DOMAINS as _domains, EXCLUDE_DOMAINS as _excluded_domains, DATE_FROM as _date_from, DATE_TO as _date_to\
    ,SORT_BY as _sort_by
    
from .ParamTyping import ApiKey as _ApiKey, Category as _Category, Page as _Page, Query as _Query\
    ,Sources as _Sources, Country as _Country,

__all__ = ['EVERYTHING', 'TOP_HEADLINES']

class TopHeadlines:

    BASE_URL = _Url('top-headlines', api_key = _key, category = _cat, page = _p, page_size = _page_size, query = _q, sources = _sources, country = _country)

    @classmethod
    def validate(cls, api_key:_ApiKey, category:Optional[_Category], page_size:Optional[_Page], query:_Query, sources:_Sources, country:_Country):...


class Everything:

    BASE_URL = _Url('everything', api_key = _key, query = _q, search_in = _search_in, sources = _sources,
                    domains = _domains, _exclude_domains = _excluded_domains, date_start = _date_from,
                    date_end = _date_to, language = _lang, sort_by = _sort_by, page_size = _page_size,
                    page = _p)

    @classmethod
    def validate(cls):...


EVERYTHING = Everything.validate
TOP_HEADLINES = TopHeadlines.validate