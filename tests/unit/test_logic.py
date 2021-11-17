""" Testing unittest_assertions/logic.py """

import pytest
from pytest_builtin_types import _ALL_BASIC_TYPES_1
from tests.base import AssertionTester

from unittest_assertions.logic import (
    AssertFalse,
    AssertTrue,
)


class TestAssertTrue(AssertionTester):
    _assertion = AssertTrue

    @pytest.mark.parametrize(
        "testing_data", tuple(value for value in _ALL_BASIC_TYPES_1.values())
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize("testing_data", (False, 0, None, "", []))
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(testing_data)


class TestAssertFalse(AssertionTester):
    _assertion = AssertFalse

    @pytest.mark.parametrize("testing_data", (False, 0, None, "", []))
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data", tuple(value for value in _ALL_BASIC_TYPES_1.values())
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(testing_data)