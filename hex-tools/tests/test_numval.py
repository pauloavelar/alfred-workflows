from hextools import Base, NumericValue


def test_numval_constructor():
    numval = NumericValue(10, Base.BINARY)

    assert numval.value == 10
    assert numval.base == Base.BINARY


def test_numval_copy():
    original = NumericValue(10, Base.BINARY)
    copied = original.copy(Base.OCTAL)
    default = original.copy()

    assert original != copied
    assert original != default
    assert original.base == Base.BINARY
    assert copied.base == Base.OCTAL
    assert default.base == Base.BINARY


def test_numval_format():
    binary = NumericValue(203040, Base.BINARY)
    assert binary.format() == "110001100100100000"
    assert binary.format(separators=True) == "11 0001 1001 0010 0000"

    octal = NumericValue(203040, Base.OCTAL)
    assert octal.format() == "614440"
    assert octal.format(separators=True) == "61 4440"

    decimal = NumericValue(203040, Base.DECIMAL)
    assert decimal.format() == "203040"
    assert decimal.format(separators=True) == "203,040"

    hexadecimal = NumericValue(203040, Base.HEXADECIMAL)
    assert hexadecimal.format() == "31920"
    assert hexadecimal.format(separators=True) == "3 19 20"


def test_numval_to_other_formats():
    binary = NumericValue(10, Base.DECIMAL)
    others = binary.to_other_formats()

    assert len(others) == 3
    assert others[0].base == Base.BINARY
    assert others[1].base == Base.OCTAL
    assert others[2].base == Base.HEXADECIMAL


def test_numval_parse():
    numval = NumericValue.parse("0x1abc", Base.HEXADECIMAL)

    assert numval.value == 0x1abc
    assert numval.base == Base.HEXADECIMAL
