__title__ = "NewsApi"
__author__ = "Archist"

from .URLs import URL as URL
from .ParamConstraintsConsts import API_KEY as __key, CATEGORY as __cat, PAGE as __p, LANG as _lang
from .ParamTyping import ApiKey as _ApiKey, Category as _Category, Page as _Page

@URL(api_key = __key, category = __cat, page_size = __p)
def everything(api_key: _ApiKey, category: _Category, page_size: _Page):pass


@URL()
def top_headlines():pass