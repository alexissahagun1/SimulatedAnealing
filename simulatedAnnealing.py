import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from copy import deepcopy

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


def simulatedAnnealing(temp, iterations, tempDrop, tempChange, costs, currPath, currPathCost, graph):
    error = 1e-3  # delta para el ultimo paso (quenching step)

    # main loop
    costs.append(currPathCost)
    for i in range(iterations):
        i = random.randint(0, len(graph) - 1)
        j = random.randint(0, len(graph) - 1)
        currPath[i], currPath[j] = currPath[j], currPath[i]
        newPathCost = getPathCost(currPath)

        delta = newPathCost - currPathCost

        if(delta <= 0 or math.exp(-delta / temp) > random.random()):
            # si la ruta es mejor:
            currPathCost = newPathCost
        else:
            currPath[i], currPath[j] = currPath[j], currPath[i]

        costs.append(currPathCost)

        if (i % tempChange == 0):
            temp *= (1-tempDrop)


# def findValues(testValue, graph):
#     bestValues = [[1000000 for col in range(4)] for row in range(10)]
#     tempValues = np.random.normal(10000, 1000, size=(testValue))
#     tempDrops = np.random.normal(0.002, 0.0005, size=(testValue))
#     iterations = 200000
#     tempChanges = np.random.normal(120, 20, size=(testValue))
#     currPath = range(len(graph))
#     currPath = np.random.permutation(currPath)
#     currPathCost = getPathCost(currPath)

#     for i in range(testValue):
#         costs = []
#         simulatedAnnealing(deepcopy(tempValues[i]), iterations, deepcopy(tempDrops[i]), deepcopy(tempChanges[i]),
#                            costs, deepcopy(currPath), deepcopy(currPathCost), graph)
#         minCost = costs[-1]
#         for i in range(10):
#             if (minCost < bestValues[i][0]):
#                 value = []
#                 value.append(minCost)
#                 value.append(tempValues[i])
#                 value.append(tempDrops[i])
#                 value.append(tempChanges[i])
#                 bestValues.insert(i, value)
#                 del bestValues[-1]

#                 break
#     return bestValues


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


# tabla = findValues(1000, graph)
# print(tabla)

# Definir un camino incial y su costo
currPath = range(len(graph))
currPath = np.random.permutation(currPath)
currPathCost = getPathCost(currPath)
costs = []
temp = 10488
iterations = 200000
tempDrop = 0.00115
tempChange = 104
simulatedAnnealing(temp, iterations, tempDrop, tempChange,
                   costs, currPath, currPathCost, graph)


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

costIteration = range((iterations+1))

plt.plot(costIteration, costs, label="Costo: " + str(costs[-1]))
plt.legend(loc="upper left")

plt.show()

plotPath(currPath, xCoordinates, yCoordinates)
