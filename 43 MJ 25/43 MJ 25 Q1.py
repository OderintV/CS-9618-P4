from Tools.scripts.generate_opcode_h import header

global Queue
global HeadPointer
global TailPointer

Queue = [-1]*50
HeadPointer = -1
TailPointer = -1

def Enqueue(intdata):
    global Queue
    global TailPointer
    global HeadPointer

    if TailPointer == 49:
        return False
    if TailPointer == -1 and HeadPointer == -1:
        TailPointer, HeadPointer = 0,0
    else:
        Queue[TailPointer] = intdata
        TailPointer += 1


def Dequeue():
    global Queue
    global TailPointer
    global HeadPointer

    if TailPointer == -1 and HeadPointer == -1:
        return -1
    HeadPointer += 1
    return Queue[HeadPointer-1]

def CreateQueue():
    try:
        file = open("QueueData.txt")
        for line in file:
            result = Enqueue(int(line))
            if not result:
                print("Queue full.")
                break
        file.close()
    except:
        print("Cannot open or read file")

CreateQueue()