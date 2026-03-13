from animal import Animal
from cat import Cat
from dog import Dog


def main():
    default = Animal("asdf", 23, "male")
    kowka = Cat("ketttis", 23, "female", "black")
    aktos = Dog("aktos", 45, "female", "white")

    animals = []
    animals.append(default)
    animals.append(kowka)
    animals.append(aktos)

    for x in range(len(animals)):
        print(animals[x])

    
    print(kowka.voice())
    print(default.voice())
    print(aktos.voice())




if __name__ == "__main__":
    main()



#class method must include SELF