
class Hex(int):

    def __new__(cls, i, base=0):
        """
        In contrast to int(), Hex() converts literal string integers to integers by default.
        Note from int():
        For base 0, the string is interpreted in a similar way to an integer literal in code,
        in that the actual base is 2, 8, 10, or 16 as determined by the prefix. (b=2, o=8, x=16)
        """
        kwargs = dict() if isinstance(i, int) else dict(base=base)
        return super().__new__(cls, i, **kwargs)

    def __repr__(self):
        return hex(self)






if __name__ == "__main__":
    def test(a, b):
        assert a == b, fmt(a, b)

    def fmt(a, b):
        return f"{a} != {b}"

    h1 = Hex(255)
    h2 = Hex(0xff)
    h3 = Hex("0xff")
    h4 = Hex("255")

    hs = (h1, h2, h3, h4)

    for a in hs:
        ra = repr(a)
        for b in hs:
            rb = repr(b)
            test(a, b)
            test(ra, rb)

    for h in hs:
        r = repr(h)
        test(h, 255)
        test(h, 0xff)
        test(r, "0xff")



