from .base import Base
from .numval import NumericValue
from .__helpers import is_valid_input


def parse(input: str) -> list[NumericValue]:
    if input.startswith("-"):
        raise ValueError("Negative numbers are not supported")

    if not is_valid_input(input):
        raise ValueError("Invalid number format")

    parsed_input = NumericValue.parse(input, base=Base.infer(input))

    return [parsed_input] + parsed_input.to_other_formats()
