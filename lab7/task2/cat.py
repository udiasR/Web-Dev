from animal import Animal

class Cat(Animal):
    def __init__(self, name, age, sex, color):
        super().__init__(name, age, sex)
        self.color = color

    def getColor(self):
        return self.color
    
    def setColor(self, newColor):
        self.color = newColor

    #@override. 
    def voice(self):
        print(super().voice())
        print("meow, meow")
