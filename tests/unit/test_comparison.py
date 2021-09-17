""" Testing unittest_assertions/comparison.py """
import pytest

from tests.base import AssertionTester
from tests.conftest import (
    BASIC_CONTAINERS_1,
    BASIC_CONTAINERS_2,
    MULTILINE_1,
    MULTILINE_2,
    combined_equal_all_basic_types,
    combined_non_equal_all_basic_types,
    equal_lists,
    equal_sequences,
    non_equal_list,
    not_equal_sequences,
)
from unittest_assertions.comparison import (
    AssertAlmostEqual,
    AssertCountEqual,
    AssertDictEqual,
    AssertEqual,
    AssertGreater,
    AssertGreaterEqual,
    AssertLess,
    AssertLessEqual,
    AssertListEqual,
    AssertMultilineEqual,
    AssertNotAlmostEqual,
    AssertNotEqual,
    AssertSequanceEqual,
    AssertSetEqual,
    AssertTupleEqual,
)


class TestAssertEqual(AssertionTester):
    _assertion = AssertEqual

    @pytest.mark.parametrize(
        "testing_data",
        combined_equal_all_basic_types(),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        combined_non_equal_all_basic_types(),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertNotEqual(AssertionTester):
    _assertion = AssertNotEqual

    @pytest.mark.parametrize(
        "testing_data",
        combined_non_equal_all_basic_types(),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        combined_equal_all_basic_types(),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAlmostEqual(AssertionTester):
    _assertion = AssertAlmostEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1.00000001, 1.0),
            (0, 0.1 + 0.1j, 0, None),
            (float("inf"), float("inf")),
            (1.1, 1.0, None, 0.5),
            (1.1, 1.1, None, 0.5),
        ),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1.00000001, 2.0),
            (0, 0.1 + 0.1j, 1),
            (1.1, 1.0, None, 0.05),
        ),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


class TestNotAlmostEqual(AssertionTester):
    _assertion = AssertNotAlmostEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1.00000001, 2.0),
            (0, 0.1 + 0.1j, 1),
            (1.1, 1.0, None, 0.05),
        ),
    )
    def test_assertion_passes(self, testing_data: tuple):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1.00000001, 1.0),
            (0, 0.1 + 0.1j, 0),
            (float("inf"), float("inf")),
            (1.1, 1.0, None, 0.5),
            (1.1, 1.1, None, 0.5),
        ),
    )
    def test_assertion_raises(self, testing_data: tuple):
        super().test_assertion_raises(*testing_data)


class TestAssertCountEqual(AssertionTester):
    _assertion = AssertCountEqual

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (container, container) for container in BASIC_CONTAINERS_1.values()
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (container1, container2)
            for container1, container2 in zip(
                BASIC_CONTAINERS_1.values(),
                BASIC_CONTAINERS_2.values(),
            )
            if not isinstance(container1, dict)
            and not isinstance(container2, dict)
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertMultilineEqual(AssertionTester):
    _assertion = AssertMultilineEqual

    @pytest.mark.parametrize(
        "testing_data",
        ((MULTILINE_1, MULTILINE_1),),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize("testing_data", ((MULTILINE_1, MULTILINE_2),))
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertSequenceEqual(AssertionTester):
    _assertion = AssertSequanceEqual

    @pytest.mark.parametrize(
        "testing_data",
        equal_sequences(),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        not_equal_sequences(),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertListEqual(AssertionTester):
    _assertion = AssertListEqual

    @pytest.mark.parametrize(
        "testing_data",
        (equal_lists(),),
    )
    def test_assertion_passes(self, testing_data):
        print(testing_data)
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (non_equal_list(),),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertTupleEqual(AssertionTester):
    _assertion = AssertTupleEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                BASIC_CONTAINERS_1[tuple],
                BASIC_CONTAINERS_1[tuple],
            ),
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (tup1, tup2)
            for tup1, tup2 in zip(
                BASIC_CONTAINERS_1[tuple], BASIC_CONTAINERS_2[tuple]
            )
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertSetEqual(AssertionTester):
    _assertion = AssertSetEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                BASIC_CONTAINERS_1[set],
                BASIC_CONTAINERS_1[set],
            ),
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (set1, set2)
            for set1, set2 in zip(
                BASIC_CONTAINERS_1[set], BASIC_CONTAINERS_2[set]
            )
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertDictEqual(AssertionTester):
    _assertion = AssertDictEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (
                BASIC_CONTAINERS_1[dict],
                BASIC_CONTAINERS_1[dict],
            ),
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (dict1, dict2)
            for dict1, dict2 in zip(
                BASIC_CONTAINERS_1[dict], BASIC_CONTAINERS_2[dict]
            )
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertLess(AssertionTester):
    _assertion = AssertLess

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (2, 1),
            (2, 2),
            (2, -1),
            (1.2, 1.1),
            (
                "string",
                "str",
            ),
            ([2], []),
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertLessEqual(AssertionTester):
    _assertion = AssertLessEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (1, 2),
            (-1, 2),
            (1.1, 1.2),
            (1, 1),
            (1.1, 1.1),
            ("s", "s"),
            ("str", "string"),
            ([], [2]),
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (
            (2, 1),
            (2, -1),
            (1.2, 1.1),
            (
                "string",
                "str",
            ),
            ([2], []),
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertGreater(AssertionTester):
    _assertion = AssertGreater

    @pytest.mark.parametrize(
        "testing_data",
        (
            (2, 1),
            (2, -1),
            (1.2, 1.1),
            (
                "string",
                "str",
            ),
            ([2], []),
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)


class TestAssertGreaterEqual(AssertionTester):
    _assertion = AssertGreaterEqual

    @pytest.mark.parametrize(
        "testing_data",
        (
            (2, 1),
            (1, 1),
            (2, -1),
            (1.2, 1.1),
            (1.1, 1.1),
            (
                "string",
                "str",
            ),
            (
                "str",
                "str",
            ),
            ([2], []),
            ([2], [2]),
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(*testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(*testing_data)
