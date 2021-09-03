from unittest_assertions.comparison import (
    EqualityAssertion,
    AssertEqual,
    AssertNotEqual,
    AssertAlmostEqual,
    AssertNotAlmostEqual,
    AssertCountEqual,
)
from unittest import TestCase
import pytest


class TestAssertEqual:
    @pytest.mark.parametrize(
        "equal_data",
        (
            (1, 1),
            (-1.2, -1.2),
            ("string", "string"),
            (["list", 1], ["list", 1]),
        ),
    )
    @pytest.mark.parametrize("msg", ("message", None, 2))
    def test_assert_equal_passes(self, msg, equal_data):

        assert_equal = AssertEqual(msg=msg)
        assert assert_equal.msg == msg
        assert_equal(*equal_data)

    @pytest.mark.parametrize(
        "unequal_data",
        (
            (1, 2),
            (-1.2, -1.29),
            ("string", "string2"),
            (["list", 1], ["list2", 2]),
        ),
    )
    @pytest.mark.parametrize("msg", ("message", None, 2))
    def test_assert_equal_raises_assertion(self, msg, unequal_data):

        assert_equal = AssertEqual(msg=msg)
        assert assert_equal.msg == msg
        with pytest.raises(AssertionError):
            assert_equal(*unequal_data)
