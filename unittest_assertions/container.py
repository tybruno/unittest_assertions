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
    function: Callable = field(default=TestCase().assertIn, init=False)


@dataclass
class AssertNotIn(ContainerAssertion):
    function: Callable = field(default=TestCase().assertNotIn, init=False)
