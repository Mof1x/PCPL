import sys


def input_data():
    a, b, c = None, None, None
    if len(sys.argv[1:]) == 3:
        try:
            a, b, c = map(float, sys.argv[1:])

        except Exception:
            print("Ошибка ввода")

    while not all([isinstance(x, float) for x in (a, b, c)]):
        a, b, c = map(float, input("Введите коэффициенты a, b, c через пробел: ").split())

    return a, b, c


def D(a, b, c):
    return b ** 2 - 4 * a * c


def solve(a, b, c):
    match (a, b, c):
        case (0, 0, c):
            return "Любое число является корнем" if c == 0 else []
        case (0, b, c):
            return list({(-c / b) ** 0.5, -(-c / b) ** 0.5}) if -c / b >= 0 else []
        case (a, b, c):
            d = D(a, b, c)
            return [] if d < 0 else list(set(sum([[x ** 0.5, -x ** 0.5] if x >= 0 else [] for x in
                                                  [(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]], [])))


def run():
    a, b, c = input_data()
    solves = solve(a, b, c)
    if solves == "Любое число является корнем":
        print(solves)
    elif not solves:
        print("Нет корней")
    else:
        print(", ".join(map(str, solves)))

