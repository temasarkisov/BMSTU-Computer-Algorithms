import matplotlib as plt
from math import *
from numpy import *

def gauss(func, a, b, num_of_nodes):
    args, coeffs = leggauss(num_of_nodes)
    res = 0

    for i in range(num_of_nodes):
        res += (b - a) / 2 * coeffs[i] * func(t_to_x(args[i], a, b))

    return res


def simpson(func, a, b, num_of_nodes):
    if (num_of_nodes < 3 or num_of_nodes & 1 == 0):
        raise ValueError

    h = (b - a) / (num_of_nodes - 1)
    x = a
    res = 0

    for _ in range((num_of_nodes - 1) // 2):
        res += func(x) + 4 * func(x + h) + func(x + 2 * h)
        x += 2 * h

    return res * (h / 3)


def main_function(param):
    subfunc = lambda x, y: 2 * cos(x) / (1 - (sin(x) ** 2) * (cos(y) ** 2))
    func = lambda x, y: (4 / pi) * (1 - exp(-param * subfunc(x, y))) * cos(x) * sin(x)
    return func


def func_2_to_1(func2, value):
    return lambda y: func2(value, y)


def t_to_x(t, a, b):
    return (b + a) / 2 + (b - a) * t / 2


def integrate2(func, limits, num_of_nodes, integrators):
    inner = lambda x: integrators[1](func_2_to_1(func, x), limits[1][0], limits[1][1], num_of_nodes[1])
    return integrators[0](inner, limits[0][0], limits[0][1], num_of_nodes[0])


def tao_graph(integrate_func, ar_params, label):
    X = list()
    Y = list()
    for t in arange(ar_params[0], ar_params[1] + ar_params[2], ar_params[2]):
        X.append(t)
        Y.append(integrate_func(t))
    plt.plot(X, Y, label=label)


def generate_label(n, m, func1, func2):
    res = "N = " + str(n) + ", M = " + str(m) + ", Methods = "
    res += "Simpson" if func1 == simpson else "Gauss"
    res += "-Simpson" if func2 == simpson else "-Gauss"
    return res

end = False


while not end:
    N = int(input("N: "))
    M = int(input("M: "))

    param = float(input("Enter parametr: "))
    mode = bool(int(input("Enter external method: ")))
    func1 = simpson if mode else gauss
    mode = bool(int(input("Enter internal method: ")))
    func2 = simpson if mode else gauss
    param_integrate = lambda tao: integrate2(main_function(tao), [[0, pi / 2], [0, pi / 2]], [N, M], [func1, func2])
    print("Result:", param_integrate(param))

    try:
        tao_graph(param_integrate, [0.05, 10, 0.05], generate_label(N, M, func1, func2))
    except ValueError:
        print("Be careful with simpson: argument should be > 2 and not even (3, 5...);")
    except ZeroDivisionError:
        print("Can't use 2 Simpsons, zero in denominator")
    end = bool(int(input("End? (0 - No, 1 - Yes): ")))

