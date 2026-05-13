global DataStored
global NumberItems
DataStored = [] # Array

def Initialise():
    global NumberItems
    while True:
        quantity = int(input("Enter number of data you want to enter: "))
        if quantity >= 1 and quantity <=20:
            break
    for i in range(1, quantity+1):
        data = int(input(f"Enter data for {i} "))
        DataStored.append(data)
    NumberItems = quantity

def BubbleSort(DataStored, NumberItems):
    for i in range(NumberItems):
        for j in range(NumberItems-i-1):
            if DataStored[j] > DataStored[j+1]:
                DataStored[j], DataStored[j+1] = DataStored[j+1], DataStored[j]


def BinarySearch(DataToFind):
    global DataStored
    global NumberItems
    low = 0
    high = NumberItems -1
    while low <= high:
        mid = (low + high) // 2
        if DataStored[mid] == DataToFind:
            return mid
        elif DataStored[mid] < DataToFind:
            low = mid + 1
        else:
            high = mid - 1
    return -1


NumberItems = 0
Initialise()
print("Data in DataStored Array:")
for _ in DataStored:
    print(_)
BubbleSort(DataStored, NumberItems)
print("Data Sorted Array:")
for _ in DataStored:
    print(_)
noToFind = int(input("Enter number to find in array: "))
Found = BinarySearch(noToFind)
print(Found)
