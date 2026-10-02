from .Params import Param as __Param

class HeaderGroup:

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

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__name