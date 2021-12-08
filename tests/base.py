from typing import Type

import pytest

from unittest_assertions.base import (
    Assertion,
)


class BasicAssertionTester:
    _assertion: Type[Assertion]

    def test_assertion_passes(self, *args, **kwargs):
        assertion = self._assertion()
        assertion(*args, **kwargs)

    def test_assertion_raises(self, *args, **kwargs):
        assertion = self._assertion()
        with pytest.raises(AssertionError):
            assertion(*args, **kwargs)


class AssertionTester:
    _assertion: Type[Assertion]

    def test_assertion_passes(self, *args, **kwargs):
        assertion = self._assertion()
        assertion(*args, **kwargs)

    def test_assertion_raises(self, *args, **kwargs):
        assertion = self._assertion()
        with pytest.raises(AssertionError):
            assertion(*args, **kwargs)
