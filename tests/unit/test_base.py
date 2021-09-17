""" Testing unittest_assertions/base.py """
from string import Template
from typing import (
    Any,
    Callable,
    Iterable,
    Mapping,
)

import pytest

from unittest_assertions.base import BuiltinAssertion
from unittest_assertions.comparison import AssertEqual


class TestBuiltinAssertion:
    """Testing builtin assertions"""

    @pytest.mark.parametrize("msg", (None, "Hello"))
    @pytest.mark.parametrize("function", (AssertEqual,))
    def test_init(self, msg: Any, function: Callable) -> None:
        """Test builtin assertion __init__

        Args:
            msg: message for BuiltinAssertion paramater
            function: function for BuiltinAssertion paramater

        Returns:
            None
        """
        bulitin_assertion = BuiltinAssertion(
            msg=msg, _assertion_function=AssertEqual
        )
        assert bulitin_assertion._assertion_function == function
        assert bulitin_assertion.msg == msg

    @pytest.mark.parametrize("msg", (None, "Hello", Template("msg $a  $b")))
    @pytest.mark.parametrize("arguments", (("hello", None, 2),))
    @pytest.mark.parametrize(
        "keyword_args",
        ({"testing": "hello there"}, {"msg": "message"}, {"a": 1, "b": 2}),
    )
    def test_call(
        self, msg: Any, arguments: Iterable, keyword_args: Mapping
    ) -> None:
        """Test `BuiltinAssertion` __call__ function

        Args:
            msg: Messages tested for the __call__
            arguments: arguments passed to __call__
            keyword_args: keyword arguments passed to __call__

        Returns:
            None
        """

        def _mock_function(*_args, **_kwargs) -> None:
            """mock function
            Args:
                *_args: arguments for the mocked function
                **_kwargs: keyword arguments for the mocked function

            Returns:
                None

            """
            nonlocal msg
            expected_msg = msg
            if isinstance(expected_msg, Template):
                expected_msg = expected_msg.safe_substitute(keyword_args)
            expected_keyword_args = {"msg": expected_msg}
            expected_keyword_args.update(keyword_args)
            assert arguments == _args
            assert expected_keyword_args == _kwargs

        bulitin_assertion = BuiltinAssertion(
            msg=msg, _assertion_function=_mock_function
        )
        bulitin_assertion.__call__(*arguments, **keyword_args)
