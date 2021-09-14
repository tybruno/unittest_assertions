from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Pattern, AnyStr
from unittest import TestCase

from unittest_assertions.base import BasicBuiltinAssertion


@dataclass
class AssertRaisesRegex(BasicBuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertRaisesRegex, init=False
    )

    def __call__(
        self,
        expected_exception: Exception,
        expected_regex: Pattern[str],
        **kwargs
    ):
        super().__call__(
            expected_exception=expected_exception,
            expected_regex=expected_regex,
            **kwargs
        )


@dataclass
class AssertWarnsRegex(BasicBuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertWarnsRegex, init=False
    )

    def __call__(
        self, expected_warning: Warning, expected_regex: Pattern[str], **kwargs
    ):
        super().__call__(
            expected_warning=expected_warning,
            expected_regex=expected_regex,
            **kwargs
        )


@dataclass
class AssertRegex(BasicBuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertRegex, init=False
    )

    def __call__(self, text: AnyStr, expected_regex: Pattern[AnyStr]):
        super().__call__(text=text, expected_regex=expected_regex)


@dataclass
class AssertNotRegex(BasicBuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertNotRegex, init=False
    )

    def __call__(self, text: AnyStr, unexpected_regex: Pattern[AnyStr]):
        super().__call__(text=text, unexpected_regex=unexpected_regex)
