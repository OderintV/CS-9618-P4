class Animal:
    def __init__(self, namep, soundp, sizep, intelligencep):
        self.Name = namep # string
        self.Sound = soundp # string
        self.Size = sizep # integer
        self.Intelligence = intelligencep # string

    def Description(self):
        desc = "The animal's name is", self.Name, ", it makes a", self.Sound,", its size is", self.Size,"and its intelligence level is", self.Intelligence
        return desc

class Parrot(Animal):
    def __init__(self, wingspanp, nowords):
        self.WingSpan = wingspanp
        self.NumberWords = nowords
    def ChangeNumberWords(self, number):
        self.NumberWords += number
    def Description(self):
        desc = "The animal's name is", self.Name, ", it makes a", self.Sound,", its size is", self.Size,"and its intelligence level is", self.Intelligence, ". It has a wingspan of ", self.WingSpan, "cm and can say", self.NumberWords, "words."
        return desc

class Wolf(Animal):
    def __init__(self, name, sound, size, intelligence, territory, tsize):
        super().__init__(name, sound, size, intelligence, territory)
        self.TerritorySize = tsize
    def SetTerritorySize(self, number):
        self.TerritorySize += number
        