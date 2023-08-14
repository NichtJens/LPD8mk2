from functools import wraps
from rich import print


def debug(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(format_call(f, args, kwargs))
        return f(*args, **kwargs)
    return wrapper


def format_call(f, args, kwargs):
    name = f.__name__
    str_args = [str(a) for a in args]
    str_kwargs = [f"{k}={v}" for k, v in kwargs.items()]
    combined = str_args + str_kwargs
    argument = ", ".join(combined)
    return f"call: {name}({argument})"



