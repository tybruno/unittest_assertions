from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Any, Optional
from abc import abstractmethod
from string import Template


class AbstractAssertion:
    def __init__(
        self,
        function: Callable,
    ):
        ...

    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...


@dataclass
class BuiltinAssertion(AbstractAssertion):
    _function: Callable
    msg: Optional[Any] = field(default=None)

    def __call__(self, *args, **kwargs):
        if "msg" not in kwargs:
            msg = self.msg
            if isinstance(msg, Template):
                msg = msg.substitute(kwargs)
            kwargs["msg"] = msg
        self._function(*args, **kwargs)
