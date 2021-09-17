# unittest_assertions
Thin wrapper around the python builtin `unittest` allowing developers to use the builtin assertions for non-unittest use cases.
 

#### Key Features:
* **Easy**: Designed to make it be simple allowing developers to use the builtin unittest assertions for their own use cases.
* **Great Developer Experience**: Being fully typed, documented, and tested makes it great for editor support and extension.
* **There is More!!!**:
    * [assertify](https://github.com/tybruno/assertify): Simple, Flexible, and Extendable python3.6+ library to evaulate an expression and return `True`/`False` or raise an `AssertionError` or `Exception`.
    * [assertify_predicates](https://github.com/tybruno/assertify_predicates): Is an extension of Assertify which allows for assertifying predicates. This is useful for validating variables or user input.
    * [descriptify](https://github.com/tybruno/descriptify): Descriptify is a library that contians helpful python descriptors. It uses `assertify_predicates` to validate various descriptors.

## Installation
```bash
pip install unittest-assertions
```
## Examples
```python
from unittest_assertions.identity import AssertIsInstance

assert_is_instance = AssertIsInstance(msg="Raised a AssertionError")
assert_is_instance("example str", int) # raise TypeError("'example str' is not an instance of <class 'int'> : Raised a AssertionError")
```
```python
from unittest_assertions.comparison import AssertEqual
assert_equal = AssertEqual()
assert_equal(1,1)
assert_equal(first="hello",second="hello")
```
```python
from unittest_assertions.container import AssertNotIn
assert_in = AssertNotIn()
assert_in(member=1,container=[5,2,3])
```
# Asserters
## Comparison
| Asserter | Expression | 
|-----------------|----------|
|AssertEqual| `assert first == second`| 
| AssertNotEqual| `assert first != second` | 
|AssertAlmostEqual| `assert first ~= second` |
|AssertNotAlmostEqual| `assert first !~= second` | 
|AssertCountEqual| `assert Counter(list(first)) == Counter(list(second))`| 
|AssertMultilineEqual| `assert first.splitlines()` == `second.splitlines()` |
|AsseritySequenceEqual| `assert seq1 == seq2`| 
|AssertListEqual| `assert list1 == list2`| 
|AssertTupleEqual| `assert tuple1 == tuple2`| 
|AssertSetEqual| `assert set1 == set2` | 
|AssertDictEqual| `assert dict1 == dict2`| 
|AssertLess| `assert a < b`| 
|AssertLessEqual| `assert a <= b` | 
|AssertGreater| `assert a > b` | 
|AssertGreater| `assert a >= b` | 
## Container
| Asserter | Expression |
|-----------------|----------------|
|AssertIn| `member in container`| 
| AssertNotIn| `member not in container` |
## Control
| Asserter | Expression |
|-----------------|----------------|
|AssertRaises| excpected_exception | 
|AssertWarns| excpected_warning| 
|AssertLogs| logger(level) | 
## Identity
| Asserter | Expression |
|-----------------|----------------|
|AssertIs| `assert exp1 is exp2`|
|AssertIsNot| `assert exp1 is not exp2`| 
|AssertIsNone| `assert obj is None`|
|AssertIsNotNone| `assert obj is not None`|
|AssertIsInstance|`assert isinstance(obj,class)` |
|AssertIsNotInstance| `assert not isinstance(obj,class)` | 

## Logic
| Asserter| Expression | 
|-----------------|----------------|
|AssertTrue| `assert expr` |
|AssertFalse| `assert not expr` |
## Regex
| Asserter | Expression | 
|-----------------|----------------|
|AssertRaisesRegex| `assert expected_regex in expected_exception_message` |
|AssertWarnsRegex| `assert expected_regex in expected_warning_message` | 
|AssertRegex| `assert text in expected_regex`| 
|AssertNotRegex| `assert text not in expected_regex`| 
