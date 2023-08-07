from midi_io import MIDI_IO
from knob import Knob
from pad import Pad
from consts import SYSEX_ID_REQUEST, SYSEX_WHICH_PROGRAM, SYSEX_GET_PROGRAM


IDS_KNOBS = {i+1: i+70 for i in range(8)}
IDS_PADS  = {i+1: i+36 for i in range(8)}


class LPD8(MIDI_IO):

    def __init__(self, pattern="LPD8", n_knobs=8, n_pads=8):
        super().__init__(pattern)

        self._mk_attrs(n_knobs, "knob", Knob, IDS_KNOBS)
        self._mk_attrs(n_pads,  "pad",  Pad,  IDS_PADS)


    def _mk_attrs(self, n, prefix, Type, ids):
        collect = {}
        for i in range(n):
            i += 1 # count from 1
            a = Type()
            setattr(self, f"{prefix}{i}", a)
            id = ids[i]
            collect[id] = a
        setattr(self, f"all_{prefix}s", collect)


    def handle_note_on(self, note, velocity):
        self.all_pads[note].on.run_callbacks(velocity)

    def handle_note_off(self, note, velocity):
        self.all_pads[note].off.run_callbacks(velocity)

    def handle_control_change(self, control, value):
        self.all_knobs[control].change.run_callbacks(value)


    def send_id_request(self):
        resp = self.send_sysex(SYSEX_ID_REQUEST)
        return parse_id_request_response(resp)

    def send_which_program(self):
        resp = self.send_sysex(SYSEX_WHICH_PROGRAM)
        return parse_which_program_response(resp)

    def send_get_program(self, n):
        resp = self.send_sysex(SYSEX_GET_PROGRAM + [n])
        return parse_get_program_response(resp)





def parse_id_request_response(data):
    start, channel, subid1, subid2, manid, fam1, fam2, dev1, dev2, ver1, ver2, ver3, end, *rest = data
    print("Start  ", start)
    print("Channel", channel)
    print("Sub-ID ", subid1, subid2)
    print("Man. ID", manid)
    print("Family ", fam1, fam2)
    print("Device ", dev1, dev2)
    print("SW Ver.", ver1, ver2, ver3) # why only 3?
    print("End    ", end)
    print("Rest   ", rest)


def parse_which_program_response(data):
    manid, fam, dev, cmd1, cmd2, cmd3, n_program = data
    print("Man. ID", manid)
    print("Family ", fam)
    print("Device ", dev)
    print("Command", cmd1, cmd2, cmd3)
    print("n      ", n_program)
    n_program = sint(n_program)
    return n_program


def parse_get_program_response(data):
    ids_pads  = {}
    ids_knobs = {}

    manid, fam, dev, cmd1, cmd2, cmd3, n_program, x1, x2, x3, x4, *rest = data
    print("Man. ID", manid)
    print("Family ", fam)
    print("Device ", dev)
    print("Command", cmd1, cmd2, cmd3)
    print("n      ", n_program)

    print("x      ", x1, x2, x3, x4)

    for i in range(8):
        note, count1, count2, channel, *rest = rest
        count1, count2, channel = sint((count1, count2, channel))
        block = rest[:12]
        rest = rest[12:]
        print("Note   ", note, sint(note), "| count", count1, count2, "| channel", channel, "|", sint(block))
        ids_pads[i+1] = sint(note)

#        note = sysexData[8 + 4*i],
#        programChange = sysexData[9 + 4*i],
#        controlChange = sysexData[10 + 4*i],
#        toggle = sysexData[11 + 4*i]

    for i in range(8):
        ctrl, cc, low, high, *rest = rest
        print("Control", ctrl, sint(ctrl), "| CC", cc, "| low", low, "| high", high)
        ids_knobs[i+1] = sint(ctrl)

    if rest:
        print("Rest   ", rest)

    return ids_knobs, ids_pads





from collections import defaultdict


def parse(desc, data):
    res = defaultdict(list)
    for name in desc:
        item, data = data[0], data[1:]
        res[name].append(item)
    if data:
        res["Rest"] = data
    res = {k: v[0] if len(v) == 1 else v for k, v in res.items()}
    return res


def print_table(d):
    length = max(len(i) for i in d)
    for k, v in d.items():
        print(k.ljust(length), v)





def sint(s, base=0):
    """
    Convert literal string integers to integers. Note from int():
    For base 0, the string is interpreted in a similar way to an integer literal in code,
    in that the actual base is 2, 8, 10, or 16 as determined by the prefix. (b=2, o=8, x=16)
    """
    if isinstance(s, str):
        return int(s, base=base)
    else:
        return [int(i, base=base) for i in s]



