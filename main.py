import numpy as np
import hiddenNode
'''rewrite of spongegar ANN'''


error = 0

nodes = 4

deltas = [-error]

input = 2
output = input* 4

def sigmoid(x):
    out = 1/(1 + np.exp(-x))
    return out

print(sigmoid(4))
testNode = hiddenNode.hiddenNode()
print(testNode.weight)