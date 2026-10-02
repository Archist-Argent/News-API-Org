from typing import Any, Iterable, Optional

from .Constraints import Constraint

__all__ = ["Param"]


class Param:
    """
    Represents a parameter that could be used and assigned to a header group.
    """
    def __init__(self, name:str, *constraints:Constraint[Any], literals:Optional[Iterable[Any]] = None):
        self.__name = name
        self.__constraints = constraints

    def validate(self, value:Any):
        for constraint in self.__constraints:
            constraint.validate_value(value)

    @property
    def name(self):
        return self.__name
