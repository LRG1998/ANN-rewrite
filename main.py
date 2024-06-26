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
learning = 0.00001
error = 0
grace = 0.01
nodes = 6
dataset = ds.dataSet(1000)
dataset.split()
rmse = 1
dataset.normalize()
deltas = [-error]
numInput = dataset.trainingSet[0]
expected = numInput * float(inNode.getValue())



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
for x in range(nodes+1):
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
    deltas = [-error(calcResult(numInput))]
    for e in range(nodes):
        delta = (deltas[0] * secondLayer[e].weight* (sigmoid(outputs[e].res)*(1-sigmoid(outputs[e].res))))
        deltas.append(delta)
    return deltas

def update():
    for x in range(nodes):
        for y in range(2):
            hiddenNodes[y][x].updateWeight(numInput, calcDeltas()[x+1], learning)
        secondLayer[x].updateWeight(outputs[x].output(numInput, hiddenNodes[0][x].weight, 2, hiddenNodes[1][x].weight, biasNodes[x].weight), deltas[0], learning)
        biasNodes[-1].updateBias(learning, calcDeltas()[0])
        biasNodes[x].updateBias(learning, calcDeltas()[x+1])
    

def calcResult(numIn):
    result = 0
    for x in range(nodes):
        result +=  outputs[x].output(numIn, hiddenNodes[0][x].weight, 2, hiddenNodes[1][x].weight, biasNodes[x].weight) + secondLayer[x].weight
    result += biasNodes[-1].weight
    return result
def train():
    numInput = dataset.trainingSet[0]
    loop = 0
    fileoutput = open("output.csv", "w")
    while abs(error(calcResult(numInput))) > grace:
        for t in range(len(dataset.trainingSet)):
            numInput = dataset.trainingSet[t]
        update()
        if loop % 100 == 0:
            rmse = np.sqrt(np.mean((error(calcResult(numInput))**2)))
            fileoutput.write(str(rmse) + "\n")
            print(rmse)
        loop += 1
        if loop >= 30000000:
            break
    fileoutput.close()



def test():
    numInput = dataset.testingSet[0]
    for x in range(len(dataset.testingSet)):
        numInput = dataset.testingSet[x]
        expected = numInput * float(inNode.getValue())
        print(str(numInput) + " , " + str(expected) + ", " + str(calcResult(numInput)))
        rmse = np.sqrt(np.mean((error(calcResult(numInput))**2)))


train()
test()