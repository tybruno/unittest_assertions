""" Container Assertions"""
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    Callable,
    Container,
)
from unittest import TestCase

from unittest_assertions.base import BuiltinAssertion


@dataclass
class ContainerAssertion(BuiltinAssertion):
    """Perent class for Container assertions."""

    def __call__(self, *, member: Any, container: Container) -> None:
        """call `_assertion_function` with `member` and `container` as
        agruments

        Args:
            member: will be checked to see if it is in the `container`
            container: `container` that will be checked if it contains the
             `container`

        Returns:
             None
        """
        super().__call__(member=member, container=container)


@dataclass
class AssertIn(ContainerAssertion):
    """assert `member` `in` `container`

    raise `AssertionError` if `member` not in `container`

    For more documentation read TestCase().assertIn.__doc__

    Example:
        >>> assert_in = AssertIn()
        >>> assert_in(member=1,container=[5,2,1])
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIn, init=False
    )


@dataclass
class AssertNotIn(ContainerAssertion):
    """assert `member` `not in` `container`

    raise `AssertionError` if `member` in `container`

    For more documentation read TestCase().assertNotIn.__doc__

    Example:
        >>> assert_in = AssertNotIn()
        >>> assert_in(member=1,container=[5,2,3])
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotIn, init=False
    )
