

class ConstraintFail(Exception):pass


class LengthLimit:

    def __init__(self, len_limit:int):
        self.__check_type(len_limit)
        self.limit:int = len_limit

    @staticmethod
    def __check_type(length:int):
        if type(length) != int:
            raise TypeError("length must be of type int but got: %s" % type(length))

    def __call__(self, value:str):
        if len(value) > self.limit:
            raise ConstraintFail


class TypeCheck:
    #Update type hinting to better show types.
    def __init__(self, obj_type:type):
        self.objType:type = obj_type

    def __call__(self, obj:type):
        if type(obj) != self.objType:
            raise ConstraintFail


class IntRoof:

    def __init__(self, limit:tuple[str,int]):
        self.limit = limit

    def __call__(self, int_val):
        lower, upper = self.limit
        if isinstance(lower, int) and int_val < lower:
            raise ConstraintFail
        if isinstance(upper, int) and int_val > upper:
            raise ConstraintFail
