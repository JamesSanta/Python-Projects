class Encapsulation:
    def __init__(self):
        self._protected_var = 20    # Protected variable
        self.__private_var = 30     # Private variable

    def access_vars(self):
        print("Protected var:", self._protected_var)
        print("Private var:", self.__private_var)


obj = Encapsulation()
obj.access_vars()
















    
        
