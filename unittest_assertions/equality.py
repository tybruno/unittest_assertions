""" Equality Assertions

Objects provided by this module:
    * `AssertEqual`: `assert first == second`
    * `AssertNotEqual`: `assert first != second`
    * `AssertAlmostEqual`: `assert first ~= second`
    * `AssertNotAlmostEqual`: `assert first !~= second`
    * `AssertCountEqual`: `assert len(first) == len(second)`
    * `AssertMultilineEqual`: `assert first.splitlines() == second.splitlines()`
    * `AssertSequenceEqual`: `assert seq1 == seq2`
    * `AssertListEqual`: `assert list1 == list2`
    * `AssertTupleEqual`: `assert tuple1 == tuple2`
    * `AssertSetEqual`: `assert seq1 == seq2`
    * `AssertDictEqual`: `assert dict1 == dict2`
    * `AssertLess`: `assert a < b`
    * `AssertLessEqual`: `assert a <= b`
    * `AssertGreater`: `assert a > b`
    * `AssertGreaterEqual`: `assert a>= b`
"""
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
    Any,
    Sequence,
    Type,
    List,
    Tuple,
    Set,
    Dict,
    Iterable,
)
from unittest import TestCase

from unittest_assertions.base import Assertion


@dataclass
class AssertEqual(Assertion):
    """`assert first == second`

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

    def __call__(
        self,
        first: Any,
        second: Any,
    ) -> None:
        """Assert equality comparison on the `first` and `second`

        Args:
            first: will be compared against `second`
            second: will be compared against `first`
        """
        super().__call__(first=first, second=second)


@dataclass
class AssertNotEqual(AssertEqual):
    """`assert first != second`

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
class AssertAlmostEqual(Assertion):
    """`assert first ~= second`

    raise `AssertionError` if `first` is not almost equal to `second`

    For more documentation read TestCase().assertAlmostEqual.__doc__

    Fail if the two objects are unequal as determined by their
    difference rounded to the given number of decimal places
    (default 7) and comparing to zero, or by comparing that the
    difference between the two objects is more than the given
    delta.

    Note that decimal places (from zero) are usually not the same
    as significant digits (measured from the most significant digit).

    If the two objects compare equal then they will automatically
    compare almost equal.

    Example:
        >>> assert_almost_equal = AssertAlmostEqual()
        >>> assert_almost_equal(1.00000001, 1.0)
        >>> assert_almost_equal(first=1.1, second=1.0, places=None, delta=0.5)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertAlmostEqual, init=False
    )

    def __call__(
        self, first: Any, second: Any, places: int = None, delta: float = None
    ) -> None:
        """Assert `first` almost equals `second`

        For more documentation read unittest.TestCase.assertSequenceEqual.__doc__

        Args:
            first: will be checked if it almost equals `second`
            second: will be checked if it almost equals `first`
            places: precision of decimal places
            delta: the amount of acceptable difference
        """
        super().__call__(
            first=first, second=second, places=places, delta=delta
        )


@dataclass
class AssertNotAlmostEqual(AssertAlmostEqual):
    """`assert first !~= second`

    raise `AssertionError` if `first` is almost  equal to `second`

    For more documentation read TestCase().assertNotAlmostEqual.__doc__
    Fail if the two objects are equal as determined by their
    difference rounded to the given number of decimal places
    (default 7) and comparing to zero, or by comparing that the
    difference between the two objects is less than the given delta.

    Note that decimal places (from zero) are usually not the same
    as significant digits (measured from the most significant digit).

    Objects that are equal automatically fail.

    Example:
        >>> assert_not_almost_equal = AssertNotAlmostEqual()
        >>> assert_not_almost_equal(1.00000001, 2.0)
        >>> assert_not_almost_equal(first=1.1,second= 1.0,
        ... places=None, delta=0.05)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotAlmostEqual, init=False
    )


@dataclass
class AssertCountEqual(Assertion):
    """`assert Counter(list(first) == Counter(list(second))`

    Asserts that two iterables have the same elements, the same number of
    times, without regard to order.

    raise `AssertionError` if `first` counter does not equal `second` counter

    For more documentation read TestCase().assertCountEqual.__doc__

    Example:
        >>> assert_count_equal = AssertCountEqual()
        >>> assert_count_equal([0, 1, 1],(1, 0, 1))
    """

    _assertion_function: Callable = field(
        default=TestCase().assertCountEqual, init=False
    )

    def __call__(
        self,
        first: Iterable,
        second: Iterable,
    ) -> None:
        """Assert equality comparison on the `first` and `second`

        Args:
            first: will be compared against `second`
            second: will be compared against `first`
        """
        super().__call__(first=first, second=second)


@dataclass
class AssertMultilineEqual(AssertEqual):
    """`assert first.splitlines() == second.splitlines()`

    raise `AssertionError` if `first` multiline string does not equal
     `second` multiline string

    For more documentation read TestCase().assertMultiLineEqual.__doc__

    Example:
        >>> multiline = 'line1\\nline2'
        >>> assert_multiline_equal = AssertMultilineEqual()
        >>> assert_multiline_equal(first=multiline,second=multiline)

    """

    _assertion_function: Callable = field(
        default=TestCase().assertMultiLineEqual, init=False
    )

    def __call__(
        self,
        first: str,
        second: str,
    ) -> None:
        """Assert equality comparison on the `first` and `second`

        Args:
            first: will be compared against `second`
            second: will be compared against `first`
        """
        super().__call__(first=first, second=second)


