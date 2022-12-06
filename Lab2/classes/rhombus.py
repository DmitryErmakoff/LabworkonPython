from figure import Figure
import random

class Rhombus(Figure):
    area_figure = 0
    perimeter_figure = 0

    def __init__(self, a, h):
        if(a <= 0 or h <= 0):
            print("Параметры ромба должны быть положительные числа, вместо ваших чисел сгенерировались рандомные числа в диапозоне [1,7]")
            self.a = random.randint(1, 7)
            self.h = random.randint(1, 7)
        else:
            self.a = a
            self.h = h

    def area_figure(self):
        area_figure = self.a * self.h
        print(area_figure)
    
    def perimeter_figure(self):
        perimeter_figure = self.a * 4
        print(perimeter_figure)
        
    def property_figure(self):
        print(f'Фигура - ромб, площадью {self.a * self.h}, периметром {self.a * 4}')


    