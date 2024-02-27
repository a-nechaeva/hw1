import math


def y1(x):
    return x**3 - 0.5 * x**2 + x + 1


def y2(x):
    return math.log(x + 1) + 1


def y3(x):
    return (1 / 100) * math.exp(x) * (math.cos(100 * x) + 100)


def y4(x):
    return math.exp(x)



if __name__ == '__main__':


