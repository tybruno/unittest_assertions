from unittest_assertions.base import BuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable
from unittest import TestCase


class ControlAssertion(BuiltinAssertion):
    def __call__(self, *args, **kwargs):
        self._function(*args, **kwargs)


@dataclass
class AssertRaises(ControlAssertion):
    _function: Callable = field(default=TestCase().assertRaises, init=False)

    def __call__(self, expected_exception, *args, **kwargs):
        super().__call__(expected_exception, *args, **kwargs)


@dataclass
class AssertWarns(ControlAssertion):
    _function: Callable = field(default=TestCase().assertWarns, init=False)

    def __call__(self, expected_warning, **kwargs):
        super().__call__(expected_warning=expected_warning, **kwargs)


@dataclass
class AssertLogs(ControlAssertion):
    _function: Callable = field(default=TestCase().assertLogs, init=False)

    def __call__(self, logger=None, level=None):
        super().__call__(logger=logger, level=level)
