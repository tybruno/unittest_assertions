BASIC_TYPES1 = {
    str: "string1",
    int: 1,
    float: 1.0,
    list: [1, "string"],
    tuple: (),
}


EQUAL_DATA = (
    (1, 1),
    (-1.2, -1.2),
    ("string", "string"),
    (["list", 1], ["list", 1]),
)
NON_EQUAL_DATA = (
    (1, 2),
    (-1.2, -1.29),
    ("string", "string2"),
    (["list", 1], ["list2", 2]),
)
