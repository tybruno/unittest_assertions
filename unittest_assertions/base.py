from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Any, Optional, Mapping, Sequence
from abc import abstractmethod, ABC
from string import Template


class AbstractAssertion(ABC):
    """Foundational Abstract Method for Assertions"""

    @abstractmethod
    def __call__(self, *args: Sequence, **kwargs: Mapping) -> None:
        """Method to run the assertion.

        Args:
            *args: Arguments to be passed to the Assertion function
            **kwargs: Keyword arguments to be passed to the Assertion Function

        Returns:
            None
        """
        ...


@dataclass
class BasicBuiltinAssertion(AbstractAssertion):
    """Basic Builtin Assertion base class

    `_assertion_function` is the assertion method from the `unittest` library.
    """

    _assertion_function: Callable

    def __call__(self, *args: Sequence, **kwargs: Mapping) -> None:
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
    """Buitlin Assertion base class for assertions that have a `msg` argument"""

    msg: Optional[Any] = field(default=None)

    def __call__(self, *args: Sequence, **kwargs: Mapping) -> None:
        """Run the Assertion function with the given args and kwargs

        Args:
            *args: Arguments that will be passed to the `_assertion_function`
            **kwargs: Keyword arguments to be passed to the `_assertion_function`

        Returns:
            None
        """
        if "msg" not in kwargs:
            msg: Any = self.msg

            # If it is a Template string substitute it with the kwargs
            if isinstance(msg, Template):
                msg: str = msg.safe_substitute(kwargs)
            kwargs["msg"] = msg

        super().__call__(*args, **kwargs)
