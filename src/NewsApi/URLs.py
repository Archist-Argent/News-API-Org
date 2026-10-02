from urllib import parse

from .ApiCaller import ApiResponse
from .ApiKey import ApiKey
from .HeaderGroups import HeaderGroup
from .ApiCaller import call_api

class URL:

    __baseURL = 'https://newsapi.org/v2/'

    def __init__(self, name:str, *params:__Param):
            """
            Instances header group creating a group of parameters to be used for a specific header.
            :param name: The name to be printed out for the header group in url formation.
            :param params: Parameter objects
            module to be used in the header group.
            """
            self.__name:str = name
            self.__params:dict[str,__Param] = {} #A dictionary of the param name and parameter.
            self.add_params(*params) #Adding initial passed in parameters.
    
    @property
    def name(self):
        """
        Returns the name of the header group.
        """
        return self.__name

    def add_params(self, *params:__Param):
        """
        Adds in the new parameter values to the params dictionary.
        :param params: An iterable of initialized parameters to be assigned to the header group.
        """
        self.__params[param] = param_obj

    @property
    def set_params(self):
        return self.__setParams

    def set_api_key(self, key):
        """
        Sets a new api key.
        :param key: An instance of the ApiKey class.
        """
        if not isinstance(key, ApiKey):
            raise TypeError('"key" must be of type %s' % ApiKey)
        self.__apiKey = key

    def form_url(self, **params):
        """
        Returns a formatted url to be sent as an HTTP request.
        :param params: Parameter values to be passed into at format time. These will overwrite non set defaults.
        These values still need to be defined within the header group assigned to the URL.
        """
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
