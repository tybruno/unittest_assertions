""" Regex Assertions

Objects provided by this module:
    * `AssertRaisesRegex`: asserts that the message in a raised exception matches a regex
    * `AssertWarnsRegex`: asserts that the message in a triggered warning matches a regexp.
    * `AssertRegex`: Fail the assertion unless the text matches the regular expression
    * `AssertNotRegex`: Fail the assertion if the text matches the regular expression
"""
import re
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
    ContextManager,
    Type,
    Union,
    Tuple,
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

    def __call__(
        self,
        expected_exception: Union[
            Type[BaseException], Tuple[Type[BaseException]]
        ],
        expected_regex: Union[re.Pattern, str],
        function: Callable,
        *function_args,
        **function_kwargs
    ):
        """assert function raises regex

        Args:
            expected_exception: expected exception to be raised
            expected_regex: expected regex during `expected_exception` is raised
            function: function to be called
            *arg: extra positional function_args for the called function
            **function_kwargs: Extra function_kwargs for the called function.
        """
        if isinstance(expected_exception, ContextManager):
            super().__call__(
                expected_exception,
                expected_regex,
                function,
                *function_args,
                **function_kwargs
            )
        else:
            self._assertion_function(
                expected_exception,
                expected_regex,
                function,
                *function_args,
                **function_kwargs
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

    def __call__(
        self,
        expected_warning: Type[Warning],
        expected_regex: Union[re.Pattern, str],
        function: Callable,
        *function_args,
        **function_kwargs
    ) -> None:
        """Asserts that the message in a triggered warning matches a regexp.

        Args:
            expected_warning: `Warning~ class expected to be raised
            expected_regex: Regex expected to be found in error message
            function: function that will be called
            *function_args: extra positional function_args for called function
            **function_kwargs: Extra function_kwargs for called function
        """
        if isinstance(expected_warning, ContextManager):
            super().__call__(
                expected_warning,
                expected_regex,
                function,
                *function_args,
                **function_kwargs
            )
        else:
            self._assertion_function(
                expected_warning,
                expected_regex,
                function,
                *function_args,
                **function_kwargs
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

    def __call__(
        self, text: str, expected_regex: Union[re.Pattern, str]
    ) -> None:
        """asserts `text` matches `expected_regex`

        Args:
            text: checked to see if will match `expected_regex`
            expected_regex: checked to see if it matched `text`
        """
        super().__call__(text=text, expected_regex=expected_regex)


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

    def __call__(
        self, text: str, unexpected_regex: Union[re.Pattern, str]
    ) -> None:
        """assert `text` does not match `unexpected_regex`

        Args:
            text: checked to see that it does not match `unexpected_regex`
            unexpected_regex: checked to see that it does not match `text`
        """
        super().__call__(text=text, unexpected_regex=unexpected_regex)
