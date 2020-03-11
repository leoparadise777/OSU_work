#TSP
#Project Group 6

import sys
import math
import time


# creating initial array to store city data
class City:
    def __init__(self, number, xCoord, yCoord):
        self.cityName = number
        self.x = xCoord
        self.y = yCoord


# read data from file and store information as arguments in city array.
def readFile(fileName):
    file = fileName + '.txt'
    with open(file) as data:
        cityArray = []
        for line in data:
            line = line.split()  # blank
            if line:             # lines
                cityInfo = []
                for value in line:
                    cityInfo.append(value)
                city = City(int(cityInfo[0]), int(cityInfo[1]), int(cityInfo[2]))  # new object
                cityArray.append(city)  # append the object to city array
    return cityArray


# write file
def writeFile(fileName, array):
    file = fileName + '.txt' + '.tour'
    with open(file, 'w') as outPutFile:
        for val in array:
            num = str(val)
            outPutFile.write(num + "\n")


# distance between two cities
def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    return int(round(math.sqrt(dx*dx + dy*dy)))


# candidate paths by nighest neighbor algorithm
def nearestNeighbor(cityArray, startCity):
    tourArray = [startCity]
    x = 0
    while x != len(cityArray)-1:
        i = tourArray[-1]
        lastDistance = float('inf')
        for j in cityArray:
            if j.cityName not in tourArray:
                d = distance(cityArray[i].x, cityArray[i].y, j.x, j.y)
                if d <= lastDistance:
                    lastDistance = d
                    currentCity = j.cityName
        tourArray.append(currentCity)
        x += 1
    return tourArray


# 2-OPT algorithm
def Two_OPT(cityArray, tour,i):
    g=i
    iter = 0
    while True:
        iter+=1
        minchange = 0
        swap = False
        for i in range(len(tour)-2):
            for j in range(i+2, len(tour)-1):
                change = distance(cityArray[tour[i]].x, cityArray[tour[i]].y, cityArray[tour[j]].x, cityArray[tour[j]].y)+ \
                distance(cityArray[tour[i+1]].x, cityArray[tour[i+1]].y, cityArray[tour[j+1]].x, cityArray[tour[j+1]].y) - \
                distance(cityArray[tour[i]].x, cityArray[tour[i]].y, cityArray[tour[i+1]].x, cityArray[tour[i+1]].y)- \
                distance(cityArray[tour[j]].x, cityArray[tour[j]].y, cityArray[tour[j+1]].x, cityArray[tour[j+1]].y)
                if minchange > change:
                    minI = i
                    minJ = j
                    minchange = change
                    swap = True
        if swap == True:
            temp = tour[minI+1]
            tour[minI+1] = tour[minJ]
            tour[minJ] = temp
        if g == 249:
            if minchange >= 0:  # if no changes
                break
        else:
            if i > iter:
                break
    return tour


# tour distance
def tourDistance(cityArray, tour):
        dist = 0
        for i in range(len(cityArray)-1):
            dist = dist + distance(cityArray[tour[i]].x,cityArray[tour[i]].y,cityArray[tour[i+1]].x, cityArray[tour[i+1]].y)
        lfCity = distance(cityArray[tour[0]].x, cityArray[tour[0]].y, cityArray[tour[-1]].x, cityArray[tour[-1]].y)
        dist += lfCity
        return dist


# main
def main():
    fileName = sys.argv[1]
    cityArray = readFile(fileName)
    finalDistance = float('inf')
    n = len(cityArray)
    if n <= 100:
        iterations = len(cityArray)
        i=250
    elif 100 < n and n <= 400:
        iterations = len(cityArray)*(3/4)
        i=249
    elif 400 < n and n <= 500:
        iterations = 20  # len(cityArray)*(1/4)
        i=30
    elif 500 < n and n <= 1000:
        iterations = 15
        i=15
    elif 1000 < n and n <= 2000:
        iterations = 2
        i=2
    else:
        iterations = 1
        i=1
    start = time.perf_counter()
    for p in range(int(iterations)):
        initTour = nearestNeighbor(cityArray, p)
        sumDist = tourDistance(cityArray, initTour)
        if sumDist <= finalDistance:
            finalDistance = sumDist
            finalTour = initTour
    optTour = Two_OPT(cityArray, finalTour, i)
    optDist = tourDistance(cityArray, optTour)
    end = time.perf_counter()
    elapsed = end - start  # amount of time
    optTour.insert(0,optDist)
    print(elapsed)
    writeFile(fileName,optTour)

if __name__ == "__main__":
    main()

