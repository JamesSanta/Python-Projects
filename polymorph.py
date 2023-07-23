# Python: 3.11.4
# Coder: James Santa

#Parent class
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

    def move(self):
        print("Mammals move on land.")

#Child class
class WingedAnimal(Mammal):
    def winged_animal_info(self):
        print("Winged animals can flap.")

# Overrides the move method to provide an implementation of Wingedanimal class
    def move(self):
        print("Winged animals can fly.")
        
#Child class
class Bat(WingedAnimal):
    def bat_info(self):
        print("Bats are nocturnal.")

# Move method from WingedAnimal class will be used
    def move(self):
        print("Bats can move both on land and fly in the air.")

# create an object of Bat class
b1 = Bat()

#Invokes methods inside each class
b1.mammal_info() #Inherited from Mammal class
b1.winged_animal_info() #Defined in WingedAnimal
b1.bat_info() #Defined in bat
b1.move() #Inherited from WingedAnimal
    
