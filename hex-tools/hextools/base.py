from enum import Enum

from .__helpers import is_possibly_hex, build_formatter, format_decimal


class Base(Enum):
    BINARY = 2, build_formatter(bin, 4), "Binary", "0b"
    OCTAL = 8, build_formatter(oct, 4), "Octal", "0o"
    DECIMAL = 10, format_decimal, "Decimal"
    HEXADECIMAL = 16, build_formatter(hex, 2), "Hexadecimal", "0x"

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: int, serializer, label: str, prefix: str = ""):
        self._serializer_ = serializer
        self._label_ = label
        self._prefix_ = prefix

    @property
    def prefix(self):
        return self._prefix_

    @property
    def label(self):
        return self._label_

    def format(self, value: int, with_separators: bool) -> str:
        return self._serializer_(value, with_separators)

    @staticmethod
    def values() -> list['Base']:
        return [b for b in Base]

    @staticmethod
    def is_valid(base: int) -> bool:
        return base in map(lambda b: b.value, Base.values())

    @staticmethod
    def infer(input: str) -> 'Base':
        for base in Base.values():
            if base.prefix and input.startswith(base.prefix):
                return base

        return Base.HEXADECIMAL if is_possibly_hex(input) else Base.DECIMAL
