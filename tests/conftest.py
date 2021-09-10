import pytest

BASIC_TYPES_1 = {str: "string1", int: 1, float: 1.1}
BASIC_TYPES_2 = {str: "string2", int: 2, float: 1.2}

MULTILINE_1 = """Multiline1\nTest1\n\n"""
MULTILINE_2 = """Multiline2\nTest2\n\n"""

BASIC_CONTAINERS_1 = {
    list: [value for value in BASIC_TYPES_1.values()],
    tuple: tuple(value for value in BASIC_TYPES_1.values()),
    set: set(value for value in BASIC_TYPES_1.values()),
    dict: BASIC_TYPES_1,
}
BASIC_CONTAINERS_2 = {
    list: [value for value in BASIC_TYPES_2.values()],
    tuple: tuple(value for value in BASIC_TYPES_2.values()),
    set: set(value for value in BASIC_TYPES_2.values()),
    dict: BASIC_TYPES_2,
}
ALL_BASIC_TYPES_1 = {**BASIC_TYPES_1, **BASIC_CONTAINERS_1}
ALL_BASIC_TYPES_2 = {**BASIC_TYPES_2, **BASIC_CONTAINERS_2}


def create_not_instance_testing_data(dictionary):
    testing_data = list()
    for _type in dictionary.keys():
        temp_dict = dictionary.copy()
        temp_dict.pop(_type)

        for obj in temp_dict.values():
            testing_data.append((obj, _type))

    return testing_data


NOT_INSTANCE_TESTING_DATA = create_not_instance_testing_data(ALL_BASIC_TYPES_1)

print(create_not_instance_testing_data(ALL_BASIC_TYPES_1))


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
