from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, sex, color):
        super().__init__(name, age, sex)
        self.color = color
    #override
    def voice(self):
        print("bark bark")
    
    def getColor(self):
        return self.color
    
    def setColor(self, newColor):
        self.color = newColor


