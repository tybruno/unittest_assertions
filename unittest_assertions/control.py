""" Control Assertions """  # pylint: disable=duplicate-code
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
class AssertRaises(BuiltinAssertion):
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


@dataclass
class AssertWarns(BuiltinAssertion):
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


@dataclass
class AssertLogs(BuiltinAssertion):
    """assert `Callable` Logs

    raise `AssertionError` if `Callable` does not Log

    For more documentation read TestCase().assertLogs.__doc__
    """

    _assertion_function: Callable = field(
        default=TestCase().assertLogs, init=False
    )
