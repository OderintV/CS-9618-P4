from platform import node


class Node:
    def __init__(self, data):
        self.TheData = data # integer data type
        self.NextNode = None # node data type

    def GetData(self):
        return self.TheData
    def GetNextNode(self):
        return self.NextNode
    def SetNextNode(self, pnode):
        self.NextNode = pnode

class LinkedList:
    def __init__(self, hnode):
        self.HeadNode = None # type node

    def InsertNode(self, dataint):
        pnode = Node(dataint)
        pnode.SetNextNode(self.HeadNode)
        self.HeadNode = pnode

    def Traverse(self):
        ReturnValue = ""
        CurrentNode = self.HeadNode
        while (CurrentNode != None):
            ReturnValue = ReturnValue + str(CurrentNode.GetData()) + " "
        CurrentNode = CurrentNode.GetNextNode()
        return ReturnValue

    def RemoveNode(self, dataint):
        if self.HeadNode == None:
            return False
        elif self.HeadNode.GetData() == dataint
            self.HeadNode = self.HeadNode.GetNextNode()
            return True
        Found = False
        currentNode = self.HeadNode
        while not Found and currentNode!=None:
            if