""" Identity Assertions

Objects provided by this module:
    * `AssertTrue`: `assert expr is True`
    * `AssertFalse`: `assert expr is False`
    * `AssertIs`: `assert expr1 is expr2`
    * `AssertIsNot`: `assert expr1 is not expr2`
    * `AssertIsNone`: `assert obj is None`
    * `AssertIsNotNone`: `assert obj is not None`
    * `AssertIsInstance`: `assert isinstance(obj, cls)`
    * `AssertNotIsInstance`: `assert not isinstance(obj,cls)`
"""

from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
    Any,
    Type,
)
from unittest import TestCase

from unittest_assertions.base import Assertion


@dataclass
class AssertTrue(Assertion):
    """`assert expr is True`

    raise `AssertionError` if `expr is False`

    For more documentation read TestCase().assertTrue.__doc__

    Example:
        >>> assert_true = AssertTrue()
        >>> assert_true(True)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertTrue, init=False
    )

    def __call__(self, expr: Any) -> None:
        """`assert expr is True`


        Args:
            expr: Expression that will be evaluated as True

        """
        super().__call__(expr=expr)


@dataclass
class AssertFalse(AssertTrue):
    """`assert expr is False`

    raise `AssertionError` if `expr`

    For more documentation read TestCase().assertFalse.__doc__

    Example:
        >>> _false_objects = ["", 0, [], False]
        >>> assert_false = AssertFalse()
        >>> for obj in _false_objects:
        ...     assert_false(obj)

    """

    _assertion_function: Callable = field(
        default=TestCase().assertFalse, init=False
    )


@dataclass
class AssertIs(Assertion):
    """`assert expr1 is expr2`

    raise `AssertionError` if `expr1 is not expr2`

    For more documentation read TestCase().assertIs.__doc__

    Example:
        >>> value = "string"
        >>> assert_is = AssertIs()
        >>> assert_is(value,value)
        True
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIs, init=False
    )

    def __call__(self, expr1: Any, expr2: Any) -> None:
        """`assert expr1 is expr2`

        Args:
            expr1: check if is `expr2`
            expr2: check if is `expr1
        """
        super().__call__(expr1=expr1, expr2=expr2)


@dataclass
class AssertIsNot(AssertIs):
    """`assert expr1 is not expr2`

    raise `AssertionError` if `expr1 is expr2`

    For more documentation read TestCase().assertIsNot.__doc__

    Example:
        >>> value1 = "string1"
        >>> value2 = "string2"
        >>> assert_is_not = AssertIsNot()
        >>> assert_is_not(value1,value2)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIsNot, init=False
    )


@dataclass
class AssertIsNone(Assertion):
    """`assert obj is None`

    raise `AssertionError` if `obj is not None`

    For more documentation read TestCase().assertIsNone.__doc__

    Example:
        >>> assert_is_none = AssertIsNone()
        >>> assert_is_none(None)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIsNone, init=False
    )

    def __call__(self, obj: Any) -> None:
        """`assert obj is None`

        Args:
            obj: Object that will be checked if it is `None`
        """
        super().__call__(obj=obj)


@dataclass
class AssertIsNotNone(AssertIsNone):
    """`assert obj is not None`

    raise `AssertionError` if `obj is None`

    For more documentation read TestCase().assertIsNone.__doc__

    Example:
        >>> assert_is_not_none = AssertIsNotNone()
        >>> assert_is_not_none("")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIsNotNone, init=False
    )


@dataclass
class AssertIsInstance(Assertion):
    """`assert isinstance(obj,cls)`

    raise `AssertionError` if `not isinstance(obj,cls)`

    For more documentation read TestCase().assertIsInstance.__doc__

    Example:
        >>> assert_is_instance = AssertIsInstance()
        >>> assert_is_instance(2,int)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIsInstance, init=False
    )

    def __call__(self, obj: Any, cls: Type) -> None:
        """`assert isinstance(obj,cls)`

        Args:
            obj: check if `isinstance` of `cls`
            cls: check if `obj` is instance of `cls`
        """
        super().__call__(obj=obj, cls=cls)


@dataclass
class AssertNotIsInstance(AssertIsInstance):
    """`assert not isinstance(obj,cls)`

    raise `AssertionError` if `isinstance(obj,cls)`

    For more documentation read TestCase().assertNotIsInstance.__doc__

    Example:
        >>> assert_is_instance = AssertNotIsInstance()
        >>> assert_is_instance(2.5,int)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotIsInstance, init=False
    )
