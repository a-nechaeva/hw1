import math
import numpy as np


def y1(x):
    return x**3 - 0.5 * x**2 + x + 1


def y2(x):
    return math.log(x + 1) + 1


def y3(x):
    return (1 / 100) * math.exp(x) * (math.cos(100 * x) + 100)


def y4(x):
    return math.exp(x)


def zero_norm(func1, func2):
    return np.linalg.norm(func1 - func2, ord=0)


def first_norm(func1, func2):
    return np.linalg.norm(func1 - func2, ord=1)


def second_norm(func1, func2):
    return np.linalg.norm(func1 - func2, ord=2)


if __name__ == '__main__':
    x_values = np.linspace(-0.1, 0.1, 10)
    y1_v = y1(x_values)
    y2_v = y2(x_values)
    y3_v = y3(x_values)
    y4_v = y4(x_values)

    print("zero_norm:", "\n")
    z_12 = zero_norm(y1_v, y2_v)
    z_13 = zero_norm(y1_v, y3_v)
    z_14 = zero_norm(y1_v, y4_v)

    if z_12 < 1:
        print("y1, y2: ", z_12)

    if z_13 < 1:
        print("y1, y3: ", z_13)

    if z_14 < 1:
        print("y1, y4: ", z_14)


