from unittest_assertions.base import BuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable
from unittest import TestCase


@dataclass
class LogicalAssertion(BuiltinAssertion):
    def __call__(self, expr):
        super().__call__(expr=expr)


@dataclass
class AssertTrue(LogicalAssertion):
    function: Callable = field(default=TestCase().assertTrue, init=False)


@dataclass
class AssertFalse(LogicalAssertion):
    function: Callable = field(default=TestCase().assertFalse, init=False)
