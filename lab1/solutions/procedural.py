import sys


def D(a, b, c):
    return b ** 2 - 4 * a * c


def exist_solve(a, b, c):
    return D(a, b, c) >= 0 and not (a == 0 and b == 0 and c != 0)


def input_data():
    coef = []
    try:
        for x in sys.argv[1:]:
            coef.append(float(x))
    except Exception:
        print("Ошибка ввода")
        coef.clear()
    while len(coef) != 3:
        try:
            coef = list(map(float, input("Введите коэффициенты a, b, c через пробел: ").split()))
        except Exception:
            print("Ошибка ввода")
    return coef


def solve(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "Любое число является корнем"

    if a == 0:
        if b == 0:
            return []
        x = -c / b
        return list({x ** 0.5, -x ** 0.5}) if x >= 0 else []

    d = D(a, b, c)
    if d < 0:
        return []
    elif d == 0:
        x = -b / (2 * a)
        return list({x ** 0.5, -x ** 0.5}) if x >= 0 else []
    else:
        solves = []
        x1, x2 = (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
        for x in (x1, x2):
            if x >= 0:
                solves.extend(list({x ** 0.5, -x ** 0.5}) if x >= 0 else [])
        return solves


def run():
    a, b, c = input_data()

    solves = list(map(str, solve(a, b, c)))

    if solves == "Любое число является корнем":
        print(solves)
    elif not solves:
        print("Нет корней")
    else:
        print(", ".join(solves))
    return None
