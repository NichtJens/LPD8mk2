from concurrent.futures import ThreadPoolExecutor
from itertools import count


class CallbackController:

    def __init__(self):
        self.indexer = count()
        self.callbacks = {}
        self.executor = ThreadPoolExecutor()

    def __repr__(self):
        return repr(self.callbacks)


    def add_callback(self, func):
        idx = next(self.indexer)
        self.callbacks[idx] = func


    def remove_callback(self, idx_or_func):
        if callable(idx_or_func):
            self.remove_callback_as_function(idx_or_func)
        else:
            self.remove_callback_as_index(idx_or_func)

    def remove_callback_as_function(self, func):
        indices = self.find_indices_for_function(func)
        for idx in indices:
            self.remove_callback_as_index(idx)

    def find_indices_for_function(self, func):
        indices = []
        for idx, cb in self.callbacks.items():
            if cb == func:
                indices.append(idx)
        return indices

    def remove_callback_as_index(self, idx):
        self.callbacks.pop(idx, None)


    def run_callbacks(self, *args, **kwargs):
        futures = {
            idx: self.executor.submit(cb, *args, **kwargs)
            for idx, cb in self.callbacks.items()
        }
        results = {
            idx: fut.result()
            for idx, fut in futures.items()
        }
        return results





if __name__ == "__main__":
    from time import sleep

    def f1(a, k=2):
        for i in range(3):
            print(i, a, k)
            sleep(0.1)
        return a, k

    def f2(c, k=4):
        for i in range(4):
            print(i, c, k)
            sleep(0.2)
        return c, k

    cc = CallbackController()
    print(cc)

    cc.add_callback(f1)
    cc.add_callback(f2)
    cc.add_callback(f1)
    cc.add_callback(f2)
    print(cc)

    res = cc.run_callbacks(123, 456)
    print(res)

    res = cc.run_callbacks(789, k=0)
    print(res)

    cc.remove_callback(0)
    print(cc)

    cc.remove_callback(f2)
    print(cc)

    res = cc.run_callbacks(1, k=2)
    print(res)



