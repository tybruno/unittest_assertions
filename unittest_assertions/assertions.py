from dataclasses import (
    dataclass,
    field,
)
from typing import Callable, Union, Optional
from unittest import TestCase
from abc import abstractmethod
from string import Template


class AbstractAssertion:
    def __init__(
        self,
        function: Callable,
    ):
        ...

    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...


@dataclass
class BuiltinAssertion(AbstractAssertion):
    function: Callable
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, **kwargs):
        msg = self.msg
        if isinstance(msg, Template):
            msg = msg.substitute(kwargs)
        self.function(**kwargs, msg=msg)


@dataclass
class BasicBuiltinAssertion(BuiltinAssertion):
    def __call__(self, first, second):
        super().__call__(first=first, second=second)


@dataclass
class AssertTrue(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertTrue, init=False)

    def __call__(self, expr):
        super().__call__(expr=expr)


@dataclass
class AssertFalse(AssertTrue):
    function: Callable = field(default=TestCase().assertFalse, init=False)


@dataclass
class AssertEqual(BasicBuiltinAssertion):
    function: Callable = field(default=TestCase().assertEqual, init=False)


@dataclass
class AssertNotEqual(BasicBuiltinAssertion):
    function: Callable = field(default=TestCase().assertNotEqual, init=False)


@dataclass
class AssertAlmostEqual(BuiltinAssertion):
    function: Callable = field(
        default=TestCase().assertAlmostEqual, init=False
    )

    def __call__(self, first, second, places=None, delta=None):
        super().__call__(
            first=first, second=second, places=places, delta=delta
        )


@dataclass
class AssertNotAlmostEqual(AssertAlmostEqual):
    function: Callable = field(
        default=TestCase().assertNotAlmostEqual, init=False
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
class AssertIn(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertIn, init=False)

    def __call__(self, member, container):
        super().__call__(member=member, container=container)


@dataclass
class AssertNotIn(AssertIn):
    function: Callable = field(default=TestCase().assertNotIn, init=False)


@dataclass
class AssertIs(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertIs, init=False)

    def __call__(self, exp1, exp2):
        super().__call__(exp1=exp1, exp2=exp2)


@dataclass
class AssertIsNot(AssertIs):
    function: Callable = field(default=TestCase().assertIsNot, init=False)


@dataclass
class AssertDictEqual(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertDictEqual, init=False)

    def __call__(self, dict1, dict2):
        super().__call__(dict1=dict1, dict2=dict2)


@dataclass
class AssertCountEqual(BasicBuiltinAssertion):
    function: Callable = field(default=TestCase().assertCountEqual, init=False)


@dataclass
class AssertMultilineEqual(BasicBuiltinAssertion):
    function: Callable = field(
        default=TestCase().assertMultiLineEqual, init=False
    )


@dataclass
class AssertLess(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertLess, init=False)

    def __call__(self, a, b):
        super().__call__(a=a, b=b)


@dataclass
class AssertLessEqual(AssertLess):
    function: Callable = field(default=TestCase().assertLessEqual, init=False)


@dataclass
class AssertGreater(AssertLess):
    function: Callable = field(default=TestCase().assertGreater, init=False)


@dataclass
class AssertGreaterEqual(AssertLess):
    function: Callable = field(
        default=TestCase().assertGreaterEqual, init=False
    )


@dataclass
class AssertIsNone(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertIsNone, init=False)

    def __call__(self, obj):
        super().__call__(obj=obj)


@dataclass
class AssertIsNotNone(AssertIsNone):
    function: Callable = field(default=TestCase().assertIsNotNone, init=False)


@dataclass
class AssertIsInstance(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertIsInstance, init=False)

    def __call__(self, obj, cls):
        super().__call__(obj=obj, cls=cls)


@dataclass
class AssertNotIsInstance(AssertIsInstance):
    function: Callable = field(
        default=TestCase().assertNotIsInstance, init=False
    )


@dataclass
class AssertRaises(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertRaises, init=False)

    def __call__(self, expected_exception, **kwargs):
        super().__call__(expected_exception=expected_exception, **kwargs)


@dataclass
class AssertWarns(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertWarns, init=False)

    def __call__(self, expected_warning, **kwargs):
        super().__call__(expected_warning=expected_warning, **kwargs)


@dataclass
class AssertLogs(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertLogs, init=False)

    def __call__(self, logger=None, level=None):
        super().__call__(logger=logger, level=level)


@dataclass
class AssertRaisesRegex(BuiltinAssertion):
    function: Callable = field(
        default=TestCase().assertRaisesRegex, init=False
    )

    def __call__(self, expected_exception, expected_regex, **kwargs):
        super().__call__(
            expected_exception=expected_exception,
            expected_regex=expected_regex,
            **kwargs
        )


@dataclass
class AssertWarnsRegex(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertWarnsRegex, init=False)

    def __call__(self, expected_warning, expected_regex, **kwargs):
        super().__call__(
            expected_warning=expected_warning,
            expected_regex=expected_regex,
            **kwargs
        )


@dataclass
class AssertRegex(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertRegex, init=False)

    def __call__(self, text, expected_regex):
        super().__call__(text=text, expected_regex=expected_regex)


@dataclass
class AssertNotRegex(BuiltinAssertion):
    function: Callable = field(default=TestCase().assertNotRegex, init=False)

    def __call__(self, text, unexpected_regex):
        super().__call__(text=text, unexpected_regex=unexpected_regex)
