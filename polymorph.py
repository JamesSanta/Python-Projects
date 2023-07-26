# Python: 3.11.4
# Coder: James Santa

#Parent class
class Mammal:

    species = "Unknown"
    num_legs = 0
    has_hair = False
    diet = "Unknown"
    
    def mammalSpecifics(self):
        return ("This is a {}, it has {} legs, it is: {} that it has hair, and its diet is {}.".format(self.species,self.num_legs,self.has_hair,self.diet))
              
#Child class
class WingedAnimal(Mammal):
    
    wing_span = 0
    can_swim = False
    
    def mammalSpecifics(self):
        return ("This is a {}, it has {} legs, it is: {} that it has hair, its diet is {}, it has a wing span of {} inches, and it is: {} that it can swim.".format(self.species,self.num_legs,self.has_hair,self.diet,self.wing_span,self.can_swim))

#Child class
class Bat(WingedAnimal):

    is_nocturnal = False
    echolocation = False
    
    def mammalSpecifics(self):
        return ("This is a {}, it has {} legs, it is: {} that it has hair, its diet is {}, it has a wing span of {} inches, it is : {} that it can swim, it is: {} that it is nocturnal, and it is: {} that it uses echolocation.".format(self.species,self.num_legs,self.has_hair,self.diet,self.wing_span,self.can_swim,self.is_nocturnal,self.echolocation))

        
       

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
print(human.mammalSpecifics())
print(eagle.mammalSpecifics())
print(brown_bat.mammalSpecifics())

    
