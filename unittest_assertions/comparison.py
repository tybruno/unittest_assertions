from dataclasses import (
    dataclass,
    field,
)
from typing import Any, Callable, Sequence, Mapping, Union
from unittest import TestCase

from unittest_assertions.base import BuiltinAssertion


@dataclass
class EqualityAssertion(BuiltinAssertion):
    """Parent class for Equality Assertions"""

    def __call__(
        self, first: Any, second: Any, *args: Sequence, **kwargs: Mapping
    ) -> None:
        """Run the `_assertion_function`.

        Args:
            first: First item that will be passed to the `_assertion_function`
            second: Second item that will be passed to the `_assertion_function`
            *args: Arguments to be passed to the Assertion function
            **kwargs: Keyword arguments to be passed to the Assertion Function

        Returns:
            None
        """
        super().__call__(first=first, second=second, *args, **kwargs)


@dataclass
class AssertEqual(EqualityAssertion):
    """assert `first` `==` `second`

    raise `AssertionError` if `first` is not equal to `second`

    For more documentation read TestCase().assertEqual.__doc__

    Example:
        >>> assert_equal = AssertEqual()
        >>> assert_equal(1,1)
        >>> assert_equal(first="hello",second="hello")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertEqual, init=False
    )


@dataclass
class AssertNotEqual(EqualityAssertion):
    """assert `first` `!=` `second`

    raise `AssertionError` if `first` is equal to `second`

    For more documentation read TestCase().assertNotEqual.__doc__

    Example:
        >>> assert_equal = AssertNotEqual()
        >>> assert_equal(1,2)
        >>> assert_equal(first="hello",second="goodbye")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotEqual, init=False
    )


@dataclass
class AssertAlmostEqual(EqualityAssertion):
    """assert `first` `~=` `second`

    raise `AssertionError` if `first` is not almost equal to `second`

    For more documentation read TestCase().assertAlmostEqual.__doc__

    Example:
        >>> assert_almost_equal = AssertAlmostEqual()
        >>> assert_almost_equal(1.00000001, 1.0)
        >>> assert_almost_equal(first=1.1, second=1.0, float=None, delta=0.5)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertAlmostEqual, init=False
    )

    def __call__(
        self,
        first: Any,
        second: Any,
        places: Any = None,
        delta: Any = None,
    ) -> None:
        """assert `first` almost equals `second`

        Args:
            first: object that will be compared with second
            second: object that will be compared with second
            places: The difference rounded to the given decimal places
            (default: 7 decimal places)
            delta: The amount of differnece that will raise the
            `AssertionError`

        Returns:
            None
        """
        super().__call__(
            first=first, second=second, places=places, delta=delta
        )


@dataclass
class AssertNotAlmostEqual(AssertAlmostEqual):
    """assert `first` `!~=` `second`

    raise `AssertionError` if `first` is almost  equal to `second`

    For more documentation read TestCase().assertNotAlmostEqual.__doc__

    Example:
        >>> assert_not_almost_equal = AssertNotAlmostEqual()
        >>> assert_not_almost_equal(1.00000001, 2.0)
        >>> assert_not_almost_equal(first=1.1,second= 1.0, places=None, delta=0.05)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotAlmostEqual, init=False
    )


@dataclass
class AssertCountEqual(EqualityAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertCountEqual, init=False
    )


@dataclass
class AssertMultilineEqual(EqualityAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertMultiLineEqual, init=False
    )


@dataclass
class AssertSequanceEqual(BuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertSequenceEqual, init=False
    )

    def __call__(self, seq1, seq2):
        super().__call__(seq1=seq1, seq2=seq2)


@dataclass
class AssertListEqual(BuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertListEqual, init=False
    )

    def __call__(self, list1, list2):
        super().__call__(list1=list1, list2=list2)


@dataclass
class AssertTupleEqual(BuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertTupleEqual, init=False
    )

    def __call__(self, tuple1, tuple2):
        super().__call__(tuple1=tuple1, tuple2=tuple2)


@dataclass
class AssertSetEqual(BuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertSetEqual, init=False
    )

    def __call__(self, set1, set2):
        super().__call__(set1=set1, set2=set2)


@dataclass
class AssertDictEqual(BuiltinAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertDictEqual, init=False
    )

    def __call__(self, d1, d2):
        super().__call__(d1=d1, d2=d2)


@dataclass
class ComparisonAssertion(BuiltinAssertion):
    def __call__(self, a, b):
        super().__call__(a=a, b=b)


@dataclass
class AssertLess(ComparisonAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertLess, init=False
    )


@dataclass
class AssertLessEqual(ComparisonAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertLessEqual, init=False
    )


@dataclass
class AssertGreater(ComparisonAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertGreater, init=False
    )


@dataclass
class AssertGreaterEqual(ComparisonAssertion):
    _assertion_function: Callable = field(
        default=TestCase().assertGreaterEqual, init=False
    )
