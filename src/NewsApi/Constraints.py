
from typing import override, NoReturn, TypeVar, Generic
from collections.abc import Sized
from abc import ABC, abstractmethod

__all__ = ["LengthLimit", "BoundedInt"]

class ConstraintFail(Exception):pass


_AllowedValTypes = TypeVar('_AllowedValTypes', contravariant=True)

class Constraint(Generic[_AllowedValTypes], ABC):

    @abstractmethod
    def validate_value(self, value:_AllowedValTypes) -> NoReturn | None:...


class LengthLimit(Constraint[str]):

    def __init__(self, len_limit:int):
        self.limit:int = len_limit

    @staticmethod
    def __check_type(length:int):
        if type(length) != int:
            raise TypeError("length must be of type int but got: %s" % type(length))

    @override
    def validate_value(self, value:Sized) -> NoReturn | None:
        if len(value) > self.limit:
            raise ConstraintFail
        return None

from typing import TypeAlias

class BoundedInt(Constraint[int]):

    __LowerLimit:TypeAlias = int
    __UpperLimit:TypeAlias = int

    def __init__(self, lower_limit:__LowerLimit, upper_limit:__UpperLimit):
        self.__lower_imit = lower_limit
        self.__upper_limit = upper_limit

    @override
    def validate_value(self, value: int) -> NoReturn | None:
        if self.__lower_imit < value < self.__upper_limit:
            raise ConstraintFail
        return None
