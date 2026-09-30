
from .HeaderGroups import HeaderGroup as __HeaderGroup
from ParamConstraintsConsts import *


TOP = __HeaderGroup\
    ("top-headlines", API_KEY, COUNTRY, CATEGORY, SOURCES, QUERY, SIZE, PAGE, LANG)
EVERYTHING = __HeaderGroup\
    ("everything", API_KEY, QUERY, SEARCH_IN, SOURCES, DOMAINS, EXCLUDE_DOMAINS,
                        DATE_FROM, DATE_TO, SORT_BY, SIZE, PAGE, LANG)