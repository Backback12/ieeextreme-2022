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

# class Node {
#     def __init__(self, nodeTyp, nodeID, character, leftChildID=None, rightChildID = None):
#         self.nodeType = nodeTyp
#         self.nodeID = nodeID
#         self.character = character
#         self.leftChildID = leftChildID
#         self.rightChildID = rightChildID
#         self.rightChild = None
#         self.leftChild = None
    
    
#     def get_left_id(self):
#         return self.leftChildID
#     def get_right_id(self):
#         return self.rightChildID
    
#     def set_left(self, node):
#         self.leftChild = node
#     def set_right(self, node):
#         self.rightChild = node
#     def get_left(self):
#         return self.leftChild
#     def get_right(self):
#         return self.rightChild
        
    
#     def searchForID(self, getID):
#         if self.leftChildID == getID:
#             return self.leftChild
#         elif self.rightChildID == getID:
#             return self.rightChild
        
#         else:
#             # search childs
#             if self.leftChild != None:
#                 return self.leftChild.searchForID()
#             elif self.rightChild != None:
#                 # search right
#             return self.rightChild.searchForID()
        
#         else:
#             return None
        
# }

class Node:
    def __init__(self, nodeType, nodeID, char, leftID=None, rightID=None, lang=None):
        self.nodeType = nodeType
        self.nodeID = nodeID
        self.char = char
        self.leftID = leftID
        self.rightID = rightID
        self.left = None
        self.right = None
        self.up = None
        
        self.lang = lang
    
    def getID(self):
        return self.nodeID
    
    def set_up(self, up):
        self.up = up
    def get_up(self):
        return self.up
    
    def set_left(self, left):
        self.left = left
        self.left.set_up(self)
    def get_left(self):
        return self.left
        
    def set_right(self, right):
        self.right = right
        self.right.set_up(self)
    def get_right(self):
        return self.right
        
    
    def get_left_id(self):
        return self.leftID
    def get_right_id(self):
        return self.rightID
    
    
    # returns NODE OBJECT if matches ID
    # else None
    def getByID(self, searchID):
        output = None
        
        # Node matches
        if self.nodeID == searchID:
            output = self.get_up()
        else:
            # check children
            if self.leftID == searchID:
                output = self
            elif self.rightID == searchID:
                output = self
            
            
            elif self.left != None:
                output = self.left.getByID(searchID)
            if output == None:
                if self.right != None:
                    output = self.right.getByID(searchID)
        
        return output
    
    
    
    
    
    def get_type(self):
        return self.nodeType
    def get_char(self):
        return self.char
    def get_lang(self):
        return self.lang
        
    # checks if node has char
    # and checks children
    # returns list of languages (unordered)
    def getLang(self, phrase):
        if self.nodeType == 'L':
            return [self.lang]
        else:
            # internal leaf
            
            if self.char in phrase:
                # absolutely IS left
                return self.left.getLang(phrase)
            
            else:
                # might be left or right still
                return self.left.getLang(phrase) + self.right.getLang(phrase)


nodeCount = get_number()
phraseCount = get_number()
top = None

addLater = []

for _ in range(nodeCount):
    nodeType = get_word()
    
    if nodeType == 'I':
        # INTERNAL NODE
        nodeID = get_number()
        character = get_word()
        leftCh = get_number()
        rightCh = get_number()
        lang = None
    else:
        # LEAF NODE
        nodeID = get_number()
        character = None
        leftCh = None
        rightCh = None
        lang = get_word()
    
    addNode = Node(nodeType, nodeID, character, leftCh, rightCh, lang)
    
    
    if top == None:
        top = addNode
    else:
        parentNode = top.getByID(nodeID)
        
        if parentNode == None:
            # found no link, check above???????
            
            if leftCh == top.getID():
                # 
                # print(f"added {addNode.getID()} normally to top, moved {top.getID()} down")
                addNode.set_left(top)
                top = addNode
            elif rightCh == top.getID():
                # print(f"added {addNode.getID()} normally to top, moved {top.getID()} down")
                addNode.set_right(top)
                top = addNode
            
            
                
            else:
                # found nothing.... check later
                addLater.append(addNode)
        else:
            # found parent node, check if left or right child
            if parentNode.get_left_id() == nodeID:
                # boom add to parent node's left
                parentNode.set_left(addNode)
                # print(f"added {nodeID} normally under {parentNode.getID()}")
            elif parentNode.get_right_id() == nodeID:
                # add to parent node's right ID
                parentNode.set_right(addNode)
                # print(f"added {nodeID} normally under {parentNode.getID()}") 

# print([x.getID() for x in addLater])


while len(addLater) > 0:
    # print("array size:", len(addLater))
    
    arraySize = len(addLater)
    i = 0
    while i < len(addLater):
        arraySize = len(addLater)
        # print(f">>>>>> {i} < {arraySize}")
        
    # for node in addLater[:]:
        addNode = addLater[i]
        if top == None:
            top = node
        else:
            nodeID = addNode.getID()
            parentNode = top.getByID(nodeID)
            # parentNode = node.get_up()
            
            if parentNode == None:
                # found no link, check above???????
            
                if leftCh == top.getID():
                    # 
                    # print(f"added {addNode.getID()} laterly to top, moved {top.getID()} down")
                    addNode.set_left(top)
                    top = addNode
                    # addLater.remove(node)
                    del addLater[i]
                    
                elif rightCh == top.getID():
                    # print(f"added {addNode.getID()} laterly to top, moved {top.getID()} down")
                    addNode.set_right(top)
                    top = addNode
                    # addLater.remove(node)
                    del addLater[i]
                
                    
                else:
                    # found nothing.... check later
                    # addLater.append(addNode)
                    i += 1
            else:
                # found parent node, check if left or right child
                if parentNode.get_left_id() == nodeID:
                    # boom add to parent node's left
                    # print(f"added {addNode.getID()} later under {parentNode.getID()}")
                    parentNode.set_left(addNode)
                    # addLater.remove(node)
                    del addLater[i]
                    
                elif parentNode.get_right_id() == nodeID:
                    # add to parent node's right ID
                    # print(f"added {addNode.getID()} later under {parentNode.getID()}")
                    parentNode.set_right(addNode)
                    # addLater.remove(node)
                    del addLater[i]
                    
                    
        # print('finished working on node...', addNode.getID())      
        # print([x.getID() for x in addLater])
# print("DONE")

#### PARSE THROUGH PHRASES LETS GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
phraseOutput = []
for i in range(phraseCount):
    phrase = input()
    phraseOutput.append(top.getLang(phrase))

for line in phraseOutput:
    line.sort()
    print(" ".join(line))
    
    


        
        # if top == None:
        #     top = Node('I', nodeID, character, leftCh, rightCh)
        # else:
        #     # search each left and right for ID
        #     attach = top.getByID(nodeID)
        #     if attach == None:
        #         addLater.append(Node('I', nodeID, character, leftCh, rightCh))
        #     else:
        #         attach = Node('I', nodeID, character, leftCh, rightCh)
            
            
    
        
        
        
        # if top == None:
        #     addLater.append(Node('L', nodeID, lang=lang))
        # else:
        #     attach = top.getByID(nodeID)
        #     if attach == None:
        #         addLater.append(Node('L', nodeID, lang=lang))
        #     else:
        #         attach = Node('L', nodeID, lang=lang)

