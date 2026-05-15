class TreasureChest:
    def __init__(self, questionp, answerp, pointsp):
        self._question = questionp # string
        self._answer = answerp # integer
        self._points = pointsp # integer
    def getQuestion(self):
        return self._question
    def checkAnswer(self, answerp):
        if answerp == self._answer:
            return True
        else:
            return False
    def getPoints(self, noofattempts):
        if noofattempts == 1:
            return self._points
        elif noofattempts == 2:
            return self._points//2
        elif noofattempts == 3 or noofattempts == 4:
            return self._points//4
        else:
            return 0
arrayTreasure = []
def Readdata():
    global arrayTreasure
    with (open("TreasureChestData.txt",'r') as file):
        while True:
            q = file.readline()
            if not q:
                break
            a = file.readline()
            p = file.readline()
            obj = TreasureChest(q,a,p)
            arrayTreasure.append(obj)

Readdata()
qno = int(input("Enter question number: "))
while qno<1 or qno>5:
    print("Enter between 1 and 5")
    qno = int(input("Enter question number: "))
print(arrayTreasure[qno-1].question)

attempt = 0
answer = input("Enter your answer: ")
result = arrayTreasure[qno-1].checkAnswer(answer)
attempt += 1
while not result:
    result = arrayTreasure[qno - 1].checkAnswer(answer)
    attempt += 1
print(arrayTreasure[qno-1].getPoints(attempt))


