
def ReadData():
    data = []
    filename = input("Enter filename: ")
    with open(filename,'r') as file:
        for line in file:
            data.append(line)
    return data

def SplitData(DataArray):
    red, green, blue, orange, yellow, pink = [], [], [], [], [], []
    for item in DataArray:
        number, color = item.strip().split(",")
        if color == "red":
            red.append(number)
        elif color == "green":
            green.append(number)
        elif color == "blue":
            blue.append(number)
        elif color == "orange":
            orange.append(number)
        elif color == "yellow":
            yellow.append(number)
        else:
            pink.append(number)
        StoreData(red, "Red.txt")
        StoreData(green, "Green.txt")
        StoreData(blue, "Blue.txt")
        StoreData(orange, "Orange.txt")
        StoreData(yellow, "Yellow.txt")
        StoreData(pink, "Pink.txt")

def StoreData(DataToStore, Fname):
    with open(Fname, 'a') as file:
        for item in DataToStore:
            file.write(item)

datareturned = ReadData()
SplitData(datareturned)

