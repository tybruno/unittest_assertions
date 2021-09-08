import pytest
from tests.base import AssertionTester
from unittest_assertions.identity import (
    AssertIs,
    AssertIsNot,
    AssertIsNone,
    AssertIsNotNone,
    AssertIsInstance,
    AssertNotIsInstance,
)
from tests.conftest import (
    ALL_BASIC_TYPES_1,
    ALL_BASIC_TYPES_2,
)


class TestIs(AssertionTester):
    _assertion = AssertIs

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value, value) for value in ALL_BASIC_TYPES_1.values()),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (value1, value2)
            for value1, value2 in zip(
                ALL_BASIC_TYPES_1.values(), ALL_BASIC_TYPES_2.values()
            )
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestIsNot(AssertionTester):
    _assertion = AssertIsNot

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (value1, value2)
            for value1, value2 in zip(
                ALL_BASIC_TYPES_1.values(), ALL_BASIC_TYPES_2.values()
            )
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value, value) for value in ALL_BASIC_TYPES_1.values()),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertIsNone(AssertionTester):
    _assertion = AssertIsNone

    @pytest.mark.parametrize(
        "testing_data",
        ((None,),),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value,) for value in ALL_BASIC_TYPES_1.values()),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertIsNotNone(AssertionTester):
    _assertion = AssertIsNotNone

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value,) for value in ALL_BASIC_TYPES_1.values()),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((None,),),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertIsInstance(AssertionTester):
    _assertion = AssertIsInstance

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value, type_) for type_, value in ALL_BASIC_TYPES_1.items()),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    #
    # @pytest.mark.parametrize(
    #     "testing_data",
    #     tuple((value, type_) for type_, value in),
    # )
    def test_assertion_raises(self, testing_data):
        ...
        # super().test_assertion_raises(testing_data)


class TestAssertNotIsInstance(AssertionTester):
    _assertion = AssertNotIsInstance

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value, type_) for type_, value in ALL_BASIC_TYPES_1.items()),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)
