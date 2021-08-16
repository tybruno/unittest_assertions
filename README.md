# unittest_assertions
Made the unittest assertions standalone allowing developers to use the builtin assertions for non unittest use cases.


#### Key Features:
* **Easy**: Designed to make it be simple allowing developers to use the builtin unittest assertions for their own use cases.
* **Great Developer Experience**: Being fully typed makes it great for editor support.
* **There is More!!!**:
    * [assertify](https://github.com/tybruno/assertify): Simple, Flexible, and Extendable python3.6+ library to evaulate an expression and return `True`/`False` or raise an `AssertionError` or `Exception`.
    * [assertify_predicates](https://github.com/tybruno/assertify_predicates): Is an extension of Assertify which allows for assertifying predicates. This is useful for validating variables or user input.
    * [descriptify](https://github.com/tybruno/descriptify): Descriptify is a library that contians helpful python descriptors. It uses `assertify_predicates` to validate various descriptors.

## Installation
```bash
pip install "git+https://github.com/tybruno/unittest_assertions.git#egg=unittest_assertions"
```
## Example
```python
from unittest_assertions.identity import AssertIsInstance

assert_is_instance = AssertIsInstance(msg="Raised a AssertionError")
assert_is_instance("example str", int) # raise TypeError("'example str' is not an instance of <class 'int'> : Raised a AssertionError")
```
# Asserters
## Comparison
| Asserter | Expression | 
|-----------------|----------|
|AssertEqual| first == second| 
| AssertNotEqual| first != Second | 
|AssertAlmostEqual| first ~ second|
|AssertNotAlmostEqual| first !~ second| 
|AssertCountEqual| len(first) == len(second)| 
|AssertMultilineEqual| first.splitlines() == second.splitlines()|
|AsseritySequenceEqual| seq1 == seq2| 
|AssertListEqual| list1 == list2| 
|AssertTupleEqual| tuple1 == tuple2| 
|AssertSetEqual| set1 == set2 | 
|AssertDictEqual| dict1 == dict2| 
|AssertLess| a < b| 
|AssertLessEqual| a <= b | 
|AssertGreater| a > b | 
|AssertGreater| a >= b | 
## Container
| Asserter | Expression |
|-----------------|----------------|
|AssertIn| member in container| 
| AssertNotIn| member not in container |
## Control
| Asserter | Expression |
|-----------------|----------------|
|AssertRaises| excpected_exception | 
|AssertWarns| excpected_warning| 
|AssertLogs| logger(level) | 
## Identity
| Asserter | Expression |
|-----------------|----------------|
|AssertIs| exp1 is exp2|
|AssertIsNot| exp1 is not exp2| 
|AssertIsNone| obj is None|
|AssertIsNotNone| obj is not None|
|AssertIsInstance|isinstance(obj,class) |
|AssertIsInstances| isinstance(obj,cls) for cls in classes | 
|AssertIsNotInstance| not isinstance(obj,class) | 
|AssertIsNotInstances| not isinstance(obj,cls) for cls in classes |
## Logic
| Asserter| Expression | 
|-----------------|----------------|
|AssertTrue| expr |
|AssertFalse| not expr |
## Regex
| Asserter | Expression | 
|-----------------|----------------|
|AssertRaisesRegex| expected_regex in expected_exception_message |
|AssertWarnsRegex| expected_regex in expected_warning_message | 
|AssertRegex| text in expected_regex| 
|AssertNotRegex| text not in expected_regex| 
