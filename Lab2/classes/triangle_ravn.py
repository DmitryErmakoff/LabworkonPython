from figure import Figure
import random
import math

class Triangle(Figure):
    area_figure = 0
    perimeter_figure = 0

    def __init__(self, a):
        if(a <= 0):
            print("Длина стороны равностороннего треугольника не может быть нулем или отрицательным числом, будет сгенерировано рандомное число в диапазоне [1,7]")
            self.a = random.randint(1, 7)
        else:
            self.a = a

    def area_figure(self):
        area_figure = (self.a ** 2 * math.sqrt(3)) / 4
        print(area_figure)

    def perimeter_figure(self):
        perimeter_figure = self.a * 3
        print(perimeter_figure)

    def property_figure(self):
          print(f'Фигура - равносторонний треугольник, площадью {(self.a ** 2 * math.sqrt(3)) / 4}, периметром {self.a * 3}')

treg = Triangle(5)
treg.property_figure()

        
