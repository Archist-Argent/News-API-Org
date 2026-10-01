from typing import Any

from .Constraint import ParamConstraint
from .Constraints import Constraint

__all__ = ["Param"]


_ConstrainVals = tuple[Any, ...] | Any


class Param:
    """
    Represents a parameter that could be used and assigned to a header group.
    """
    def __init__(self, *constraints:ParamConstraint | tuple[Constraint, _ConstrainVals] | tuple[ParamConstraint | tuple[Constraint, _ConstrainVals], ...]):
        self.__constraints = constraints

    def validate(self, value:Any):
        for constraint in self.__constraints:
            constraint(value)
