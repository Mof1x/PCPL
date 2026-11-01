import random


def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    result = list(gen_random(5, 1, 3))
    print(", ".join(map(str, result)))

    result2 = list(gen_random(10, 10, 20))
    print(result2)