@dataclass
class AssertSequenceEqual(Assertion):
    """`assert seq1 == seq2`

    An equality assertion for ordered sequences (like lists and tuples).

    For the purposes of this function, a valid ordered sequence type is one
    which can be indexed, has a length, and has an equality operator.

    raise `AssertionError` if `seq1` is not equal to `seq2`

    For more documentation read TestCase().assertSequenceEqual.__doc__

    Example:
        >>> assert_sequence_equal = AssertSequenceEqual()
        >>> assert_sequence_equal((1,2.5),[1,2.5])
    """

    _assertion_function: Callable = field(
        default=TestCase().assertSequenceEqual, init=False
    )

    def __call__(
        self, seq1: Sequence, seq2: Sequence, seq_type: Type = None
    ) -> None:
        """An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.

        Returns:
            None
        """
        super().__call__(seq1=seq1, seq2=seq2, seq_type=seq_type)


@dataclass
class AssertListEqual(Assertion):
    """`assert list1 == list2`

    raise `AssertionError` if `list1` is not equal to `list2`

    For more documentation read TestCase().assertListEqual.__doc__

    Example:
        >>> _list = [1,2,3.5]
        >>> assert_list_equal = AssertListEqual()
        >>> assert_list_equal(_list,_list)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertListEqual, init=False
    )

    def __call__(self, list1: List, list2: List) -> None:
        """assert `list1` is deep equal to `list2`

        Args:
            list1: check if equal to `list2`
            list2: check if equal to `list1`
        """
        super().__call__(list1=list1, list2=list2)


@dataclass
class AssertTupleEqual(Assertion):
    """`assert tuple1 == tuple2`

    raise `AssertionError` if `tuple1` is not equal to `tuple2`

    For more documentation read TestCase().assertTupleEqual.__doc__

    Example:
        >>> _tuple = (1,2,"hello")
        >>> assert_tuple_equal = AssertTupleEqual()
        >>> assert_tuple_equal(_tuple,_tuple)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertTupleEqual, init=False
    )

    def __call__(self, tuple1: Tuple, tuple2: Tuple) -> None:
        """assert `tuple1` deep equals `tuple2`

        Args:
            tuple1: check if equal to `tuple2`
            tuple2: check if equal to `tuple1`
        """
        super().__call__(tuple1=tuple1, tuple2=tuple2)


@dataclass
class AssertSetEqual(Assertion):
    """`assert seq1 == seq2`

    raise `AssertionError` if `set1` is not equal to `set2`

    For more documentation read TestCase().assertSetEqual.__doc__

    Example:
        >>> _set = {1,2,5}
        >>> assert_set_equal = AssertSetEqual()
        >>> assert_set_equal(_set,_set)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertSetEqual, init=False
    )

    def __call__(self, set1: Set, set2: Set) -> None:
        """assert `set1` is deep equal to `set2`

        Args:
            set1: checks if deep equal to `set2`
            set2: checks if deep equal to `set1`
        """
        super().__call__(set1=set1, set2=set2)


@dataclass
class AssertDictEqual(Assertion):
    """`assert dict1 == dict2`

    raise `AssertionError` if `dict1` is not equal to `dict2`

    For more documentation read TestCase().assertDictEqual.__doc__

    Example:
        >>> _dict = {"a": 1, "b":2}
        >>> assert_dict_equal = AssertDictEqual()
        >>> assert_dict_equal(_dict,_dict)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertDictEqual, init=False
    )

    def __call__(self, d1: Dict, d2: Dict) -> None:
        """assert `dict1` is deep equal to `dict2`

        Args:
            d1: checks if deep equal to `d2`
            d2: checks if deep equal to `d1`
        """
        super().__call__(d1=d1, d2=d2)


@dataclass
class ComparisonAssertion(Assertion):
    """Parent class for Comparison Assertions"""

    def __call__(self, a: Any, b: Any) -> None:
        """Compares `a` with `b`
        Args:
            a: compares to `b`
            b: compares to `a`

        Returns:
            `True` if `a` and `b` pass comparison
        """
        super().__call__(a=a, b=b)


@dataclass
class AssertLess(ComparisonAssertion):
    """`assert a < b`

    raise `AssertionError` if `a` is less than or equal `b`

    For more documentation read TestCase().assertLess.__doc__

    Example:
        >>> assert_less = AssertLess()
        >>> assert_less(1,2)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertLess, init=False
    )


@dataclass
class AssertLessEqual(ComparisonAssertion):
    """`assert a <= b`

    raise `AssertionError` if `a` is greater than `b`

    For more documentation read TestCase().assertLessEqual.__doc__

    Example:
        >>> assert_less = AssertLessEqual()
        >>> assert_less(1,2)
        >>> assert_less(2,2)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertLessEqual, init=False
    )


@dataclass
class AssertGreater(ComparisonAssertion):
    """`assert a > b`

    raise `AssertionError` if `a` is less than or equal to `b`

    For more documentation read TestCase().assertGreater.__doc__

    Example:
        >>> assert_greater = AssertGreater()
        >>> assert_greater(2,1)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertGreater, init=False
    )


@dataclass
class AssertGreaterEqual(ComparisonAssertion):
    """`assert a >= b`

    raise `AssertionError` if `a` is less than `b`

    For more documentation read TestCase().assertGreaterEqual.__doc__

    Example:
        >>> assert_greater_equal = AssertGreaterEqual()
        >>> assert_greater_equal(2,1)
        >>> assert_greater_equal(2,2)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertGreaterEqual, init=False
    )
