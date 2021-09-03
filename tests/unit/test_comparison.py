from abc import abstractmethod

from unittest_assertions.comparison import (
    EqualityAssertion,
    AssertEqual,
    AssertNotEqual,
    AssertAlmostEqual,
    AssertNotAlmostEqual,
    AssertCountEqual,
)

from tests.conftest import (
    combined_equal_all_basic_types,
    combined_non_equal_all_basic_types,
)
import pytest


class TestAssertEqual:
    @pytest.mark.parametrize(
        "equal_data",
        tuple(combined_equal_all_basic_types()),
    )
    @pytest.mark.parametrize("msg", ("message", None, 2))
    def test_assert_equal_passes(self, msg, equal_data):
        assert_equal = AssertEqual(msg=msg)
        assert assert_equal.msg == msg
        assert_equal(*equal_data)

    @pytest.mark.parametrize(
        "unequal_data",
        tuple(combined_non_equal_all_basic_types()),
    )
    @pytest.mark.parametrize("msg", ("message", None, 2))
    def test_assert_equal_raises_assertion(self, msg, unequal_data):
        assert_equal = AssertEqual(msg=msg)
        assert assert_equal.msg == msg
        with pytest.raises(AssertionError):
            assert_equal(*unequal_data)


class TestAssertNotEqual:
    @pytest.mark.parametrize(
        "unequal_data",
        tuple(combined_non_equal_all_basic_types()),
    )
    @pytest.mark.parametrize("msg", ("message", None, 2))
    def test_assert_equal_passes(self, msg, unequal_data):
        assert_not_equal = AssertNotEqual(msg=msg)
        assert assert_not_equal.msg == msg
        assert_not_equal(*unequal_data)

    @pytest.mark.parametrize(
        "equal_data",
        tuple(combined_equal_all_basic_types()),
    )
    @pytest.mark.parametrize("msg", ("message", None, 2))
    def test_assert_equal_raises_assertion(self, msg, equal_data):
        assert_not_equal = AssertNotEqual(msg=msg)
        assert assert_not_equal.msg == msg
        with pytest.raises(AssertionError):
            assert_not_equal(*equal_data)
