from unittest_assertions.base import BasicBuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable
from unittest import TestCase


@dataclass
class AssertRaises(BasicBuiltinAssertion):

    _assertion_function: Callable = field(
        default=TestCase().assertRaises, init=False
    )

    def __call__(self, expected_exception, *args, **kwargs):
        super().__call__(expected_exception, *args, **kwargs)


@dataclass
class AssertWarns(BasicBuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertWarns, init=False
    )

    def __call__(self, expected_warning, *args, **kwargs):
        super().__call__(expected_warning, *args, **kwargs)


@dataclass
class AssertLogs(BasicBuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertLogs, init=False
    )

    def __call__(self, logger=None, level=None):
        super().__call__(logger=logger, level=level)
