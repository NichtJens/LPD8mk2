from fnmatch import fnmatch
from queue import Queue

import mido

from .debug import debug
from .hex import Hex
from .msgdisp import MessageDispatcher


class MIDI_IO(MessageDispatcher):

    def __init__(self, pattern):
        self.port = find_and_open_port(pattern)
        self.port.input.callback = self.handle_message
        self.queue_sysex = Queue()

    @debug
    def send_sysex(self, data):
        msg = mido.Message("sysex", data=data)
        self.port.send(msg)
        resp = self.queue_sysex.get()
        return resp

    @debug
    def handle_sysex(self, data):
        data = [Hex(i) for i in data]
        self.queue_sysex.put(data)





def find_and_open_port(pattern):
    ports = mido.get_ioport_names()
    ports = sorted(set(ports))
    matching = [n for n in ports if fnmatch(n, f"*{pattern}*")]
    n_matching = len(matching)

    if n_matching == 1:
        n = matching[0]
        return mido.open_ioport(n)

    if n_matching == 0:
        msg = f'cannot find device for pattern "{pattern}"'
        header = "available ports"
        which = ports
    else:
        msg = f'pattern "{pattern}" is ambiguous'
        header = "matching ports"
        which = matching

    print_list(header, which)
    raise ValueError(msg)


def print_list(header, items):
    print()
    print(f"{header}:")
    for n in items:
        print("-", n)
    print()



