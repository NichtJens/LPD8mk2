from debug import debug


class Any:

#    @debug
    def __eq__(self, other):
        return True

    def __int__(self):
        return 0 #TODO: here, something is needed for hex conversion

    def __repr__(self):
        return type(self).__name__



Any = Any()



