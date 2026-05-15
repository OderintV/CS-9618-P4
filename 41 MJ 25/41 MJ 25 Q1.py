Queue = [""] * 20 # queue of 20 elements
HeadPointer = -1
TailPointer = -1
NumberItems = 0
print(Queue)
def Enqueue(integer):
    global HeadPointer
    global TailPointer
    global NumberItems
    global Queue
    if NumberItems == 20:
        return False
    elif NumberItems == 0:
        Headpointer, TailPointer = 0,0

    else:
        TailPointer += 1
        if TailPointer == 20:
            TailPointer = 0
        Queue[TailPointer] = integer
    NumberItems += 1
    return True

def Dequeue():
    global HeadPointer
    global TailPointer
    global NumberItems
    global Queue
    if NumberItems == 0:
        return -1
    elif NumberItems == 1:
        HeadPointer = -1
        TailPointer = -1
        NumberItems -= 1
        return Queue[0]
    else:
        NumberItems -= 1
        HeadPointer += 1
        return Queue[HeadPointer]

for i in range(1,26):
    result = Enqueue(i)
    if result:
        print(f"{i} successful")
    else:
        print(f"{i} unsuccessful")

print(Dequeue())
print(Dequeue())

