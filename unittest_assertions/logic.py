""" Logical Assertions """  # pylint: disable=duplicate-code
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
)
from unittest import TestCase

from unittest_assertions.base import BuiltinAssertion


@dataclass
class AssertTrue(BuiltinAssertion):
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
class AssertFalse(BuiltinAssertion):
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
