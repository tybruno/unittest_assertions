""" Regex Assertions """  # pylint: disable=duplicate-code
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
)
from unittest import TestCase

from unittest_assertions.base import BuiltinAssertion


@dataclass
class AssertRaisesRegex(BuiltinAssertion):
    """assert function raises regex

    For more documentation read TestCase().assertRaisesRegex.__doc__

    Example:
        >>> assert_raises_regex = AssertRaisesRegex()
        >>> assert_raises_regex(ValueError, "invalid literal for.*XYZ'$",
        ... int, 'XYZ')
    """

    _assertion_function: Callable = field(
        default=TestCase().assertRaisesRegex, init=False
    )


@dataclass
class AssertWarnsRegex(BuiltinAssertion):
    """assert function warns regex

    For more documentation read TestCase().assertWarnsRegex.__doc__

    Example:
        >>> import warnings
        >>>
        >>> def legacy_function(msg):
        ...     warnings.warn(msg,DeprecationWarning)
        >>> assert_warns_regex = AssertWarnsRegex()
        >>> assert_warns_regex(DeprecationWarning, r'deprecated',
        ... legacy_function,r'legacy_function is deprecated')
    """

    _assertion_function: Callable = field(
        default=TestCase().assertWarnsRegex, init=False
    )


@dataclass
class AssertRegex(BuiltinAssertion):
    """assert regex

    Example:
        >>> assert_regex = AssertRegex()
        >>> assert_regex("Ala ma kota", r"k.t")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertRegex, init=False
    )


@dataclass
class AssertNotRegex(BuiltinAssertion):
    """assert not regex

    Example:
        >>> assert_regex = AssertNotRegex()
        >>> assert_regex("Ala ma kota", r"wrong")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotRegex, init=False
    )
