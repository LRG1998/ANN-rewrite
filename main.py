import numpy as np
import hiddenNode
import dataSet as ds
import matplotlib as mp
import outputNode
import biasNode
from inputNode import inputNode

'''rewrite of spongegar ANN'''


inputval: float = input("What are you multiplying values by? ")
inNode = inputNode()
inNode.create(inputval)
loop = 0
setIndex = 0
learning = 0.0001
error = 0
grace = 0.00001
nodes = 80
dataset = ds.dataSet(1000)
dataset.split()
rmse = 1
dataset.normalize()
deltas = [-error]
numInput = dataset.trainingSet[0]
expected = np.sin( 2* numInput)


#Build hidden Nodes

hiddenNodes = [[0 for x in range(nodes)]for y in range(2)]
for x in range(nodes):
    for y in range(2):
        hiddenNodes[y][x] = hiddenNode.hiddenNode()
#Building the second layer
secondLayer = []
for x in range(nodes+1):
    secondLayer.append(hiddenNode.hiddenNode())

#Building Bias nodes
biasNodes = []
for x in range(nodes):
    biasNodes.append(biasNode.biasNode())

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
    deltas = [-1 * error(calcResult(numInput))]
    for e in range(nodes):
        deltas.append(deltas[0] * secondLayer[e].weight)
    return deltas

def update():
    for x in range(nodes):
        for y in range(2):
            hiddenNodes[y][x].updateWeight(numInput, calcDeltas()[x+1], learning)
        secondLayer[x].updateWeight(numInput, deltas[0], learning)
        biasNodes[x].updateBias(learning, calcDeltas()[x+1])

def calcResult(inVal):
    result = 0
    for x in range(nodes):
        result += secondLayer[x].weight * outputs[x].output(inVal, hiddenNodes[0][x].weight, 2, hiddenNodes[1][x].weight) - (1*biasNodes[0].weight)
    return result
def train():
    loop = 0
    fileoutput = open("output.csv", "w")
    while abs(error(calcResult(numInput))) > grace:
        for t in range(len(dataset.trainingSet)):
            numinput = dataset.trainingSet[t]
        update()
        if loop % 100 == 0:
            rmse = np.sqrt(np.mean((error(calcResult(numInput))**2)))
            fileoutput.write(str(rmse) + "\n")
            print(rmse)
        loop += 1
        if loop >= 3000000:
            break
    fileoutput.close()
    for x in range(nodes):
        for y in range(2):
            print(hiddenNodes[y][x].weight)

def test():
    dataset.testingSet = np.sort(dataset.testingSet)
    numInput = dataset.testingSet[0]
    expected = np.sin(2*numInput)
    sinFile = open("sinfile.csv", "w")
    for x in range(len(dataset.testingSet)):
        numInput = dataset.testingSet[x]
        expected = np.sin(2*numInput)
        sinFile.write(str(calcResult(numInput))+"," + str(numInput) + "\n")
    sinFile.close()

train()
test()