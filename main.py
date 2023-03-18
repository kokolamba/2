import random



class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)

    def feed(self):
        self.hunger -= 2
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10
        print(f"{self.name} щасливо їсть!")

    def pet(self):
        self.happiness += 2
        if self.happiness > 10:
            self.happiness = 10
        print(f"{self.name} радісно вирушає хвостом!")

    def mood(self):
        if self.hunger >= 7:
            print(f"{self.name} голодний.")
        elif self.hunger >= 4:
            print(f"{self.name} трохи голодний.")
        else:
            print(f"{self.name} не голодний.")

        if self.happiness >= 7:
            print(f"{self.name} щасливий.")
        elif self.happiness >= 4:
            print(f"{self.name} трохи засмучений.")
        else:
            print(f"{self.name} засмучений.")


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Кіт"

    def meow(self):
        print(f"{self.name} м'явкне.")


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Собака"

    def bark(self):
        print(f"{self.name} загавкає.")


my_cat = Cat("Том")
my_cat.meow()
my_cat.mood()
my_cat.feed()
my_cat.mood()
my_cat.pet()
my_cat.mood()
