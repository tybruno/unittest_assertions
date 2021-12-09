""" Testing unittest_assertions/base.py """
from typing import (
    Callable,
    Iterable,
    Mapping,
)

import pytest

from unittest_assertions.base import Assertion
from unittest_assertions.equality import AssertEqual


class TestBuiltinAssertion:
    """Testing builtin assertions"""

    @pytest.mark.parametrize("function", (AssertEqual,))
    def test_init(self, function: Callable) -> None:
        """Test builtin assertion __init__

        Args:
            function: function for Assertion paramater

        Returns:
            None
        """
        builtin_assertion = Assertion(_assertion_function=AssertEqual)
        assert builtin_assertion._assertion_function == function

    @pytest.mark.parametrize("arguments", (("hello", None, 2),))
    @pytest.mark.parametrize(
        "keyword_args",
        ({"testing": "hello there"}, {"a": 1, "b": 2}),
    )
    def test_call(self, arguments: Iterable, keyword_args: Mapping) -> None:
        """Test `Assertion` __call__ function

        Args:
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
            keyword_args["msg"] = builtin_assertion.msg
            assert arguments == _args
            assert keyword_args == _kwargs

        builtin_assertion = Assertion(_assertion_function=_mock_function)
        builtin_assertion.__call__(*arguments, **keyword_args)
