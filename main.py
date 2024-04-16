import numpy as np
import hiddenNode
import dataSet as ds
import matplotlib as mp
import outputNode

'''rewrite of spongegar ANN'''
loop = 0
setIndex = 0
learning = 0.0001
error = 0
grace = 0.01
nodes = 1 
dataset = ds.dataSet(1000)
dataset.split()
rmse = 0
dataset.normalize()
deltas = [-error]
np.random.seed(1)
numInput = dataset.trainingSet[0]
expected = numInput * 2


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
    return error

def calcDeltas():
    deltas = [-1 * error(calcResult())]
    for e in range(nodes):
        deltas.append(deltas[0] * secondLayer[e].weight)
    return deltas

def update():
    for x in range(nodes):
        for y in range(2):
            hiddenNodes[y][x].updateWeight(numInput, calcDeltas()[x+1], learning)
        secondLayer[x].updateWeight(numInput, deltas[0], learning)

def calcResult():
    result = 0
    for x in range(nodes):
        result = secondLayer[x].weight * outputs[x].output(numInput, hiddenNodes[0][x].weight, 2, hiddenNodes[1][x].weight)
    return result
def train():
    loop = 0
    fileoutput = open("output.csv", "w")
    while abs(error(calcResult())) > grace:
        for t in range(len(dataset.trainingSet)):
            numinput = dataset.trainingSet[t]
        update()
        if loop % 100 == 0:
            rmse = np.sqrt(np.mean((error(calcResult())**2)))
            fileoutput.write(str(rmse) + ", " + "\n")
        loop += 1
    fileoutput.close()
    for x in range(nodes):
        for y in range(2):
            print(hiddenNodes[y][x].weight)

def test():
    numInput = dataset.testingSet[0]
    for x in range(len(dataset.testingSet)):
        numInput = dataset.testingSet[x]
        print(str(error(calcResult())) + ", " + str(numInput))

train()

test()