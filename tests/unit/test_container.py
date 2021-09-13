import pytest

from tests.base import AssertionTester
from tests.conftest import (
    ALL_BASIC_TYPES_1,
    ALL_BASIC_TYPES_2,
)
from unittest_assertions.container import (
    AssertIn,
    AssertNotIn,
)


class ContainerTester(AssertionTester):
    def test_assertion_passes(self, testing_data):
        assertion = self._assertion()
        member, container = testing_data
        assertion(member=member, container=container)

    def test_assertion_raises(self, testing_data):
        assertion = self._assertion()
        member, container = testing_data
        with pytest.raises(AssertionError):
            assertion(member=member, container=container)


class TestAssertIn(ContainerTester):
    _assertion = AssertIn

    @pytest.mark.parametrize(
        "testing_data",
        tuple((key, ALL_BASIC_TYPES_1) for key in ALL_BASIC_TYPES_1.keys()),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (value, ALL_BASIC_TYPES_1[tuple])
            for value in ALL_BASIC_TYPES_2[tuple]
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertNotIn(ContainerTester):
    _assertion = AssertNotIn

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (value, ALL_BASIC_TYPES_1[tuple])
            for value in ALL_BASIC_TYPES_2[tuple]
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple((key, ALL_BASIC_TYPES_1) for key in ALL_BASIC_TYPES_1.keys()),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)
