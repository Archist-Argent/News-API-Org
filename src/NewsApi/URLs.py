from typing import Any

from .Params import Param as __Param

__BASE_URL = r'https://newsapi.org/v2'

class Url:

    def __init__(self, header:str, **params:__Param):
        """
        Replace kwargs with keywords for params. These keywords will be used to index the parameters for checking later on validation.
        :param params: A dicitonary of named parameter isntances.
        :param header: A header to choose what query to run.
        """
        self.params = params
        self.header = header

    def validate(self, **kvals:Any):
        """
        Generates URL based on parameter inputs. Should override in child class for type hinting purposes that calls super with all the parameters.
        """
        for name, value in kvals.items():
            if param := self.params.get(name):
                param.validate(value)
            else:
                raise KeyError('Parameter "%s" is not defined in params <%s>' %(name, self.params.keys()))
