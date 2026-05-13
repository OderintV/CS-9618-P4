class Tree:
    def __init__(self, treename, growtheight, heightmax, widthmax, evergreen):
        self.__TreeName = treename
        self.__HeightGrowth = growtheight
        self.__MaxHeight = heightmax
        self.__MaxWidth = widthmax
        self.__Evergreen = evergreen
    def GetTreeName(self):
        return self.__TreeName
    def GetHeightGrowth(self):
        return self.__HeightGrowth
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetEvergreen(self):
        return self.__Evergreen

def ReadData():
    TreeObjects = []
    try:
        file = open("Data.txt", "r")
        TreeData = []
        TreeData = file.read().split("\n")
    with open("Trees.txt", "r") as f:
