import numpy as np


class hiddenNode():
    def __init__(self):
        self.weight = np.random.uniform(-1,1)


    def updateWeight(self, x1, dn, l):
        self.weight += l * x1 * dn


# function to remember for updating weights is hn = l*x1*dn * hn this will be the hidden node
# l is the learning rate
# x1 is the value of the first input node
# dn is the delta
# hn is the current weight. 
