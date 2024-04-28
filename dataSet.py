import numpy as np
#Fuck you python and your 'self' bullshit
class dataSet():
    def __init__(self, setLength):
        self.arr = []
        while len(self.arr) < setLength:
            self.arr.append(np.random.uniform(0,np.pi*4))
        

    def split(self):
        self.trainingSet = []
        self.testingSet = []
        for i in range(len(self.arr)):
            if i%2 == 0:
                self.trainingSet.append(self.arr[i])
            else:
                self.testingSet.append(self.arr[i])
    def normalize(self):
        for i in range(len(self.trainingSet)):
            self.trainingSet[i] = (self.trainingSet[i] - np.min(self.trainingSet))/(np.max(self.trainingSet) - np.min(self.trainingSet))