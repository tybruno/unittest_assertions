""" Container Assertions"""
from unittest_assertions.base import BuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable
from unittest import TestCase


@dataclass
class ContainerAssertion(BuiltinAssertion):
    def __call__(self, *, member, container):
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
