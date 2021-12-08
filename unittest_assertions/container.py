""" Container Assertions

Objects provided by this module:
    * `AssertIn`: `assert member in container`
    * `AssertNotIn`: `assert member not in container`
"""
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
)
from unittest import TestCase

from unittest_assertions.base import Assertion


@dataclass
class AssertIn(Assertion):
    """`asser member in container`

    raise `AssertionError` if `member not in container`

    For more documentation read TestCase().assertIn.__doc__

    Example:
        >>> assert_in = AssertIn()
        >>> assert_in(member=1,container=[5,2,1])
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIn, init=False
    )

    def __call__(self, member, container):
        """run assertion

        Args:
            member:
            container:

        Returns:

        """
        super().__call__(member=member, container=container)


@dataclass
class AssertNotIn(Assertion):
    """`asser member not in container`

    raise `AssertionError` if `member in container`

    For more documentation read TestCase().assertNotIn.__doc__

    Example:
        >>> assert_in = AssertNotIn()
        >>> assert_in(member=1,container=[5,2,3])
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotIn, init=False
    )

    def __call__(self, member, container):
        super().__call__(member=member, container=container)
