from collections import defaultdict
from collections.abc import Sequence, Mapping

from .consts import Any


def parse(desc, data):
    if not isinstance(desc, Mapping):
        desc = desc_sequence_to_dict(desc)

    res = defaultdict(list)
    for name, ref in desc.items():
        n = len(ref) if isinstance(ref, Sequence) else 1 #TODO?
        item, data = data[:n], data[n:]
        res[name].extend(item)

    if data:
        res["Rest"] = data

    res = unpack_single_values(res)

    for name, ref in desc.items():
        found = res[name]
#        print("compare", found, ref, "->", found == ref) #TODO: remove
        if found != ref:
            # ref are regular int, found are Hex => format both identically
            sref = fmt(ref)
            sfound = fmt(found)
            msg = f'"{name}" should be {sref} but is {sfound}'
            raise ValueError(msg)

    return res


def desc_sequence_to_dict(desc):
    res = defaultdict(list)
    for name in desc:
        res[name].append(Any)
    res = unpack_single_values(res)
    return res


def unpack_single_values(d):
    return {k: v[0] if len(v) == 1 else v for k, v in d.items()}



def print_table(d):
    length = max(len(i) for i in d)
    for k, v in d.items():
        print(k.ljust(length), v)


def print_line(d):
    print(" | ".join(f"{k} {v}" for k, v in d.items()))





#TODO: this might be a little overengineered

def fmt(x):
    sdec = fmt_dec(x)
    shex = fmt_hex(x)
    return f"{sdec} ({shex})"

def dec(x):
    return str(int(x))

def make_fmt_sequence_aware(fmt):
    def wrapper(x):
        if isinstance(x, Sequence):
            fmted = ", ".join(fmt(j) for j in x)
            return f"[{fmted}]"
        else:
            return fmt(x)
    return wrapper

def make_fmt_Any_aware(fmt):
    def wrapper(x):
        return "Any" if x is Any else fmt(x)
    return wrapper

fmt_dec = make_fmt_sequence_aware(make_fmt_Any_aware(dec))
fmt_hex = make_fmt_sequence_aware(make_fmt_Any_aware(hex))



