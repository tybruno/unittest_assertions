""" Testing unittest_assertions/identity.py """

import pytest
from pytest_builtin_types import equal_sequences, non_equal_sequences, _ALL_BASIC_TYPES_1, _NOT_INSTANCE_TESTING_DATA
from tests.base import AssertionTester

from unittest_assertions.identity import (
    AssertIs,
    AssertIsInstance,
    AssertIsNone,
    AssertIsNot,
    AssertIsNotNone,
    AssertNotIsInstance,
)


class TestIs(AssertionTester):
    _assertion = AssertIs

    @pytest.mark.parametrize(
        "testing_data",
        tuple(equal_sequences()),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            non_equal_sequences()
        ),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


class TestIsNot(AssertionTester):
    _assertion = AssertIsNot

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            non_equal_sequences()
        ),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(equal_sequences()),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


class TestAssertIsNone(AssertionTester):
    _assertion = AssertIsNone

    @pytest.mark.parametrize(
        "testing_data",
        ((None,),),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value,) for value in _ALL_BASIC_TYPES_1.values()),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


class TestAssertIsNotNone(AssertionTester):
    _assertion = AssertIsNotNone

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value,) for value in _ALL_BASIC_TYPES_1.values()),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((None,),),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


class TestAssertIsInstance(AssertionTester):
    _assertion = AssertIsInstance

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value, type_) for type_, value in _ALL_BASIC_TYPES_1.items()),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize("testing_data", tuple(_NOT_INSTANCE_TESTING_DATA))
    def test_assertion_raises(self, testing_data: tuple):
        obj, _type = testing_data
        if not isinstance(obj,_type):
            super().test_assertion_raises(obj,_type)


class TestAssertNotIsInstance(AssertionTester):
    _assertion = AssertNotIsInstance

    @pytest.mark.parametrize("testing_data", tuple(_NOT_INSTANCE_TESTING_DATA))
    def test_assertion_passes(self, testing_data: tuple):
        obj, _type = testing_data
        if isinstance(obj,_type):
            super().test_assertion_raises(obj,_type)

    @pytest.mark.parametrize(
        "testing_data",
        tuple((value, type_) for type_, value in _ALL_BASIC_TYPES_1.items()),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)