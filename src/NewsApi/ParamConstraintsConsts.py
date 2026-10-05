
from .Params import Param as __Param
from .Constraints import *
from .ParamTyping import DateFromTo as _DateFromTo, Domain as _Domain,\
    Exclude as _Exclude, Lang as _Lang, SearchIn as _SearchIn, SortBy as _SortBy,\
    Country as _Country, Sources as _Sources, Category as _Cat, Query as _Query,\
    Size as _Size, Page as _Page, ApiKey as _Key

__len_limit_two = LengthLimit(2)

COUNTRY = __Param[_Country](__len_limit_two)
SOURCES = __Param[_Sources](__len_limit_two)
CATEGORY = __Param[_Cat]()
QUERY = __Param[_Query](LengthLimit(500))
SIZE = __Param[_Size]()
PAGE = __Param[_Page](BoundedInt(0,100))
API_KEY = __Param[_Key]()
SORT_BY = __Param[_SortBy]()
SEARCH_IN = __Param[_SearchIn]()
EXCLUDE_DOMAINS = __Param[_Exclude]()
DOMAINS = __Param[_Domain]()
DATE_FROM = __Param[_DateFromTo]()
DATE_TO = __Param[_DateFromTo]()
LANG = __Param[_Lang]()
