from dataclasses import (
    dataclass,
    field,
)
from typing import Callable
from unittest import TestCase

from unittest_assertions.base import BuiltinAssertion


@dataclass
class AssertRaisesRegex(BuiltinAssertion):
    function: Callable = field(
        default=TestCase().assertRaisesRegex, init=False
    )

    def __call__(self, expected_exception, expected_regex, **kwargs):
        super().__call__(
            expected_exception=expected_exception,
            expected_regex=expected_regex,
            **kwargs
        )


@dataclass
class AssertWarnsRegex(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertWarnsRegex, init=False)

    def __call__(self, expected_warning, expected_regex, **kwargs):
        super().__call__(
            expected_warning=expected_warning,
            expected_regex=expected_regex,
            **kwargs
        )


@dataclass
class AssertRegex(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertRegex, init=False)

    def __call__(self, text, expected_regex):
        super().__call__(text=text, expected_regex=expected_regex)


@dataclass
class AssertNotRegex(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertNotRegex, init=False)

    def __call__(self, text, unexpected_regex):
        super().__call__(text=text, unexpected_regex=unexpected_regex)
