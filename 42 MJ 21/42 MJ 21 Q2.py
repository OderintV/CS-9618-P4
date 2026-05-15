global arrayData
arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearSearch(data):
    global arrayData
    for item in arrayData:
        if data == item:
            return True
    return False

data = int(input("Enter a value to search in array: "))
if linearSearch(data):
    print("Value was found.")
else:
    print("Value was not found")

def bubbleSort():
    global arrayData
    for x in range(0,len(arrayData)-1):
        for y in range(0, len(arrayData)-1-x):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

