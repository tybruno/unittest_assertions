from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Any, Optional
from abc import abstractmethod


class AbstractAssertion:
    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...


@dataclass
class BasicBuiltinAssertion(AbstractAssertion):
    _function: Callable

    def __call__(self, *args, **kwargs):
        self._function(*args, **kwargs)


@dataclass
class BuiltinAssertion(BasicBuiltinAssertion):
    msg: Optional[Any] = field(default=None)

    def __call__(self, *args, **kwargs):
        if "msg" not in kwargs:
            msg = self.msg
            kwargs["msg"] = msg

        super().__call__(*args, **kwargs)
