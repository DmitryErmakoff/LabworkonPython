from figure import Figure 
import random 

class Rectangle(Figure):
    area_figure = 0
    perimeter_figure = 0

    def __init__(self, a, b):
        if(a <= 0 or b <= 0):   
            print("Числа должны быть больше нуля, будут сгенерированы случайные числа")
            self.a = random.randint(1, 7)
            self.b = random.randint(1, 7)
        else:
            self.a = a
            self.b = b

    def area_figure(self):
        area_figure = self.a * self.b
        print(area_figure)
    
    def perimeter_figure(self):
        perimeter_figure = (self.a + self.b) * 2
        print(perimeter_figure)
    
    def property_figure(self):
        print(f'Фигура - прямоугольник, площадью {self.a * self.b}, периметром {(self.a + self.b) * 2}')


        