""" Identity Assertions """
from unittest_assertions.base import BuiltinAssertion
from dataclasses import dataclass, field
from typing import Callable, Any
from unittest import TestCase


@dataclass
class AssertIs(BuiltinAssertion):
    """assert `expr1` is `expr2`

    raise `AssertionError` if `expr1` is not `expr2`

    For more documentation read TestCase().assertIs.__doc__

    Example:
        >>> value = "string"
        >>> assert_is = AssertIs()
        >>> assert_is(value,value)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIs, init=False
    )

    def __call__(self, expr1: Any, expr2: Any) -> None:
        super().__call__(expr1=expr1, expr2=expr2)


@dataclass
class AssertIsNot(AssertIs):
    """assert `expr1` is not `expr2`

    raise `AssertionError` if `expr1` is not `expr2`

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
class AssertIsNone(BuiltinAssertion):
    """assert `obj` is None

    raise `AssertionError` if `obj` is not None

    For more documentation read TestCase().assertIsNone.__doc__

    Example:
        >>> assert_is_none = AssertIsNone()
        >>> assert_is_none(None)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIsNone, init=False
    )

    def __call__(self, obj: Any) -> None:
        """Run assertion

        Args:
            obj: will that will be evaulated as `None` or not `None`

        Returns:
            None
        """
        super().__call__(obj=obj)


@dataclass
class AssertIsNotNone(AssertIsNone):
    """assert `obj` is None

    raise `AssertionError` if `obj` is not None

    For more documentation read TestCase().assertIsNone.__doc__

    Example:
        >>> assert_is_not_none = AssertIsNotNone()
        >>> assert_is_not_none("")
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIsNotNone, init=False
    )


@dataclass
class AssertIsInstance(BuiltinAssertion):
    """assert isinstance(obj,cls)

    raise `AssertionError` if not isinstance(obj,cls)

    For more documentation read TestCase().assertIsInstance.__doc__

    Example:
        >>> assert_is_instance = AssertIsInstance()
        >>> assert_is_instance(2,int)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertIsInstance, init=False
    )

    def __call__(self, obj, cls) -> None:
        """Run assertion

        Args:
            obj: will be checked if it is an instance of `cls`
            cls: class that will be used to check if `obj` is an
             instance of it.

        Returns:
            None

        """
        super().__call__(obj=obj, cls=cls)


@dataclass
class AssertNotIsInstance(AssertIsInstance):
    """assert not isinstance(obj,cls)

    raise `AssertionError` if isinstance(obj,cls)

    For more documentation read TestCase().assertNotIsInstance.__doc__

    Example:
        >>> assert_is_instance = AssertNotIsInstance()
        >>> assert_is_instance(2.5,int)
    """

    _assertion_function: Callable = field(
        default=TestCase().assertNotIsInstance, init=False
    )
