# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

class Node:
    def __init__(self, nodeID, val):
        self.nodeID = nodeID
        self.val = val
        self.connections = []
        # self.connections.append(connections)
    
    def set_val(self, val):
        self.val = val
    def get_val(self):
        return self.val
    
    def add_connection(self, otherNode):
        self.connections.append(otherNode)
    def get_connections(self):
        return self.connections
        
    
    # super bad recurssive multiply search functions
    def multiplyUp(self, findIndex, cameFrom):
        
        if self.nodeID == findIndex:
            # base case
            return self.val
            
        else:
            # keep searching through connections
            for connection in self.connections:
                if (connection != cameFrom):
                    rec = connection.multiplyUp(findIndex, self)
                    if rec != 0:
                        # print(f"{rec} x {self.val} = {rec * self.val}")
                        return rec * self.val
                    if rec == 0:
                        pass 
            return 0
            


testCases = get_number()

for _ in range(testCases):
    nodeList = []
    outputList = []
    nodeCount = get_number()
    
    for n in range(nodeCount):
        weight = get_number()
        nodeList.append(Node(n, weight))
    
    # print(len(nodeList))
    
    for n in range(nodeCount - 1):  # create connections
        u = get_number() -1
        v = get_number() -1
        
        nodeList[u].add_connection(nodeList[v])
        nodeList[v].add_connection(nodeList[u])
    
    operationsCount = get_number()
    
    for o in range(operationsCount):
        
        t = get_number()    # 1 or 2, denoting type of operation
                            # t = 1: change node u with one for weight v
                            # t = 2: calculate multiplications from u to v % 1000000007
        u = get_number()-1
        v = get_number()
        
        if t == 1:
            # set node u to weight v
            nodeList[u].set_val(v)
        else:
            # calculate multiplications from u to v % 1000000007
            
            output = nodeList[u].multiplyUp(v-1, nodeList[u]) % 1000000007
            
            
            outputList.append(output)
            
            
# for node in nodeList:
#     print(node.get_val())

for line in outputList:
    print(line)