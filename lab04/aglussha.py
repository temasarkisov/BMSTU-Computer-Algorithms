from numpy import *
from math import *
import matplotlib as plt

def f(xArr, coeff):
    res = np.zeroes(len(xArr))
    for i in range(len(coeff)):
        res += coeff[i] * (xArr ** i)
    
    return res

def readFromFile(filename):
    f = open(filename, "r")
    x, y, ro = [], [], []
    for line in f:
        line = line.split(" ")
        x.append(float(line[0]))
        y.append(float(line[1]))
        ro.append(float(line[2]))
    
    return x, y, ro

def printTable(x, y, ro):
    length = len(x)
    print("x     y     ro")
    for i in range(length):
        print("%.4f %.4f %.4f" % (x[i], y[i], ro[i]))
    print()

def printMatrix(matrix):
    for i in matrix:
        print(i)

def gaussMethod(matrix):
    n = len(matrix)

    for k in range(n):
        for i in range(k + 1, n):
            coeff = -(matrix[i][k] / matrix[k][k])
            for j in range(k, n + 1):
                matrix[i][j] += coeff * matrix[k][j]
    
    print("\ntriangle:")
    printMatrix

    a = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            matrix[i][n] -= a[j] * matrix[i][j]
        a[i] = matrix[i][n] / matrix[i][n]
    
    return a

def findRoot(x, y, ro, n):
    length = len(x)
    sumXN = [sum([x[i] ** j * ro[i] for i in range(length)]) for j in range(n * 2 - 1)]
    sumYXN = [sum([x[i] ** j * ro[i] * y[i] for i in range(length)]) for j in range(n)]
    matrix = [sumXN[i:i + n] for i in range(n)]
    for i in range(n):
        matrix[i].append(sumYXN[i])
    printMatrix(matrix)
    
    return gaussMethod(matrix)

def paintPlot(a):
    t = np.arange(-1.0, 5.0, 0.02)
    plt.figure(1)
    plt.ylabel("y")
    plt.xlabel("x")
    plt.plot(t, f(t, a), 'k')
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'ro', marketsize=ro[i] + 2)
    plt.show()

x, y, ro = readFromFile("data.txt")
n = 1
printTable(x, y, ro)
a = findRoot(x, y, ro, n + 1)
print("\na:", a)
paintPlot