""" Logical Assertions """
from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Any
from unittest import TestCase

from unittest_assertions.base import BuiltinAssertion


@dataclass
class LogicalAssertion(BuiltinAssertion):
    """Parent class for logical assertions"""

    def __call__(self, expr: Any) -> None:
        """Evaluate the logical expression

        Args:
            expr: expression that will be evaluated by the assertion

        Returns:
            None
        """
        super().__call__(expr=expr)


@dataclass
class AssertTrue(LogicalAssertion):
    """assert `expr`

    raise `AssertionError` if not `expr`

    For more documentation read TestCase().assertTrue.__doc__

    Example:
        >>> assert_true = AssertTrue()
        >>> assert_true(True)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertTrue, init=False
    )


@dataclass
class AssertFalse(LogicalAssertion):
    """assert not `expr`

    raise `AssertionError` if `expr`

    For more documentation read TestCase().assertFalse.__doc__

    Example:
        >>> _false_objects = ["", 0, [], False]
        >>> assert_false = AssertFalse()
        >>> for obj in _false_objects:
        ...     assert_false(obj)

    """

    _assertion_function: Callable = field(
        default=TestCase().assertFalse, init=False
    )
