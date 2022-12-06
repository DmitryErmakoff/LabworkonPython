from abc import ABC
from abc import abstractclassmethod

class Figure(ABC):

    ## @abstractclassmethod 
    def __init__(self):
            super().__init__()

    @abstractclassmethod
    def area_figure(self):
        pass

    @abstractclassmethod
    def perimeter_figure(self):
        pass

    @abstractclassmethod
    def property_figure(self):
        pass
    


