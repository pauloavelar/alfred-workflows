from .tags import Bit, KNOWN_TAGS


def parse_tlv(value: str):
    pass


def parse_tag(name: str, value: str) -> list[Bit]:
    sanitized_name = name.lower()

    for tag, definitions in KNOWN_TAGS.items():
        if (tag == sanitized_name) or (name in definitions.aliases):
            return definitions.parse_value(value)

    raise ValueError(f"Unknown tag: {name}")
