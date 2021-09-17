from typing import Type

import pytest

from unittest_assertions.base import (
    BasicBuiltinAssertion,
    BuiltinAssertion,
)


class BasicAsssertionTester:
    _assertion: Type[BasicBuiltinAssertion]

    def test_assertion_passes(self, *args, **kwargs):
        assertion = self._assertion()
        assertion(*args, **kwargs)

    def test_assertion_raises(self, *args, **kwargs):
        assertion = self._assertion()
        with pytest.raises(AssertionError):
            assertion(*args, **kwargs)


class AssertionTester:
    _assertion: Type[BuiltinAssertion]

    @pytest.mark.parametrize("msg", ("message", None, 2))
    def test_init(self, msg):
        assertion = self._assertion(msg=msg)
        assert assertion.msg == msg

    def test_assertion_passes(self, *args, **kwargs):
        assertion = self._assertion()
        assertion(*args, **kwargs)

    def test_assertion_raises(self, *args, **kwargs):
        assertion = self._assertion()
        with pytest.raises(AssertionError):
            assertion(*args, **kwargs)