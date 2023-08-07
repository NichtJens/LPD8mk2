from debug import debug


class MessageDispatcher:

    @debug
    def handle_message(self, msg):
        if   msg.type == "sysex":          self.handle_sysex(msg.data)
        elif msg.type == "note_on":        self.handle_note_on(msg.note, msg.velocity)
        elif msg.type == "note_off":       self.handle_note_off(msg.note, msg.velocity)
        elif msg.type == "control_change": self.handle_control_change(msg.control, msg.value)
        elif msg.type == "program_change": self.handle_program_change(msg.program)
        else:                              self.handle_unknown(msg)


    @debug
    def handle_sysex(self, data):
        pass

    @debug
    def handle_note_on(self, note, velocity):
        pass

    @debug
    def handle_note_off(self, note, velocity):
        pass

    @debug
    def handle_control_change(self, control, value):
        pass

    @debug
    def handle_program_change(self, program):
        pass

    @debug
    def handle_unknown(self, msg):
        raise ValueError(f'cannot handle message type "{msg.type}": {msg}')





if __name__ == "__main__":
    md = MessageDispatcher()


    class Message:

        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        def __repr__(self):
            return repr(self.__dict__)


    msg0 = Message(type="sysex", data=123)
    msg1 = Message(type="note_on", note=1, velocity=10)
    msg2 = Message(type="note_off", note=2, velocity=20)
    msg3 = Message(type="control_change", control=3, value=30)
    msg4 = Message(type="program_change", program=4)
    msg5 = Message(type="???", test="?")


    for msg in (msg0, msg1, msg2, msg3, msg4, msg5):
        md.handle_message(msg)



