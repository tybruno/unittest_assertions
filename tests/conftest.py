import pytest

BASIC_TYPES_1 = {str: "string1", int: 1, float: 1.1}
BASIC_TYPES_2 = {str: "string2", int: 2, float: 1.2}


BASIC_CONTAINERS_1 = {
    list: [value for value in BASIC_TYPES_1.values()],
    tuple: tuple(value for value in BASIC_TYPES_1.values()),
    set: set(value for value in BASIC_TYPES_1.values()),
}
BASIC_CONTAINERS_2 = {
    list: [value for value in BASIC_TYPES_2.values()],
    tuple: tuple(value for value in BASIC_TYPES_2.values()),
    set: set(value for value in BASIC_TYPES_2.values()),
}
ALL_BASIC_TYPES_1 = {**BASIC_TYPES_1, **BASIC_CONTAINERS_1}
ALL_BASIC_TYPES_2 = {**BASIC_TYPES_2, **BASIC_CONTAINERS_2}


@pytest.fixture
def basic_types_1():
    return BASIC_TYPES_1


@pytest.fixture
def basic_types_2():
    return BASIC_TYPES_2


@pytest.fixture
def basic_containers_1():
    return BASIC_CONTAINERS_1


@pytest.fixture
def basic_containers_2():
    return BASIC_CONTAINERS_2


@pytest.fixture
def all_basic_types1():
    return ALL_BASIC_TYPES_1


@pytest.fixture
def all_basic_types2():
    return ALL_BASIC_TYPES_2


def combined_equal_all_basic_types():
    combined_types = tuple(
        (value, value) for value in ALL_BASIC_TYPES_1.values()
    )
    return combined_types


def combined_non_equal_all_basic_types():
    combined_types = tuple(
        (value1, value2)
        for value1, value2 in zip(
            ALL_BASIC_TYPES_1.values(), ALL_BASIC_TYPES_2.values()
        )
    )
    return combined_types


def equal_sequences():
    combined_sequences = (
        (sequence, sequence) for sequence in BASIC_CONTAINERS_1.values()
    )
    return combined_sequences


def not_equal_sequences():
    combined_sequences = (
        (seq1, seq2)
        for seq1, seq2 in zip(BASIC_CONTAINERS_1.values(), BASIC_CONTAINERS_2)
    )
    return combined_sequences


def equal_lists():
    equal_list = (BASIC_CONTAINERS_1[list], BASIC_CONTAINERS_1[list])
    return equal_list


def non_equal_list():
    equal_list = (BASIC_CONTAINERS_1[list], BASIC_CONTAINERS_2[list])
    return equal_list
