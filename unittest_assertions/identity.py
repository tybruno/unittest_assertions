from unittest_assertions.base import BuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable
from unittest import TestCase


@dataclass
class AssertIs(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertIs, init=False)

    def __call__(self, exp1, exp2):
        super().__call__(exp1=exp1, exp2=exp2)


@dataclass
class AssertIsNot(AssertIs):
    function: Callable = field(default=TestCase().assertIsNot, init=False)


@dataclass
class AssertIsNone(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertIsNone, init=False)

    def __call__(self, obj):
        super().__call__(obj=obj)


@dataclass
class AssertIsNotNone(AssertIsNone):
    function: Callable = field(default=TestCase().assertIsNotNone, init=False)


@dataclass
class AssertIsInstance(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertIsInstance, init=False)

    def __call__(self, obj, cls):
        super().__call__(obj=obj, cls=cls)


@dataclass
class AssertNotIsInstance(AssertIsInstance):
    function: Callable = field(
        default=TestCase().assertNotIsInstance, init=False
    )
