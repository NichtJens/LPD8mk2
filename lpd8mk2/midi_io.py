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
    ports = set(ports)
    for n in ports:
        if fnmatch(n, f"*{pattern}*"):
            return mido.open_ioport(n)
    print_available(ports)
    raise ValueError(f'cannot find device for pattern "{pattern}"')


def print_available(ports):
    print()
    print("available ports:")
    for n in ports:
        print("-", n)
    print()



