from .Params import Param as __Param

from re import findall

COUNTRY = __Param("country",type=str, length=2)
SOURCES = __Param("sources", type=str, length=2)
CATEGORY = __Param("category", type=str)
QUERY = __Param("q", length=500)
SIZE = __Param("pageSize", type=int)
PAGE = __Param("page", type=int, int_limit=(0,100))
API_KEY = __Param("apiKey", type=str)
SORT_BY = __Param("sortBy", "relevancy", "popularity", "publishedAt", type=list)
SEARCH_IN = __Param("search_in", "title", "description", "content", type=list)
EXCLUDE_DOMAINS = __Param("excludeDomains", type=list)
DOMAINS = __Param("domains", type=list)
DATE_FROM = __Param("from")
DATE_TO = __Param("to")
LANG = __Param("language", *findall('..',"ardeenesfrheitnlnoptrusvudzh"), type=str, length=2)
