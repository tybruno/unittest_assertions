from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Union, Optional
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
    function: Callable
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, **kwargs):
        msg = self.msg
        if isinstance(msg, Template):
            msg = msg.substitute(kwargs)
        self.function(**kwargs, msg=msg)
