class node:
    def __init__(self, datap, nextnodep):
        self.data = datap # integer
        self.nextNode = nextnodep # integer

def outputNodes(LinkedList, currentPointer):
    while currentPointer != -1:
        print(str(LinkedList[currentPointer].data))
        currentPointer = LinkedList[currentPointer].nextNode

def addNode(LinkedList, currentpointer, emptylist):
    data = int(input("Enter data to add:"))
    if emptylist = 0:
        return False
    else:
        newnode = node(data, -1)
        LinkedList[emptylist] = newnode
        
LinkedList = [
    node(1,1), node(5,4), node(6,7), node(7,-1),
    node(2,2), node(0,6), node(0,6), node(0,8),
    node(56, 3), node(0,9), node(0, -1)
]
startPointer = 0
emptyList = 5

outputNodes()
