
class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    

    #instance method: self 
    def getAge(self):
        return self.age
    
    def setAge(self, newAge):
        self.age = newAge
    

    #it will be returned when print(object)
    def __str__(self):
        return f"{self.name} {self.age} {self.sex}"
    
    def voice(self):
        return "Animal makes a sound"
    

