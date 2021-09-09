from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Any, Optional
from abc import abstractmethod
from string import Template


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
            if isinstance(msg, Template):
                msg = msg.substitute(kwargs)
            kwargs["msg"] = msg
        super().__call__(*args, **kwargs)
