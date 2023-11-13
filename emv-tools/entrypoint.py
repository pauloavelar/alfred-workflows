#!/usr/bin/env python3

import json
import sys

import emvtools


def build_error_response(msg: str):
    return {
        "title": "Unable to parse value",
        "subtitle": msg,
        "valid": False,
    }


EMPTY_RESPONSE = build_error_response("Please enter a valid number")


def map_to_workflow_items(value: emvtools.Bit):
    return {
        "title": value.label,
        "subtitle": "Enabled (1)" if value.value else "Disabled (0)",
        "arg": "https://paymentcardtools.com/emv-tag-decoders/termcap",
        "text": {
            "copy": value.label,
            "largetype": value.label + ": " + str(value.value),
        },
    }


try:
    params = sys.argv[1].lower().strip().split(" ")
    input = list(filter(lambda p: len(p) > 0, params))

    if len(input) > 2:
        raise ValueError(f"Too many parameters: {len(input)}")

    if len(input) == 2:
        values = emvtools.parse_tag(name=input[0], value=input[1])
    else:
        values = emvtools.parse_tlv(input[0])

    workflow_response = list(map(map_to_workflow_items, values))
except ValueError as err:
    workflow_response = build_error_response(err.args[0])

sys.stdout.write(json.dumps({"items": workflow_response}))
