def getTable():
    pointsList = []
    print("      TABLE")
    print("------------------")
    print("  X", "\t|", "     Y")
    print("------------------")
    with open("data2.txt") as file:
        for line in file:
                
            print(list(map(float, line.split()))[0], "\t|   ", list(map(float, line.split()))[1])
    
    pointsList.sort()
    return pointsList

def getPoints(x, n, pointsList):
    minList = list(filter(lambda line: line[0] <= x, pointsList))
    maxList = list(filter(lambda line: line[0] > x, pointsList))
 
    checkList = lambda curList, n: len(curList) < (n + 1) // 2
 
    if len(minList + maxList) < n + 1:
        pointsList = minList + maxList
    elif checkList(minList, n):
        pointsList = minList + maxList[:n + 1 - len(minList)]
    elif checkList(maxList, n):
        pointsList = minList[-(n + 1 - len(maxList)):] + maxList
    else:
        stopPoint = (len(minList) > (n // 2) and (n // 2) + 1) or (n // 2)
        pointsList = minList[-stopPoint:] + maxList[:(n + 1) - stopPoint]

    return pointsList

def calcY(xi, xj, yi, yj):
    return ((yi - yj) / (xi - xj))

def interpolation(pointsList, x, n):
    step = 1
    listY = list(map(lambda line: line[1], pointsList))
    print("listY :", listY)
    resY = listY[0]
    mulX = 1
 
    if len(pointsList) <= n: n = len(pointsList) - 1
 
    while len(listY) != 1:
        listY = list(map(lambda i: calcY(pointsList[i][0], pointsList[i + step][0], listY[i], listY[i + 1]), range(n)))
        mulX *= (x - pointsList[0 + step - 1][0])
        resY += mulX * listY[0]
        n -= 1
        step += 1

    return resY

def reverse(pointsList):
    pointsList = list(map(lambda line: tuple(reversed(line)), pointsList))
    pointsList.sort(key=lambda list: list[0])
    
    temp = pointsList[-1]
    pointsList = [pointsList[i] for i in range(len(pointsList) - 1) if pointsList[i][0] < pointsList[i + 1][0]]
    pointsList.append(temp)

    return pointsList

def closeEnough(x, y):
    if abs(x - y) < 0.00000001:
        return 1
    return 0

def average(x, y):
    return (x + y) / 2

def search(negPoint, posPoint, pointsList, eps, n):
    midPoint = average(negPoint, posPoint)

    if closeEnough(negPoint, posPoint):
        return midPoint

    testValue = interpolation(pointsList, midPoint, n)
    #print("testValue =", testValue, midPoint)
    
    if testValue > 0:
        return search(negPoint, midPoint, pointsList, eps, n)
    elif testValue < 0:
        return search(midPoint, posPoint, pointsList, eps, n)

    return midPoint 

def halfwayDivMeth(pointsList, eps, n):
    midList = []
    
    for i in range (n - 1):
        if (pointsList[i][1] * pointsList[i + 1][1] <= 0):
            #print("Pair: ", pointsList[i][0], pointsList[i + 1][0])
            negPoint = pointsList[i][0]
            posPoint = pointsList[i + 1][0]

            midList.append(search(negPoint, posPoint, pointsList, eps, n))

    return midList

pointsList = getTable()

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
