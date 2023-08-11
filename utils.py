from collections import defaultdict
from collections.abc import Sequence, Mapping
from consts import Any


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
        found = sint(found) #TODO: this is probably not needed / should be fixed elsewhere
#        print("compare", found, ref, "->", found == ref) #TODO: remove
        if found != ref:
            msg = f'"{name}" should be {ref} ({shex(ref)}) but is {found} ({shex(found)})'
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


def shex(i):
    if isinstance(i, int):
        return hex(i)
    else:
        return [hex(int(j)) for j in i]



