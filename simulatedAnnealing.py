import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import math

# Leer archivo csv y guradar sus conetinidos dentro de un array


def readGraphFile(fileName):
    graph = []

    with open(fileName) as csvfile:
        csvReader = csv.reader(csvfile)
        for node in csvReader:
            graph.append(node)
    return graph

# Costo de camino


def getPathCost(path):
    cost = 0

    for i in range(len(path) - 1):
        cost += int(graph[path[i]][path[i+1]])
    cost += int(graph[path[len(path) - 1]][path[0]])

    return cost


# Plot de camino

def plotPath(path, xCoordinates, yCoordinates):
    for i in range(len(path) - 1):
        # Line from node i to node i + 1
        xValues = [xCoordinates[path[i]], xCoordinates[path[i+1]]]
        yValues = [yCoordinates[path[i]], yCoordinates[path[i+1]]]
        plt.plot(xValues, yValues)
    # Line froma last to first node
    xValues = [xCoordinates[path[len(path) - 1]], xCoordinates[path[0]]]
    yValues = [yCoordinates[path[len(path) - 1]], yCoordinates[path[0]]]
    plt.plot(xValues, yValues)

    plt.scatter(xCoordinates, yCoordinates)
    plt.show()

# neighbor


def getNewPath(path):
    randIndex1 = random.randint(0, len(path)-1)
    randIndex2 = random.randint(0, len(path)-1)

    temp = path[randIndex1]
    path[randIndex1] = path[randIndex2]
    path[randIndex2] = temp

    return path


# MAIN CODE
graph = readGraphFile('cities_128.csv')

# Leer coordenadas de archivo txt (separacion es 7 espacios)
nodeCoordinates = np.loadtxt(
    "coordinates.txt", delimiter="       ", unpack=False)

xCoordinates = []
yCoordinates = []

for i in range(len(nodeCoordinates)):
    xCoordinates.append(nodeCoordinates[i][0])
    yCoordinates.append(nodeCoordinates[i][1])

temp = 1000
iterations = 200000
tempDrop = 0.001
error = 1e-3  # delta para el ultimo paso (quenching step)

# obtener camino inicial
currPath = range(len(graph))
currPath = np.random.permutation(currPath)

currPathCost = getPathCost(currPath)

# main loop
costs = []
costs.append(currPathCost)
for i in range(iterations):
    newPath = getNewPath(currPath)
    newPathCost = getPathCost(newPath)

    if(newPathCost < currPathCost):
        # si la ruta es mejor:
        currPath = newPath
        currPathCost = newPathCost
    else:
        # si la ruta es peor:
        delta = newPathCost - currPathCost

        if(math.exp(-delta / temp) > random.random()):
            currPath = newPath
            currPathCost = newPathCost

    costs.append(currPathCost)
    temp = temp * (1-tempDrop)
    for i in range(len(currPath) - 1):
        # Line from node i to node i + 1
        xValues = [xCoordinates[currPath[i]], xCoordinates[currPath[i+1]]]
        yValues = [yCoordinates[currPath[i]], yCoordinates[currPath[i+1]]]
        plt.plot(xValues, yValues)
    # Line froma last to first node
    xValues = [
        xCoordinates[currPath[len(currPath) - 1]], xCoordinates[currPath[0]]]
    yValues = [
        yCoordinates[currPath[len(currPath) - 1]], yCoordinates[currPath[0]]]
    plt.plot(xValues, yValues)

    plt.scatter(xCoordinates, yCoordinates)
    plt.pause(0.001)
    plt.clf()


# plt.show()

costIteration = range((iterations+1))

plt.plot(costIteration, costs)
# plt.show()

plotPath(currPath, xCoordinates, yCoordinates)

# i va de 1-10
# intercambiar dos ciudades random
