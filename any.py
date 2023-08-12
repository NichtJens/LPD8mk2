from debug import debug


class Any:

#    @debug
    def __eq__(self, other):
        return True

    def __repr__(self):
        return type(self).__name__



Any = Any()



