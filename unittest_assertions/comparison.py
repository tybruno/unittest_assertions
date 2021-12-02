""" Equality and Comparison Assertions"""  # pylint: disable=duplicate-code
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
)
from unittest import TestCase

from unittest_assertions.base import Assertion


@dataclass
class AssertEqual(Assertion):
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
class AssertNotEqual(Assertion):
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
class AssertAlmostEqual(Assertion):
    """assert `first` ~= `second`

    raise `AssertionError` if `first` is not almost equal to `second`

    For more documentation read TestCase().assertAlmostEqual.__doc__

    Example:
        >>> assert_almost_equal = AssertAlmostEqual()
        >>> assert_almost_equal(1.00000001, 1.0)
        >>> assert_almost_equal(first=1.1, second=1.0, places=None, delta=0.5)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertAlmostEqual, init=False
    )


@dataclass
class AssertNotAlmostEqual(Assertion):
    """assert `first` !~= `second`

    raise `AssertionError` if `first` is almost  equal to `second`

    For more documentation read TestCase().assertNotAlmostEqual.__doc__

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
class AssertMultilineEqual(Assertion):
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
class AssertSequanceEqual(Assertion):
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


@dataclass
class AssertListEqual(Assertion):
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


@dataclass
class AssertTupleEqual(Assertion):
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


@dataclass
class AssertSetEqual(Assertion):
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


@dataclass
class AssertDictEqual(Assertion):
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


@dataclass
class AssertLess(Assertion):
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
class AssertLessEqual(Assertion):
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
class AssertGreater(Assertion):
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
class AssertGreaterEqual(Assertion):
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