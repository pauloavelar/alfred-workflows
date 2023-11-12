from hextools import Base


def test_base_value():
    assert Base.BINARY.value == 2
    assert Base.OCTAL.value == 8
    assert Base.DECIMAL.value == 10
    assert Base.HEXADECIMAL.value == 16


def test_base_properties():
    assert Base.BINARY.prefix == "0b"
    assert Base.BINARY.label == "Binary"


def test_base_format():
    assert Base.BINARY.format(0b101010, with_separators=False) == "101010"
    assert Base.DECIMAL.format(15300, with_separators=True) == "15,300"
    assert Base.HEXADECIMAL.format(0x1234, with_separators=True) == "12 34"


def test_base_values():
    values = Base.values()
    assert len(values) == 4
    assert Base.BINARY in values
    assert Base.OCTAL in values
    assert Base.DECIMAL in values
    assert Base.HEXADECIMAL in values


def test_base_is_valid():
    assert all(Base.is_valid(base) for base in [2, 8, 10, 16])
    assert all(not Base.is_valid(base) for base in [1, 3, 4, 12, 36, 64])


def test_base_infer():
    assert Base.infer("0b1010") == Base.BINARY
    assert Base.infer("0o1567") == Base.OCTAL
    assert Base.infer("0x1abc") == Base.HEXADECIMAL
    assert Base.infer("123456") == Base.DECIMAL
    assert Base.infer("1a2b3c") == Base.HEXADECIMAL
