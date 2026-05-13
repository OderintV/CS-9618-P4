class Node:
    def __init__(self, nodedata):
        self.__NodeData = nodedata
        self.__LeftNode = None
        self.__RightNode = None
    def GetLeft(self):
        return self.__LeftNode
    def GetRight(self):
        return self.__RightNode
    def GetData(self):
        return self.__NodeData
    def SetLeft(self, ObjNode):
        self.__LeftNode = ObjNode
    def SetRight(self, ObjNode):
        self.__RightNode = ObjNode

class Tree:
    def __init__(self, fnode):
        self.__FirstNode = fnode
    def GetRootNode:
        return self.__FirstNode
    def Insert(self, pnode):
        current = self.__FirstNode
        while True:
            if pnode.GetData() < current.GetData():
                if current.GetLeft() == None:
                    current.SetLeft(pnode)
                    break
                else:
                    current = current.GetLeft()
            if pnode.GetData() > current.GetData():
                if current.GetRight() == None:
                    current.SetRight(pnode)
                    break
                else:
                    current = current.GetRight()

def OutputInOrder(RootNode):
    if RootNode.GetLeft() != None:
        OutputInOrder(RootNode.GetLeft())
    print(RootNode.GetData())
    if RootNode.GetRight() != None:
        OutputInOrder(RootNode.GetRight()

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)