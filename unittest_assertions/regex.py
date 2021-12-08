""" Regex Assertions

Objects provided by this module:
    * `AssertRaisesRegex`: asserts that the message in a raised exception matches a regex
    * `AssertWarnsRegex`: asserts that the message in a triggered warning matches a regexp.
    * `AssertRegex`: Fail the assertion unless the text matches the regular expression
    * `AssertNotRegex`: Fail the assertion if the text matches the regular expression
"""
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
)
from unittest import TestCase

from unittest_assertions.base import Assertion


@dataclass
class AssertRaisesRegex(Assertion):
    """assert function raises regex

    Asserts that the message in a raised exception matches a regex.

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
class AssertWarnsRegex(Assertion):
    """assert function warns regex

    Asserts that the message in a triggered warning matches a regexp.
    Basic functioning is similar to assertWarns() with the addition
    that only warnings whose messages also match the regular expression
    are considered successful matches.

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
class AssertRegex(Assertion):
    """assert regex

    Fail the assertion unless the text matches the regular expression.

    Example:
        >>> assert_regex = AssertRegex()
        >>> assert_regex("Ala ma kota", r"k.t")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertRegex, init=False
    )


@dataclass
class AssertNotRegex(Assertion):
    """assert not regex

    Fail the assertion if the text matches the regular expression

    Example:
        >>> assert_regex = AssertNotRegex()
        >>> assert_regex("Ala ma kota", r"wrong")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotRegex, init=False
    )
