from urllib import parse
from typing import Any, Callable
from types import FunctionType
from functools import wraps

from .Params import Param as __Param

type _Url = str
type _ParamArgs = dict[str,__Param[Any]]

def URL(**params:__Param[Any]) -> Callable[[FunctionType], Callable[..., _Url]]:
    """
    Returns a formatted url to be sent as an HTTP request.
    :param params: Parameter values to be passed into at format time. These will overwrite non set defaults.
    These values still need to be defined within the header group assigned to the URL.
    """
    def url_sig(signature:Callable[...,None]) -> Callable[..., _Url]:
        wraps(signature)
        def url_func(**kargs:...) -> _Url:
            if self.__apiKey is None:
                raise ValueError('You must define an API key.')
            self.__header.check_params(**params)
            url_structure = [self.__header.name]
            if type(self.__setParams) == set and len(self.__setParams.intersection(set(params.keys()))) != 0:
                # Checks for any parameters that were set as non-editable.
                raise KeyError\
                    (
                        'The following parameters were set as non-editable: %s' \
                        % self.__setParams.intersection(set(params.keys()))
                    )
            for param in set(self.__paramDefaults.keys()).difference(set(params.keys())):
                # Updates the parameters with default params that weren't overwritten.
                params[param] = self.__paramDefaults[param]
            return self.__baseURL+'/'.join(url_structure)+'?'+'&'.join(['%s=%s' % (param, value) for param, value in params.items()])
        return url_func
    return url_sig
