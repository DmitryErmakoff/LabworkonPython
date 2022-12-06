from figure import Figure
import random

class Square(Figure):
    area_figure = 0
    perimeter_figure = 0

    def __init__(self, a):
        if(a <= 0):
            print("Число должно быть больше нуля, будет сгенерировано случайное число")
            self.a = random.randint(1, 7)
        else:
            self.a = a

    def area_figure(self):
        area_figure = self.a ** 2
        print(area_figure)

    def perimeter_figure(self):
        perimeter_figure = self.a * 4
        print(perimeter_figure)
    
    def property_figure(self):
        print(f'Фигура - квадрат, площадью {self.a ** 2}, периметром {self.a * 4}')

square1 = Square(5)
square1.property_figure()
         