""" Base classes for assertions

Objects provided by this module:
    * `Assertion`: Base class for assertions
"""
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
    Union,
)


@dataclass
class Assertion:
    """Basic Builtin Assertion base class
    Example:
        >>> from unittest import TestCase
        >>> assert_equal = Assertion(_assertion_function=TestCase().assertEqual)
        >>> assert_equal(1,1)

    Attributes:
        self._assertion_function: function that runs the assertion.
    """

    _assertion_function: Callable
    msg: Union[str, None] = field(default=None)

    def __call__(self, *args, **kwargs) -> None:
        """Run the Assertion function with the given function_args and function_kwargs

        Args:
            *args: Arguments that will be passed to the `_assertion_function`
            **kwargs: Keyword arguments to be passed to the
            `_assertion_function`

        Returns:
            None
        """
        msg: Union[str, None] = kwargs.pop("msg", self.msg)
        self._assertion_function(*args, **kwargs, msg=msg)