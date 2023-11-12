import pytest

import hextools


def test_parse():
    values = hextools.parse("0x12ff")

    assert len(values) == 4
    assert all(n.value == 0x12ff for n in values)
    assert values[0].base == hextools.Base.HEXADECIMAL
    assert values[1].base == hextools.Base.BINARY
    assert values[2].base == hextools.Base.OCTAL
    assert values[3].base == hextools.Base.DECIMAL


def test_parse_negative_value():
    with pytest.raises(ValueError):
        hextools.parse("-10")


def test_parse_invalid_input():
    with pytest.raises(ValueError):
        hextools.parse("INVALID")
