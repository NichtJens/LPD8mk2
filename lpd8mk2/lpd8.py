from .midi_io import MIDI_IO
from .knob import Knob
from .pad import Pad
from .utils import parse, print_table, print_line

from .consts import N_PADS, N_KNOBS
from .consts import RESP_ID_REQUEST, RESP_WHICH_PROGRAM, RESP_GET_PROGRAM_HEAD, RESP_GET_PROGRAM_PAD, RESP_GET_PROGRAM_KNOB
from .consts import SYSEX_ID_REQUEST, SYSEX_WHICH_PROGRAM, SYSEX_GET_PROGRAM


class LPD8(MIDI_IO):

    def __init__(self, pattern="LPD8", n_knobs=8, n_pads=8):
        super().__init__(pattern)

        n = self.send_which_program()
        ids_knobs, ids_pads = self.send_get_program(n)

        self._mk_attrs(n_knobs, "knob", Knob, ids_knobs)
        self._mk_attrs(n_pads,  "pad",  Pad,  ids_pads)


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
    parsed = parse(RESP_ID_REQUEST, data)
    print_table(parsed)


def parse_which_program_response(data):
    parsed = parse(RESP_WHICH_PROGRAM, data)
    print_table(parsed)
    n_program = parsed["n"]
    n_program = int(n_program)
    return n_program


def parse_get_program_response(data):
    ids_pads  = {}
    ids_knobs = {}

    parsed = parse(RESP_GET_PROGRAM_HEAD, data)
    rest = parsed.pop("Rest")
    print_table(parsed)

    for i in range(N_PADS):
        parsed = parse(RESP_GET_PROGRAM_PAD, rest)
        rest = parsed.pop("Rest")
        print_line(parsed)
        unknown = rest[:12] # should contain: type (toggle/momentary), pressure message (off, channel, polyphonic), full level (on, off)
        rest = rest[12:]
        note = parsed["Note"]
        ids_pads[i+1] = int(note)

    for i in range(N_KNOBS):
        parsed = parse(RESP_GET_PROGRAM_KNOB, rest)
        rest = parsed.pop("Rest", None)
        print_line(parsed)
        ctrl = parsed["Control"]
        ids_knobs[i+1] = int(ctrl)

    if rest:
        print("Rest", rest)

    return ids_knobs, ids_pads



