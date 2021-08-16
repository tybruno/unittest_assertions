from unittest_assertions.base import BuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable, Any, Sequence
from unittest import TestCase


@dataclass
class EqualityAssertion(BuiltinAssertion):
    def __call__(self, first: Any, second: Any, **kwargs):
        super().__call__(first=first, second=second, **kwargs)


@dataclass
class AssertEqual(EqualityAssertion):
    function: Callable = field(default=TestCase().assertEqual, init=False)


@dataclass
class AssertNotEqual(EqualityAssertion):
    function: Callable = field(default=TestCase().assertNotEqual, init=False)


@dataclass
class AssertAlmostEqual(EqualityAssertion):
    function: Callable = field(
        default=TestCase().assertAlmostEqual, init=False
    )

    def __call__(self, first: Any, second: Any, places=None, delta=None):
        super().__call__(
            first=first, second=second, places=places, delta=delta
        )


@dataclass
class AssertNotAlmostEqual(AssertAlmostEqual):
    function: Callable = field(
        default=TestCase().assertNotAlmostEqual, init=False
    )


@dataclass
class AssertCountEqual(EqualityAssertion):
    function: Callable = field(default=TestCase().assertCountEqual, init=False)


@dataclass
class AssertMultilineEqual(EqualityAssertion):
    function: Callable = field(
        default=TestCase().assertMultiLineEqual, init=False
    )


@dataclass
class AssertSequanceEqual(BuiltinAssertion):
    function: Callable = field(
        default=TestCase().assertSequenceEqual, init=False
    )

    def __call__(self, seq1, seq2):
        super().__call__(seq1=seq1, seq2=seq2)


@dataclass
class AssertListEqual(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertListEqual, init=False)

    def __call__(self, list1, list2):
        super().__call__(list1=list1, list2=list2)


@dataclass
class AssertTupleEqual(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertTupleEqual, init=False)

    def __call__(self, tuple1, tuple2):
        super().__call__(tuple1=tuple1, tuple2=tuple2)


@dataclass
class AssertSetEqual(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertSetEqual, init=False)

    def __call__(self, set1, set2):
        super().__call__(set1=set1, set2=set2)


@dataclass
class AssertDictEqual(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertDictEqual, init=False)

    def __call__(self, dict1, dict2):
        super().__call__(dict1=dict1, dict2=dict2)


@dataclass
class ComparisonAssertion(BuiltinAssertion):
    def __call__(self, a, b):
        super().__call__(a=a, b=b)


@dataclass
class AssertLess(ComparisonAssertion):
    function: Callable = field(default=TestCase().assertLess, init=False)


@dataclass
class AssertLessEqual(ComparisonAssertion):
    function: Callable = field(default=TestCase().assertLessEqual, init=False)


@dataclass
class AssertGreater(ComparisonAssertion):
    function: Callable = field(default=TestCase().assertGreater, init=False)


@dataclass
class AssertGreaterEqual(ComparisonAssertion):
    function: Callable = field(
        default=TestCase().assertGreaterEqual, init=False
    )
