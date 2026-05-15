class NewRecord:
    def __init__(self, key, item1, item2):
        self.Key = key
        self.Item1 = item1
        self.Item2 = item2


def Initiliase():
    for i in range(200):
        HashTable.append(NewRecord(-1,-1,-1))
    for j in range(100):
        Spare.append(NewRecord(-1,-1,-1))

def CalculateHash(keyfield):
    return (int(keyfield)%200)

def InsertIntoHash(record):
    hash = CalculateHash(record.Key)
    if HashTable[hash] == NewRecord(-1,-1,-1):
        HashTable[hash] = record
    else:
        Spare.append(record)
def CreateHashTable():
    with open("HashData.txt",'r') as file:
        for line in file:
            data = line.strip().split(",")
            InsertIntoHash(NewRecord(data[0],data[1],data[2]))
def PrintSpare():
    global Spare
    for item in Spare:
        if item.Key != -1:
            print(item.Key)

HashTable = []
Spare = []

Initiliase()
CreateHashTable()
PrintSpare()
