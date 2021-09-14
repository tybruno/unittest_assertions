""" Regex Assertions """
from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Pattern, AnyStr, Type
from unittest import TestCase

from unittest_assertions.base import BasicBuiltinAssertion


@dataclass
class AssertRaisesRegex(BasicBuiltinAssertion):
    """assert function raises regex

    For more documentation read TestCase().assertRaisesRegex.__doc__

    Example:
        >>> assert_raises_regex = AssertRaisesRegex()
        >>> assert_raises_regex(ValueError, "invalid literal for.*XYZ'$", int, 'XYZ')
    """

    _assertion_function: Callable = field(
        default=TestCase().assertRaisesRegex, init=False
    )

    def __call__(
        self,
        expected_exception: Type[Exception],
        expected_regex: AnyStr,
        function: Callable,
        *args,
        **kwargs,
    ) -> None:
        """Run assertion

        Args:
            expected_exception: The expected exception to be raised
            expected_regex: The expected regex to be found in raised exception.
            function: function that will raise the exception
            *args: arguments that will be passed to `function`
            **kwargs: keyword arguments that will be passed to `function`

        Returns:
            None
        """
        super().__call__(
            expected_exception,
            expected_regex,
            function,
            *args,
            **kwargs,
        )


@dataclass
class AssertWarnsRegex(BasicBuiltinAssertion):
    """assert function warns regex

    For more documentation read TestCase().assertWarnsRegex.__doc__

    Example:
        >>> import warnings
        >>>
        >>> def legacy_function(msg):
        ...     warnings.warn(msg,DeprecationWarning)
        >>> assert_warns_regex = AssertWarnsRegex()
        >>> assert_warns_regex(DeprecationWarning, r'deprecated', legacy_function,r'legacy_function\(\) is deprecated')
    """

    _assertion_function: Callable = field(
        default=TestCase().assertWarnsRegex, init=False
    )

    def __call__(
        self,
        expected_warning: Type[Warning],
        expected_regex: AnyStr,
        function: Callable,
        *args,
        **kwargs,
    ) -> None:
        """Run assertion

        Args:
            expected_warning: The expected warning to be raised
            expected_regex: The expected regex to be in the raised warning
            function: function expected to raise warning
            *args: arguments that will be passed to `function`
            **kwargs: keyword arguments that will be passed to `function`

        Returns:
            None
        """
        super().__call__(
            expected_warning,
            expected_regex,
            function,
            *args,
            **kwargs,
        )


@dataclass
class AssertRegex(BasicBuiltinAssertion):
    """assert regex

    Example:
        >>> assert_regex = AssertRegex()
        >>> assert_regex("Ala ma kota", r"k.t")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertRegex, init=False
    )

    def __call__(
        self,
        text: AnyStr,
        expected_regex: AnyStr,
    ) -> None:
        """Run Assertion

        Args:
            text: Text that will be asserted with the expected regex
            expected_regex: Regex that is expected to be in text

        Returns:
            None
        """
        super().__call__(text=text, expected_regex=expected_regex)


@dataclass
class AssertNotRegex(BasicBuiltinAssertion):
    """assert not regex

    Example:
        >>> assert_regex = AssertNotRegex()
        >>> assert_regex("Ala ma kota", r"wrong")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotRegex, init=False
    )

    def __call__(
        self,
        text: AnyStr,
        unexpected_regex: AnyStr,
    ) -> None:
        """Run Assertion

        Args:
            text: Text asserted to not have the unexpected regex
            unexpected_regex: regex that will be asserted to not be in text

        Returns:
            None
        """
        super().__call__(text=text, unexpected_regex=unexpected_regex)
