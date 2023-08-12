# Python version 3.11.4
#
#Coder: James Santa

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    @abstractmethod
    def make_noise(self):
        pass

    def introduce(self):
        print("I am a {}, my name is {}.".format(self.animal_type, self.name))

class Mouse(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "mouse")
        self.name = name

    def make_noise(self):
        return "Golly!"

class Duck(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "duck")
        self.name = name

    def make_noise(self):
        return "Aw,phooey!"

# Creating objects
mouse = Mouse("Mickey")
duck = Duck("Donald")

# Using methods from parent and child classes
mouse.introduce()
print(mouse.make_noise())

duck.introduce()
print(duck.make_noise())


