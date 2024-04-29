import numpy as np

class outputNode():
    def output(self, nodeIn, anode, nodeIn2, bnode, biasnode):
        self.res = 1/(1 + np.exp(-(nodeIn*anode + nodeIn2 * bnode + biasnode)))
        return self.res
