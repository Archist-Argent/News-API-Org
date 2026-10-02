from typing import Any
from .Constraints import Constraint

__all__ = ["Param"]

class Param [Types]:
    """
    Represents a parameter that could be used and assigned to a header group.
    """
    def __init__(self, *constraints:Constraint[Any]):
        self.__constraints = constraints

    def validate(self, value:Types):
        for constraint in self.__constraints:
            constraint.validate_value(value)
