import json
from classes.circle import Circle
from classes.figure import Figure
from classes.rectangle import Rectangle
from classes.rhombus import Rhombus
from classes.square import Square
from classes.triangle_ravn import Triangle

def write(data):
    jsonstr = json.dumps(ensure_ascii=False, obj=data, indent=4)
    open('output.json', 'w').write(jsonstr)

def read_from_json():
    return json.load(open('output.json', 'r'))

cicrle1 = Circle(5)
rectangle1 = Rectangle(2, 3)
rhombus1 = Rhombus(3, 4)
square1 = Square(3)
triangle1 = Triangle(3)

objects = [cicrle1, rectangle1, rhombus1, square1, triangle1, ]
data = {
        'figure': [],
}
for obj in objects:
    data['figure'].append(obj.__dict__)

write(data)
data.clear()
objects.clear()
data = read_from_json()
for obj in data['figure']:
    if obj['name'] == "circle1":
        obj = cicrle1(obj['radius'])
    elif obj['name'] == "rectangle1":
        obj = rectangle1(obj['a'], obj['b'])
    elif obj['name'] == "rhombus1":
        obj = rhombus1(obj['a'], obj['h'])
    elif obj['name'] == "square1":
        obj = square1(obj['a'])
    elif obj['name'] == "triangle1":
        obj = triangle1(obj['a'])
    objects.append(obj)

with open(encoding='utf-8', file='output.txt', mode='w') as file:
    for obj in objects:
        output = obj.__repr__() + "\n"
        file.write(output)