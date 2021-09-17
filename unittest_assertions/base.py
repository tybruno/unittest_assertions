""" Base classes and Abstract Base Classes """
from dataclasses import (
    dataclass,
    field,
)
from string import Template
from typing import (
    Any,
    Callable,
    Optional,
)


@dataclass
class BasicBuiltinAssertion:
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


@dataclass
class BuiltinAssertion(BasicBuiltinAssertion):
    """Buitlin Assertion base class for assertions that have a `msg` argument

    Attributes:
        msg: Optional message that will be included when `AssertionError` is
        raised.
    """

    msg: Optional[Any] = field(default=None)

    def __call__(self, *args, **kwargs) -> None:
        """Run the Assertion function with the given args and kwargs

        Args:
            *args: Arguments that will be passed to the `_assertion_function`
            **kwargs: Keyword arguments to be passed to the
            `_assertion_function`

        Returns:
            None
        """
        if "msg" not in kwargs:
            msg: Any = self.msg

            # If it is a Template string substitute it with the function_kwargs
            if isinstance(msg, Template):
                msg = msg.safe_substitute(kwargs)
            kwargs["msg"] = msg

        super().__call__(*args, **kwargs)
