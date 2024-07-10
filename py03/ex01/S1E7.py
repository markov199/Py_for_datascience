from S1E9 import Character

class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        self.is_alive = False

class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        self.is_alive = False
#your code here
# decorator
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        obj = Lannister(first_name)
        obj.is_alive = is_alive
        return obj


"""ref 
https://stackoverflow.com/questions/61509875/create-chain-methods-for-class-in-python
https://diveintopython.org/learn/classes/object-instantiation
https://diveintopython.org/learn/classes/abstract-class
https://medium.com/quick-code/support-your-class-users-by-providing-an-alternate-way-of-creating-class-instances-using-class-e2da42241913

"""