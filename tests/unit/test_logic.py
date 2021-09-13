import pytest

from tests.base import AssertionTester
from tests.conftest import ALL_BASIC_TYPES_1
from unittest_assertions.logic import (
    AssertFalse,
    AssertTrue,
)


class TestAssertTrue(AssertionTester):
    _assertion = AssertTrue

    @pytest.mark.parametrize(
        "testing_data", tuple(value for value in ALL_BASIC_TYPES_1.values())
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize("testing_data", (False, 0, None, "", []))
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertFalse(AssertionTester):
    _assertion = AssertFalse

    @pytest.mark.parametrize("testing_data", (False, 0, None, "", []))
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data", tuple(value for value in ALL_BASIC_TYPES_1.values())
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)
