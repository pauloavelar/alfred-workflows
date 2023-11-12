from .base import Base


class NumericValue:
    def __init__(self, value: int, base: Base):
        self.value = value
        self.base = base

    def copy(self, base: Base = None):
        if base is None:
            base = self.base

        return NumericValue(self.value, base)

    def format(self, separators: bool = False) -> str:
        return self.base.format(self.value, separators)

    def to_other_formats(self) -> list['NumericValue']:
        other_formats = []

        for base in Base.values():
            if self.base != base:
                other_formats.append(self.copy(base))

        return other_formats

    @staticmethod
    def parse(value: str, base: Base) -> 'NumericValue':
        val_wo_prefix = value[len(base.prefix):]
        return NumericValue(int(val_wo_prefix, base.value), base)
