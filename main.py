import numpy as np
import hiddenNode
import dataSet as ds
import matplotlib as mp
import outputNode

'''rewrite of spongegar ANN'''


error = 0

nodes = 4
dataset = ds.dataSet(1000)
dataset.split()

deltas = [-error]
np.random.seed(1)
numInput = 2
output = numInput * 2

#Build hidden Nodes

hiddenNodes = [[0 for x in range(nodes)]for y in range(2)]
for x in range(nodes):
    for y in range(2):
        hiddenNodes[y][x] = hiddenNode.hiddenNode()
#Building the second layer
secondLayer = []
for x in range(nodes):
    secondLayer.append(hiddenNode.hiddenNode())

outputs = []
for x in range(nodes):
    outputs.append(outputNode.outputNode())

def sigmoid(x):
    out = 1/(1 + np.exp(-x))
    return out

def error(answer):
    error = answer - expected

def calcDeltas():
    deltas = [-error]
    for e in range(nodes):
        deltas.append(deltas[0] * secondLayer[e])

def update():
    for x in range(nodes):
        for y in range(2):
            hiddenNodes[y][x].updateWeight(numInput, deltas[x+1], secondLayer[x])

def calcResult():
    result = 0

