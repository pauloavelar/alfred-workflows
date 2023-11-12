import re
from textwrap import wrap


VALID_INPUT = re.compile(r'^(0x|0b)?[0-9a-f]+$')
POSSIBLE_HEX = re.compile(r'^[0-9a-f]+$', re.IGNORECASE)
HEX_CHARS = re.compile(r'[a-f]', re.IGNORECASE)


def is_valid_input(input: str) -> bool:
    return VALID_INPUT.match(input) is not None


def is_possibly_hex(value: str) -> bool:
    return POSSIBLE_HEX.match(value) and HEX_CHARS.search(value)


def rsep(value: str, interval: int) -> str:
    inverted = value[::-1]
    return ' '.join(wrap(inverted, interval))[::-1]


def build_formatter(fn, sep_n: int):
    return lambda val, seps: rsep(fn(val)[2:], sep_n) if seps else fn(val)[2:]


def format_decimal(val: int, seps: int) -> str:
    return f'{val:,}' if seps else str(val)
