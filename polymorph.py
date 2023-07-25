# Python: 3.11.4
# Coder: James Santa

#Parent class
class Mammal:

    species = "Unknown"
    num_legs = 0
    has_hair = False
    diet = "Unknown"        

#Child class
class WingedAnimal(Mammal):

    wing_span = 0
    can_swim = False

#Child class
class Bat(WingedAnimal):
    
    is_nocturnal = False
    echolocation = False

# create an object of Mammal class
human = Mammal()
human.species = "Human"
human.num_legs = 2
human.has_hair = True
human.diet = "Carnivore"


# create an object of WingedAnimal class
eagle = WingedAnimal()
eagle.species = "Eagle"
eagle.num_legs = 2
eagle.diet = "Carnivore"
eagle.wing_span = 180
eagle.can_swim = True

# create an object of Bat class
brown_bat = Bat()
brown_bat.species = "Brown Bat"
brown_bat.num_legs = 2
brown_bat.has_hair = True
brown_bat.diet = "Insectivore"
brown_bat.wing_span = 25
brown_bat.can_swim = True
brown_bat.is_nocturnal = True
brown_bat.echolocation = True

#Accessing the attributes
print(human.diet)
print(eagle.can_swim)
print(brown_bat.echolocation)

    
