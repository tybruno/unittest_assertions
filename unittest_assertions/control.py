from unittest_assertions.base import BuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable
from unittest import TestCase


@dataclass
class AssertRaises(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertRaises, init=False)

    def __call__(self, expected_exception, **kwargs):
        super().__call__(expected_exception=expected_exception, **kwargs)


@dataclass
class AssertWarns(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertWarns, init=False)

    def __call__(self, expected_warning, **kwargs):
        super().__call__(expected_warning=expected_warning, **kwargs)


@dataclass
class AssertLogs(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertLogs, init=False)

    def __call__(self, logger=None, level=None):
        super().__call__(logger=logger, level=level)
