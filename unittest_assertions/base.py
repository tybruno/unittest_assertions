""" Base classes and Abstract Base Classes """
from dataclasses import (
    dataclass,
)
from typing import (
    Callable,
)


@dataclass
class BuiltinAssertion:
    """Basic Builtin Assertion base class

    `_assertion_function` is the assertion method from the `unittest` library.
    """

    _assertion_function: Callable

    def __call__(self, *args, **kwargs) -> None:
        """Run the Assertion function with the given args and kwargs

        Args:
            *args: Arguments that will be passed to the `_assertion_function`
            **kwargs: Keyword arguments to be passed to the
            `_assertion_function`

        Returns:
            None
        """
        self._assertion_function(*args, **kwargs)
