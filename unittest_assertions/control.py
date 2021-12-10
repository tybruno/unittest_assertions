""" Control Assertions

Objects provided by this module:
    * `AssertRaises`: assert Callable raises expected exception
    * `AssertWarns`: assert Callable raises a warning
"""
import logging
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
    ContextManager,
    Union,
    Type,
    Tuple,
    Optional,
    Collection,
    Mapping,
)
from unittest import TestCase

from unittest_assertions.base import Assertion


@dataclass
class AssertRaises(Assertion):
    """assert `Callable` raises `expected_exception`

    Fail unless an exception of class expected_exception is raised
    by the callable_ when invoked with specified positional and
    keyword arguments. If a different type of exception is
    raised, it will not be caught, and the test case will be
    deemed to have suffered an error, exactly as for an
    unexpected exception.

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
        expected_exception: Union[
            Type[BaseException], Tuple[Type[BaseException]]
        ],
        callable_: Callable,
        *args: Optional[Collection],
        **kwargs: Optional[Mapping],
    ) -> None:
        """assert `callable_` raises `expected_exception`

        Args:
            expected_exception: The expected exception to be raised by `callable_`
            callable_: callable that is expecting to raise exception `expected_exception`
            *args: Optional function_args
            **kwargs: Optional function_kwargs

        Returns:
            None
        """
        if isinstance(expected_exception, ContextManager):
            super().__call__(expected_exception, callable_, *args, **kwargs)
        else:
            self._assertion_function(
                expected_exception, callable_, *args, **kwargs
            )


@dataclass
class AssertWarns(Assertion):
    """assert `Callable` raises `Warning`

    Fail unless a warning of class warnClass is triggered
    by the callable_ when invoked with specified positional and
    keyword arguments.  If a different type of warning is
    triggered, it will not be handled: depending on the other
    warning filtering rules in effect, it might be silenced, printed
    out, or raised as an exception.

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
        callable_: Callable,
        *args: Optional,
        **kwargs: Optional,
    ) -> None:
        """assert `Callable` raises `Warning`

        Args:
            expected_warning: The expected warning to be raised by `callable_`
            callable_: The callable that is expected to raise `expected_warning`
            *args: Optional function_args
            **kwargs: Optional function_kwargs

        Returns:
            None
        """
        if isinstance(expected_warning, ContextManager):
            super().__call__(expected_warning, callable_, *args, **kwargs)
        else:
            self._assertion_function(
                expected_warning, callable_, *args, **kwargs
            )


@dataclass
class AssertLogs(Assertion):
    """assert `Callable` Logs

    Fail unless a log message of level *level* or higher is emitted
    on *logger_name* or its children.  If omitted, *level* defaults to
    INFO and *logger* defaults to the root logger.

    raise `AssertionError` if `Callable` does not Log

    For more documentation read TestCase().assertLogs.__doc__
    """

    _assertion_function: Callable = field(
        default=TestCase().assertLogs, init=False
    )

    def __call__(self, logger: logging.Logger = None, level: int = None):
        """assert `logger` logs at `level`

        Args:
            logger: check it if logger logs at `level`
            level: that `logger` should log at

        Returns:
            None
        """
        super().__call__(logger=logger, level=level)
