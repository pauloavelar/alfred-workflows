#!/usr/bin/env python3

import json
import sys

import hextools


def build_error_response(msg: str):
    return {
        "title": "Unable to parse value",
        "subtitle": msg,
        "valid": False,
    }


EMPTY_RESPONSE = build_error_response("Please enter a valid number")


def map_to_workflow_items(value: hextools.NumericValue):
    formatted = value.format()
    with_separators = value.format(separators=True)

    return {
        "title": with_separators,
        "subtitle": value.base.label,
        "arg": formatted,
        "text": {
            "copy": formatted,
            "largetype": with_separators,
        },
        "mods": {
            "alt": {
                "subtitle": f"{value.base.label} (formatted)",
                "arg": with_separators,
                "text": {
                    "copy": with_separators,
                },
            },
        },
    }


try:
    sanitized_input = sys.argv[1].lower().strip()
    values = hextools.parse(sanitized_input)

    if len(values) == 0:
        workflow_response = EMPTY_RESPONSE
    else:
        workflow_response = list(map(map_to_workflow_items, values))
except ValueError as err:
    workflow_response = build_error_response(err.args[0])

sys.stdout.write(json.dumps({"items": workflow_response}))
