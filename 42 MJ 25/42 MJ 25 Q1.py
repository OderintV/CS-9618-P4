global Stack
global TopOfStack

Stack =["-1"]*20
TopOfStack = -1

def Push(data):
    global Stack
    global TopOfStack
    if TopOfStack == 19:
        return -1
    else:
        TopOfStack += 1
        Stack[TopOfStack] = data
        return 1

def Pop():
    global Stack
    global TopOfStack
    if TopOfStack == -1:
        return -1
    TopOfStack -= 1
    return (Stack[TopOfStack+1])

def ReadData(fname):
    try:
        file = open(fname)
        for line in file:
            result = Push(line.strip())
            if result == -1:
                print("Stack full")
        file.close()

    except IOError or FileNotFoundError:
        print("File not found or could not be accessed")

def Calculate():
    global Stack
    global TopOfStack
    total = int(Stack[0])
    for i in range(1,TopOfStack,2):
        operation = str(Stack[i])
        data = int(Stack[i+1])
        if operation == "+":
            total += data
        elif operation == "-":
            total -= data
        elif operation == "*":
            total = total * data
        elif operation == "/":
            total = total / data
        elif operation == "^":
            total = total**data
        else:
            print("invalid operator found")
    return total

fname = input("Enter filename to read data: ")
ReadData(fname)
print(Calculate())


