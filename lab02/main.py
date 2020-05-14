from functions import getPoints, twoStepInterpolation, getTable

pointsList = getTable()

x = float(input("Input x - "))
n1 = int(input("Input n for x - "))
y = float(input("Input y - "))
n2 = int(input("Input n for y - "))

pointsListNew = getPoints(x, n1, pointsList)
resZ = twoStepInterpolation(pointsListNew, x, n1, y, n2)

print("result Z =", resZ)

'''
x = float(input("Input x - "))
n = int(input("Input n - "))
eps = float(input("Input EPS - "))

pointsListNew = getPoints(x, n, pointsList)

resY = interpolation(pointsListNew, x, n)
print("Interpolation result (y) - ", resY)

pointsListRev = reverse(pointsList)
pointsListRevNew = getPoints(x, n, pointsListRev) 
pointsListRev = getPoints(0.0, n, pointsListRev)

resX = interpolation(pointsListRev, 0.0, n)
print("Reverse interpolation result (x)  - ", resX)

print(pointsList, len(pointsList))
xAve = halfwayDivMeth(pointsList, eps, len(pointsList))
print("Halfway division method: ")
for i in (xAve): 
    print(i)
'''