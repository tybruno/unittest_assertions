""" Testing unittest_assertions/regex.py """

import warnings

import pytest

from tests.base import BasicAssertionTester
from unittest_assertions.regex import (
    AssertNotRegex,
    AssertRaisesRegex,
    AssertRegex,
    AssertWarnsRegex,
)


def _raise(e):
    raise e


class TestAssertRaisesRegex(BasicAssertionTester):
    _assertion = AssertRaisesRegex

    @pytest.mark.parametrize(
        "testing_data",
        ((ValueError, "invalid literal for.*XYZ'$", int, "XYZ"),),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((ValueError, "invalid literal for.*XYZ'$", int, ""),),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


def _legacy_function(msg, warning):
    warnings.warn(msg, warning)


class TestAssertWarnsRegex(BasicAssertionTester):
    _assertion = AssertWarnsRegex

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                DeprecationWarning,
                r"deprecated",
                _legacy_function,
                r"legacy_function\(\) is deprecated",
                DeprecationWarning,
            ),
        ),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                DeprecationWarning,
                r"deprecated",
                _legacy_function,
                r"legacy_function\(\) is deprecated",
                BytesWarning,
            ),
            (
                DeprecationWarning,
                r"wrong",
                _legacy_function,
                r"legacy_function\(\) is deprecated",
                DeprecationWarning,
            ),
        ),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


class TestAssertRegex(BasicAssertionTester):
    _assertion = AssertRegex

    @pytest.mark.parametrize(
        "testing_data",
        (("Ala ma kota", r"k.t"),),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (("Ala ma kota", r"r+"),),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


class TestAssertNotRegex(BasicAssertionTester):
    _assertion = AssertNotRegex

    @pytest.mark.parametrize(
        "testing_data",
        (("Ala ma kota", r"r+"),),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (("Ala ma kota", r"k.t"),),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)