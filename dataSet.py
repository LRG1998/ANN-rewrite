import numpy as np
#Fuck you python and your 'self' bullshit
class dataSet():
    def __init__(self, setLength):
        self.arr = []
        while len(self.arr) < setLength:
            self.arr.append(np.random.uniform(-5,5))
        

    def split(self):
        self.trainingSet = []
        self.testingSet = []
        for i in range(len(self.arr)):
            if i%2 == 0:
                self.trainingSet.append(self.arr[i])
            else:
                self.testingSet.append(self.arr[i])
