class Bit:
    def __init__(self, byte: int, bit: int, label: str, value: bool = False):
        self.byte = byte
        self.bit = bit
        self.label = label
        self.value = value

    @property
    def mask(self) -> int:
        return 1 << ((self.byte - 1) * 8 + self.bit)

    def copy(self, value: bool) -> 'Bit':
        return Bit(byte=self.byte, bit=self.bit, label=self.label, value=value)


class TagDefinition:
    def __init__(self, length: int, bits: list[Bit], aliases: list[str] = []):
        self.length = length
        self.bits = bits
        self.aliases = aliases

    def parse_value(self, value: str) -> list[Bit]:
        if len(value) % 2 != 0:
            raise ValueError("Value must be the hex representation of bytes")

        if len(value) != (self.length * 2):
            raise ValueError(f"Value length must be {self.length} bytes")

        parsed = int(value, base=16)

        bit_values = []

        for bit in self.bits:
            enabled = (parsed & bit.mask) != 0
            bit_values.append(bit.copy(value=enabled))

        return bit_values


__cdi_cap = "Card Data Input Capability"


KNOWN_TAGS = {
    "9f33": TagDefinition(
        length=3,
        aliases=["terminal_capabilities", "term_cap", "tcap"],
        bits=[
            Bit(byte=1, bit=1, label=" - RFU"),
            Bit(byte=1, bit=2, label=f"{__cdi_cap} - RFU"),
            Bit(byte=1, bit=3, label=f"{__cdi_cap} - RFU"),
            Bit(byte=1, bit=4, label=f"{__cdi_cap} - RFU"),
            Bit(byte=1, bit=5, label=f"{__cdi_cap} - RFU"),
            Bit(byte=1, bit=6, label=f"{__cdi_cap} - ICC with contacts"),
            Bit(byte=1, bit=7, label=f"{__cdi_cap} - Magnetic stripe"),
            Bit(byte=1, bit=8, label=f"{__cdi_cap} - Manual key entry"),
        ],
    ),
}
