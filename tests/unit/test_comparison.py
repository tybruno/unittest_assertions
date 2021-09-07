from abc import abstractmethod
from typing import Type
from unittest_assertions.comparison import (
    EqualityAssertion,
    AssertEqual,
    AssertNotEqual,
    AssertAlmostEqual,
    AssertNotAlmostEqual,
    AssertDictEqual,
    AssertSetEqual,
    AssertTupleEqual,
    AssertCountEqual,
    AssertSequanceEqual,
    AssertListEqual,
    AssertLess,
    AssertLessEqual,
    AssertGreater,
    AssertGreaterEqual,
    AssertMultilineEqual,
)

from tests.conftest import (
    BASIC_CONTAINERS_1,
    BASIC_CONTAINERS_2,
    combined_equal_all_basic_types,
    combined_non_equal_all_basic_types,
    equal_sequences,
    not_equal_sequences,
    equal_lists,
    non_equal_list,
    MULTILINE_1,
    MULTILINE_2,
)
import pytest


class ComparisonTester:
    _assertion: Type[EqualityAssertion]

    @pytest.mark.parametrize("msg", ("message", None, 2))
    def test_init(self, msg):
        assertion = self._assertion(msg=msg)
        assert assertion.msg == msg

    def test_assertion_passes(self, testing_data):
        assertion = self._assertion()
        assertion(*testing_data)

    def test_assertion_raises(self, testing_data):
        assertion = self._assertion()
        with pytest.raises(AssertionError):
            assertion(*testing_data)


class TestAssertEqual(ComparisonTester):
    _assertion = AssertEqual

    @pytest.mark.parametrize(
        "testing_data",
        tuple(combined_equal_all_basic_types()),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(combined_non_equal_all_basic_types()),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertNotEqual(ComparisonTester):
    _assertion = AssertNotEqual

    @pytest.mark.parametrize(
        "testing_data",
        tuple(combined_non_equal_all_basic_types()),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(combined_equal_all_basic_types()),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertTupleEqual(ComparisonTester):
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
        super().test_assertion_passes(testing_data)

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
        super().test_assertion_raises(testing_data)


class TestAssertSetEqual(ComparisonTester):
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
        super().test_assertion_passes(testing_data)

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
        super().test_assertion_raises(testing_data)


class TestAssertDictEqual(ComparisonTester):
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
        super().test_assertion_passes(testing_data)

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
        super().test_assertion_raises(testing_data)


class TestAssertCountEqual(ComparisonTester):
    _assertion = AssertCountEqual

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (
                (container, container)
                for container in BASIC_CONTAINERS_1.values()
            )
        ),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(
            (
                (container1, container2)
                for container1, container2 in zip(
                    BASIC_CONTAINERS_1.values(),
                    BASIC_CONTAINERS_2.values(),
                )
                if not isinstance(container1, dict)
                and not isinstance(container2, dict)
            )
        ),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertSequenceEqual(ComparisonTester):
    _assertion = AssertSequanceEqual

    @pytest.mark.parametrize(
        "testing_data",
        tuple(equal_sequences()),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        tuple(not_equal_sequences()),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertListEqual(ComparisonTester):
    _assertion = AssertListEqual

    @pytest.mark.parametrize(
        "testing_data",
        (equal_lists(),),
    )
    def test_assertion_passes(self, testing_data):
        print(testing_data)
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        (non_equal_list(),),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertLess(ComparisonTester):
    _assertion = AssertLess

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

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
        super().test_assertion_raises(testing_data)


class TestAssertLessEqual(ComparisonTester):
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
        super().test_assertion_passes(testing_data)

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
        super().test_assertion_raises(testing_data)


class TestAssertGreater(ComparisonTester):
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
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertGreaterEqual(ComparisonTester):
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
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize(
        "testing_data",
        ((1, 2), (-1, 2), (1.1, 1.2), ("str", "string"), ([], [2])),
    )
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)


class TestAssertMultilineEqual(ComparisonTester):
    _assertion = AssertMultilineEqual

    @pytest.mark.parametrize(
        "testing_data",
        ((MULTILINE_1, MULTILINE_1),),
    )
    def test_assertion_passes(self, testing_data):
        super().test_assertion_passes(testing_data)

    @pytest.mark.parametrize("testing_data", ((MULTILINE_1, MULTILINE_2),))
    def test_assertion_raises(self, testing_data):
        super().test_assertion_raises(testing_data)
