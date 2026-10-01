from .Params import Param as __Param
from .Constraints import *

from re import findall

__str_type_check = TypeCheck(str)
__int_type_check = TypeCheck(int)
__list_type_check = TypeCheck(list)
__len_limit_two = LengthLimit(2)

COUNTRY = __Param("country", __str_type_check, __len_limit_two)
SOURCES = __Param("sources", __str_type_check, __len_limit_two)
CATEGORY = __Param("category", __str_type_check)
QUERY = __Param("q", LengthLimit(500))
SIZE = __Param("pageSize", __int_type_check)
PAGE = __Param("page", __int_type_check, BoundedInt(0,100))
API_KEY = __Param("apiKey", __str_type_check)
SORT_BY = __Param("sortBy", __list_type_check, literals=("relevancy", "popularity", "publishedAt"))
SEARCH_IN = __Param("search_in", "title", "description", "content", __list_type_check)
EXCLUDE_DOMAINS = __Param("excludeDomains", __list_type_check)
DOMAINS = __Param("domains", __list_type_check)
DATE_FROM = __Param("from")
DATE_TO = __Param("to")
LANG = __Param("language", *findall('..',"ardeenesfrheitnlnoptrusvudzh"), __str_type_check, __len_limit_two)
