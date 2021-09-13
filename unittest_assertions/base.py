from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Any, Optional, Mapping, Iterable
from abc import abstractmethod, ABC
from string import Template


class AbstractAssertion(ABC):
    """Foundational Abstract Method for Assertions"""

    @abstractmethod
    def __call__(self, *args: Iterable, **kwargs: Mapping) -> None:
        """Method to run the assertion.

        Args:
            *args: Arguments to be ran on the Assertion function
            **kwargs: Keyword arguments to be ran on the Assertion Function

        Returns:
            None
        """
        ...


@dataclass
class BasicBuiltinAssertion(AbstractAssertion):
    """Basic Builtin Assertion

    `_assertion_function` is the assertion method from the `unittest` library.
    """

    _assertion_function: Callable

    def __call__(self, *args: Iterable, **kwargs: Mapping) -> None:
        """Run the Assertion function with the given args and kwargs.

        Args:
            *args: Arguments that will be passed to the `_assertion_function`
            **kwargs: Keyword arguments to be passed to the `_assertion_function`

        Returns:
            None
        """
        self._assertion_function(*args, **kwargs)


@dataclass
class BuiltinAssertion(BasicBuiltinAssertion):
    msg: Optional[Any] = field(default=None)

    def __call__(self, *args, **kwargs):
        if "msg" not in kwargs:
            msg = self.msg
            if isinstance(msg, Template):
                msg = msg.safe_substitute(kwargs)
            kwargs["msg"] = msg
        super().__call__(*args, **kwargs)
