""" Equality and Comparison Assertions"""
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    Callable,
    Sequence,
    Mapping,
    List,
    Tuple,
    Set,
    Union,
)
from unittest import TestCase

from unittest_assertions.base import BuiltinAssertion


@dataclass
class EqualityAssertion(BuiltinAssertion):
    """Parent class for Equality Assertions"""

    def __call__(self, first: Any, second: Any, *args, **kwargs) -> None:
        """Run the `_assertion_function`

        Args:
            first: First item that will be passed to the `_assertion_function`
            second: Second item that will be passed to the
            `_assertion_function`
            *args: Arguments to be passed to the Assertion function
            **kwargs: Keyword arguments to be passed to the Assertion Function

        Returns:
            None
        """
        super().__call__(first=first, second=second, *args, **kwargs)


@dataclass
class AssertEqual(EqualityAssertion):
    """assert `first` == `second`

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
    """assert `first` != `second`

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
    """assert `first` ~= `second`

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
        places: Union[int, None] = None,
        delta: Union[float, None] = None,
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
    """assert `first` !~= `second`

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
    """assert `Counter(list(first))` ==  `Counter(list(second))`

    raise `AssertionError` if `first` counter does not equal `second` counter

    For more documentation read TestCase().assertCountEqual.__doc__

    Example:
        >>> assert_count_equal = AssertCountEqual()
        >>> assert_count_equal([1,2],(1,2))
    """

    _assertion_function: Callable = field(
        default=TestCase().assertCountEqual, init=False
    )


@dataclass
class AssertMultilineEqual(EqualityAssertion):
    """assert `first` multiline string == `second` multiline string

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


@dataclass
class AssertSequanceEqual(BuiltinAssertion):
    """assert `seq1` == `seq2`

    raise `AssertionError` if `seq1` is not equal to `seq2`

    For more documentation read TestCase().assertSequenceEqual.__doc__

    Example:
        >>> assert_sequence_equal = AssertSequanceEqual()
        >>> assert_sequence_equal((1,2.5),[1,2.5])
    """

    _assertion_function: Callable = field(
        default=TestCase().assertSequenceEqual, init=False
    )

    def __call__(self, seq1: Sequence, seq2: Sequence) -> None:
        """assert `seq1` == `seq2`

        Args:
            seq1: sequence that will be compared with `seq2`
            seq2: sequence that will be compared with `seq1`

        Returns:
            None
        """
        super().__call__(seq1=seq1, seq2=seq2)


@dataclass
class AssertListEqual(BuiltinAssertion):
    """assert `list1` == `list2`

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
        """assert `list1` == `list2`

        Args:
            list1: list that will be compared with `list2`
            list2: list that will be compared with `list1`

        Returns:
            None
        """
        super().__call__(list1=list1, list2=list2)


@dataclass
class AssertTupleEqual(BuiltinAssertion):
    """assert `tuple1` == `tuple2`

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
        """assert `tuple1` == `tuple2`

        Args:
            tuple1: tuple that will be compared with `tuple2`
            tuple2: tuple that will be compared with `tuple1`

        Returns:
            None
        """
        super().__call__(tuple1=tuple1, tuple2=tuple2)


@dataclass
class AssertSetEqual(BuiltinAssertion):
    """assert `set1` == `set2`

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
        """assert `set1` == `set2`

        Args:
            set1: set that will be compared with `set2`
            set2: set that will be compared with `set1`

        Returns:
            None
        """
        super().__call__(set1=set1, set2=set2)


@dataclass
class AssertDictEqual(BuiltinAssertion):
    """assert `dic1` == `dict2`

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

    def __call__(self, d1: Mapping, d2: Mapping) -> None:
        """assert `d1` == `d2`
        Args:
            d1: dictionary that will be compared with `d2`
            d2: dictionary that will be compared with `d1`

        Returns:
            None
        """
        super().__call__(d1=d1, d2=d2)


@dataclass
class ComparisonAssertion(BuiltinAssertion):
    """Parent class for Comparison Assertions"""

    def __call__(self, a: Any, b: Any) -> None:
        """Runs the `_assertion_function`

        Args:
            a: value that will be compared with `b`
            b: value that will be compared with `a`

        Returns:
            None
        """
        super().__call__(a=a, b=b)


@dataclass
class AssertLess(ComparisonAssertion):
    """assert `a` < `b`

    raise `AssertionError` if `a` is less than `b`

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
    """assert `a` <= `b`

    raise `AssertionError` if `a` is less or equal to `b`

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
    """assert `a` > `b`

    raise `AssertionError` if `a` is greater than `b`

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
    """assert `a` >= `b`

    raise `AssertionError` if `a` is greater or equal to `b`

    For more documentation read TestCase().assertGreaterEqual.__doc__

    Example:
        >>> assert_greater_equal = AssertGreaterEqual()
        >>> assert_greater_equal(2,1)
        >>> assert_greater_equal(2,2)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertGreaterEqual, init=False
    )
