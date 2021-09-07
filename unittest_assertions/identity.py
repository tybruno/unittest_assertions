from unittest_assertions.base import BuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable
from unittest import TestCase


@dataclass
class AssertIs(BuiltinAssertion):
    _function: Callable = field(default=TestCase().assertIs, init=False)

    def __call__(self, expr1, expr2):
        super().__call__(expr1=expr1, expr2=expr2)


@dataclass
class AssertIsNot(AssertIs):
    _function: Callable = field(default=TestCase().assertIsNot, init=False)


@dataclass
class AssertIsNone(BuiltinAssertion):
    _function: Callable = field(default=TestCase().assertIsNone, init=False)

    def __call__(self, obj):
        super().__call__(obj=obj)


@dataclass
class AssertIsNotNone(AssertIsNone):
    _function: Callable = field(default=TestCase().assertIsNotNone, init=False)


@dataclass
class AssertIsInstance(BuiltinAssertion):
    _function: Callable = field(
        default=TestCase().assertIsInstance, init=False
    )

    def __call__(self, obj, cls):
        super().__call__(obj=obj, cls=cls)


@dataclass
class AssertNotIsInstance(AssertIsInstance):
    _function: Callable = field(
        default=TestCase().assertNotIsInstance, init=False
    )
