class outputNode():
    def output(self, nodeIn, anode, bias, bnode):
        self.res = nodeIn * anode + bias * bnode
        return self.res