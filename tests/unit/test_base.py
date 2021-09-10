import pytest

from unittest_assertions.base import BuiltinAssertion
from unittest_assertions.comparison import AssertEqual
from string import Template


class TestBuiltinAssertion:
    @pytest.mark.parametrize("msg", (None, "Hello"))
    @pytest.mark.parametrize("function", (AssertEqual,))
    def test_init(self, msg, function):
        bulitin_assertion = BuiltinAssertion(msg=msg, _function=AssertEqual)
        assert bulitin_assertion._function == function
        assert bulitin_assertion.msg == msg

    @pytest.mark.parametrize("msg", (None, "Hello", Template("msg $a  $b")))
    @pytest.mark.parametrize("arguments", (("hello", None, 2),))
    @pytest.mark.parametrize(
        "keyword_args",
        ({"testing": "hello there"}, {"msg": "message"}, {"a": 1, "b": 2}),
    )
    def test_call(self, msg, arguments: list, keyword_args: dict):
        def _mock_function(*_args, **_kwargs):
            nonlocal msg
            expected_msg = msg
            if isinstance(expected_msg, Template):
                expected_msg = expected_msg.safe_substitute(keyword_args)
            expected_keyword_args = {"msg": expected_msg}
            expected_keyword_args.update(keyword_args)
            assert arguments == _args
            assert expected_keyword_args == _kwargs

        bulitin_assertion = BuiltinAssertion(msg=msg, _function=_mock_function)
        bulitin_assertion.__call__(*arguments, **keyword_args)
