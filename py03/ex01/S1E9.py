from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Character(ABC):
    """  Character class takes a first_name as first parameter,is_alive as second non mandatory parameter set to True by default and can change the
health state of the character with a method that passes is_alive from True to False."""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Character class. first name and is alive is initailised """
        self.first_name = first_name
        self.is_alive = is_alive
        print("character class init")
    @abstractmethod
    def die(self):
        self.is_alive = False
        
   
class Stark(Character):
    """ Class Stark inherits from the Character class"""
    def die(self):
        self.is_alive = False

