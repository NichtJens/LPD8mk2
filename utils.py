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



