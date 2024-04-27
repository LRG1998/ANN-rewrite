import numpy as np

class outputNode():
    def output(self, nodeIn, anode, nodeIn2, bnode):
        self.res = 1/(1 + np.exp(-(nodeIn*anode + nodeIn2 * bnode + 1)))
        return self.res
