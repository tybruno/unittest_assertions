import pytest
from tests.base import BasicAsssertionTester
from unittest_assertions.regex import (
    AssertRaisesRegex,
    AssertWarnsRegex,
    AssertRegex,
    AssertNotRegex,
)


def _raise(e):
    raise e


# class TestAssertRaisesRegex(BasicAsssertionTester):
#     _assertion = AssertRaisesRegex
#
#     @pytest.mark.parametrize(
#         "testing_data",
#         (),
#     )
#     def test_assertion_passes(self, testing_data):
#         super().test_assertion_passes(*testing_data)
#
#     @pytest.mark.parametrize(
#         "testing_data",
#         ((ValueError, r"k.t", ValueError("hello"), ""),),
#     )
#     def test_assertion_raises(self, testing_data: tuple):
#         super().test_assertion_raises(*testing_data)
