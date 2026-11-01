import time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        print(f"time: {elapsed}")


@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start_time
        print(f"time: {elapsed}")


if __name__ == '__main__':
    from time import sleep

    with cm_timer_1():
        sleep(1.5)

    with cm_timer_2():
        sleep(1.5)
