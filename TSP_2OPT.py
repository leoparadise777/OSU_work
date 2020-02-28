#TSP

import sys
import math
import time

#city class for creating initial array to store city data
class City:
    def __init__(self, number, xCoord, yCoord):
        self.cityName = number
        self.x = xCoord
        self.y = yCoord

#tourPayload class for holding two items, the tourArray of optimal length and the distance of tour
class tourPayload:
    def __init__(self, tourArray, distance):
        self.tourArray = tourArray
        self.distance = distance

#read data from provided file and store city info as arguements in city array.
def readFile(fileName):
    file = fileName + '.txt'
    with open(file) as data:
        cityArray = []
        for line in data:
            line = line.split() # to deal with blank
            if line:            # lines (take the line and grab individual elements in value)
                cityInfo = []
                for value in line:
                    cityInfo.append(value)
                city = City(int(cityInfo[0]), int(cityInfo[1]), int(cityInfo[2])) #create a new object
                cityArray.append(city)  #append the object to the city array
    return cityArray

#write file
def writeFile(fileName, array):
    file = fileName + '.txt' + '.tour'
    with open(file, 'w') as outPutFile:
        for val in array:
            num = str(val)
            outPutFile.write(num + "\n")

#compute distance between two cities
def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    return int(round(math.sqrt(dx*dx + dy*dy)))

#generates candidate paths using neighest neighbor algorithm
def nearestNeighbor(cityArray, startCity, bestDistance):
    tourArray = [startCity]
    x = 0
    tourLength = float(0) #initialize this tour length to zero
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
        tourLength = tourLength + d   #update the tourLength with the distance of the new addition
        if tourLength > bestDistance: #if the tour being constructed is greater than our bestDistance then...
            return 0                  #short circuit and return 0
        x += 1
        payload = tourPayload(tourArray, tourLength) #create a new payload object to pass back to main
    return payload #return the payload, this is more optimal than last function call

#optimizes best path from nearestNeighbor using 2-OPT algorithm
def Two_OPT(cityArray, tour):
    while True:
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
        if minchange >= 0:  #if no changes made, break out of loop
            break
    return tour

#compute tour distance
def tourDistance(cityArray, tour):
        dist = 0
        for i in range(len(cityArray)-1):  #the -1 remedies out or range errors, no allowing you to calculate a distance from the last city
            dist = dist + distance(cityArray[tour[i]].x,cityArray[tour[i]].y,cityArray[tour[i+1]].x, cityArray[tour[i+1]].y)
        lfCity = distance(cityArray[tour[0]].x, cityArray[tour[0]].y, cityArray[tour[-1]].x, cityArray[tour[-1]].y)  #add in distance from first to last.
        dist += lfCity
        return dist

def main():
    fileName = sys.argv[1]
    cityArray = readFile(fileName)
    finalDistance = float('inf')
    n = len(cityArray)
    if n <= 100:
        iterations = len(cityArray)
    elif 100 < n and n <= 500:
        iterations = len(cityArray)*(3/4)
    elif 500 < n and n <= 1000:
        iterations = len(cityArray)*(1/2)
    elif 1000 < n and n <= 2000:
        iterations = len(cityArray)*(1/4)
    else:
        iterations = 1
    start = time.time()
    for p in range(int(iterations)):          #create tours for all possible start points
        initTour = nearestNeighbor(cityArray, p, finalDistance) #pass the current best distance (aka finalDistance) into nearestNeighbor function
        if initTour != 0: 			          #if initTour is not zero, then we have a tour that is the new best tour
           finalTour = initTour.tourArray     #set our finalTour to initTour's tourArray
           finalDistance = initTour.distance  #set our finalDistance to initTour's distance to be passed into nearestNeighbor next iteration
    optTour = Two_OPT(cityArray, finalTour)
    optDist = tourDistance(cityArray, optTour)
    end = time.time()
    elapsed = end - start #amount of time to execute insertion sort
    optTour.insert(0,optDist)
    print(elapsed)
    writeFile(fileName,optTour)

if __name__ == "__main__":
    main()
