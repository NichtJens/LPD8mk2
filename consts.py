
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
# (repeat name n times if there are n bytes for that entry)

RESP_ID_REQUEST = [
    "Start",
    "Channel",
    "Sub-ID", "Sub-ID",
    "Man. ID",
    "Family", # why only one?
    "Device", "Device",
    "SW Ver.", "SW Ver.", "SW Ver.", "SW Ver.",
    "End",
    "Rest"
]

RESP_WHICH_PROGRAM = [
    "Man. ID",
    "Family",
    "Device",
    "Command", "Command", "Command",
    "n"
]

RESP_GET_PROGRAM_HEAD = [
    "Man. ID",
    "Family",
    "Device",
    "Command", "Command", "Command",
    "n",
    "x", "x", "x", "x"
]

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



