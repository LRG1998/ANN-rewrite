import numpy as np

class biasNode():
    def __init__(self):
        self.weight = np.random.uniform(-1,1)

    def updateBias(self, learning, delta):
        self.weight += learning * delta