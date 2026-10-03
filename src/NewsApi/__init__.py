__title__ = "NewsApi"
__author__ = "Archist"

from .URLs import URL as _URL
from .ParamConstraintsConsts import API_KEY as __key, CATEGORY as __cat, PAGE as __p

EVERYTHING = _URL(__key, __cat, __p)
TOP_HEADLINES = _URL()
 EVERYTHING.form_url()