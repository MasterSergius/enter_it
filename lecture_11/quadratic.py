import math
import sys


def get_discriminant(a, b, c):
    return b * b - 4 * a * c


def get_roots(a, b, d):
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return x1, x2


def solve_equation():
    a, b, c = [float(number) for number in sys.argv[1:]]
    d = get_discriminant(a, b, c)
    if d < 0:
        print("No solution")
        return
    x1, x2 = get_roots(a, b, d)
    print(f"x1={x1}, x2={x2}")



if __name__ == "__main__":
    solve_equation()
