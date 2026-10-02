from typing import Literal, Iterable, Any
from datetime import datetime

from .Params import Param as __Param
from .Constraints import *

__len_limit_two = LengthLimit(2)

COUNTRY = __Param[str](__len_limit_two)
SOURCES = __Param[str](__len_limit_two)
CATEGORY = __Param[str]()
QUERY = __Param[str](LengthLimit(500))
SIZE = __Param[int]()
PAGE = __Param[int](BoundedInt(0,100))
API_KEY = __Param[str]()
SORT_BY = __Param[Iterable[Literal["relevancy", "popularity", "publishedAt"]]]()
SEARCH_IN = __Param[Iterable[Literal["title", "description", "content"]]]()
EXCLUDE_DOMAINS = __Param[Iterable[Any]]()
DOMAINS = __Param[Iterable[Any]]()
DATE_FROM = __Param[datetime]()
DATE_TO = __Param[datetime]()
LANG = __Param[Literal["ar","de","en","es","fr","he","it","nl","no","pt","ru","sv","ud","zh"]]()
