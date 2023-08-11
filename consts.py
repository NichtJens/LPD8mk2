from any import Any


# Universal Identity Request
SYSEX_ID_REQUEST = [
    0x7E, # Non-Realtime
    0x7F, # The SysEx channel. May be from 0x00 to 0x7F, here set to "disregard channel"
    0x06, # Sub-ID1 -- General Information
    0x01, # Sub-ID2 -- Identity Request
]



N_PADS = N_KNOBS = 8

SYSEX_AKAI = 0x47
SYSEX_LPD8_FAMILY = 0x7f
SYSEX_LPD8_MK2_DEVICE = 0x4c

SYSEX_HEADER = [
    SYSEX_AKAI,
    SYSEX_LPD8_FAMILY,
    SYSEX_LPD8_MK2_DEVICE,
]


# read which program is currently set
SYSEX_WHICH_PROGRAM = SYSEX_HEADER + [
    0x04,
    0x00,
    0x00,
]


# read program n (the n=1..4 needs to be appended)
SYSEX_GET_PROGRAM = SYSEX_HEADER + [
    0x03,
    0x00,
    0x01,
]



# SysEx response descriptions:

# Option 1
# dict mapping name to expected value(s).
# Values may be sequences of length n, then n bytes are read for that entry.
# `Any` may be used if there's no expected value.

# Option 2
# sequence of names, no expected value(s).
# These are treated as if all values are `Any` in Option 1.
# The name may be repeated n times, then n bytes are read for that entry.

# Example:
#
#    desc_list = [
#        "x",
#        "y", "y",
#        "z"
#    ]
#
# corresponds to:
#
#    desc_dict = {
#        "x": Any,
#        "y": [Any, Any],
#        "z": Any
#    }


RESP_ID_REQUEST = {
    "Start":   0x7e,
    "Channel": 0x0,
    "Sub-ID":  [0x6, 0x2],
    "Man. ID": SYSEX_AKAI,
    "Family":  0x4c, # why only one byte?
    "Device":  [0x0, 0x19],
    "SW Ver.": [Any] * 4,
    "End":     0x7f,
    "Rest":    Any
}

RESP_WHICH_PROGRAM = {
    "Man. ID": SYSEX_AKAI,
    "Family":  SYSEX_LPD8_FAMILY,
    "Device":  SYSEX_LPD8_MK2_DEVICE,
    "Command": [0x4, 0x0, 0x1],
    "n":       Any #TODO: can be 1..4
}

RESP_GET_PROGRAM_HEAD = {
    "Man. ID": SYSEX_AKAI,
    "Family":  SYSEX_LPD8_FAMILY,
    "Device":  SYSEX_LPD8_MK2_DEVICE,
    "Command": [0x3, 0x1, 0x29],
    "n":       Any, #TODO: can be 1..4
    "Unknown": [Any] * 4
}

RESP_GET_PROGRAM_PAD = [
    "Note",
    "CC",
    "PG",
    "Channel"
]

RESP_GET_PROGRAM_KNOB = [
    "Control",
    "CC",
    "low",
    "high"
]



