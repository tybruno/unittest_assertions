""" Control Assertions """
import logging
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
    Type,
)
from unittest import TestCase

from unittest_assertions.base import BasicBuiltinAssertion


@dataclass
class AssertRaises(BasicBuiltinAssertion):
    """assert `Callable` raises `expected_exception`

    raise `AssertionError` if `Callable` does not raise `Exception`

    For more documentation read TestCase().assertRaises.__doc__

    Example:
        >>> def _raise_value_error():
        ...     raise ValueError()
        >>> assert_raises = AssertRaises()
        >>> assert_raises(ValueError,_raise_value_error )
    """

    _assertion_function: Callable = field(
        default=TestCase().assertRaises, init=False
    )

    def __call__(
        self,
        expected_exception: Type[Exception],
        function: Callable,
        *function_args,
        **function_kwargs
    ) -> None:
        """Run Assertion

        Args:
            expected_exception: The expected `Exception` raised by the function
            function: Function that will be called.
            *function_args: arguments for the calling `function`
            **function_kwargs: keyword arguments for the calling `function

        Returns:
            None
        """
        super().__call__(
            expected_exception, function, *function_args, **function_kwargs
        )


@dataclass
class AssertWarns(BasicBuiltinAssertion):
    """assert `Callable` raises `Warning`

    raise `AssertionError` if `Callable` does not raise `Warning`

    For more documentation read TestCase().assertWarns.__doc__

    Example:
        >>> import warnings
        >>> def _warning(message, warning: Warning):
        ...     warnings.warn(message, warning)
        >>> assert_warns = AssertWarns()
        >>> assert_warns( Warning,_warning, str(), Warning )
    """

    _assertion_function: Callable = field(
        default=TestCase().assertWarns, init=False
    )

    def __call__(
        self,
        expected_warning: Type[Warning],
        function: Callable,
        *function_args,
        **function_kwargs
    ) -> None:
        """Run Assertion

        Args:
            expected_warning: The expected `Warning` raised by the `function`
            function: function that will be called
            *function_args: arguments for the calling `function`
            **function_kwargs: keyword arguments for the calling `function

        Returns:
            None
        """
        super().__call__(
            expected_warning, function, *function_args, **function_kwargs
        )


@dataclass
class AssertLogs(BasicBuiltinAssertion):
    """assert `Callable` Logs

    raise `AssertionError` if `Callable` does not Log

    For more documentation read TestCase().assertLogs.__doc__
    """

    _assertion_function: Callable = field(
        default=TestCase().assertLogs, init=False
    )

    def __call__(self, logger: logging.Logger = None, level=None) -> None:
        """Run Logging Assertion

        Args:
            logger: `logging.Logger` that will be asserted
            level: level that the `logging.Logger` should log

        Returns:
            None
        """
        super().__call__(logger=logger, level=level)
