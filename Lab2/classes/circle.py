from figure import Figure
import math 
import random

class Circle(Figure):
    area_figure = 0
    perimeter_figure = 0

    def __init__(self, r):
        if(r <= 0):
            print("Радиусом фигуры должно быть положительно число, вместо вашего числа сгенерировалось рандомнон число в диапозоне [1,7]")
            self.r = random.randint(1, 7)
        else:
            self.r = r

    def area_figure(self):
        area_figure = math.pi * self.r ** 2 
        print(area_figure)
    
    def perimeter_figure(self):
        perimeter_figure = 2 * math.pi * self.r
        print(perimeter_figure)
        
    def property_figure(self):
        print(f'Фигура - круг, площадью {math.pi * self.r ** 2}, периметром {2 * math.pi * self.r}')

