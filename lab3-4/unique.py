class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)
            val = item.lower() if (self.ignore_case and isinstance(item, str)) else item
            if val not in self.seen:
                self.seen.add(val)
                return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    try:
        from lab_python_fp.gen_random import gen_random
    except ImportError:
        from gen_random import gen_random

    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data1)))

    data2 = gen_random(10, 1, 3)
    print(list(Unique(data2)))

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data3)))

    print(list(Unique(data3, ignore_case=True)))
