from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X,Z,res,Sum,Average,random_sum')

big_number = 888888 

print("big_number = ")
print(big_number)

# Сумма арифмитической прогрессии 
Sum[X] = ((1 + X) * X) / 2
print("Sum 1..big_nubmer: ")
print(Sum[big_number] == X)

# Среднее арифметической  прогрессии 
Average[X] = (X + 1) / 2
print("Average 1..big_number: ")
print(Average[big_number] == X)

# Сумма рандомных 100 случайных чисел от 1 до "big_number"
rand_numbers = [random.choice(range(big_number)) for i in range(100)]
(res["random_sum"] == sum_(Z, for_each=Z)) <= Z.in_(rand_numbers)
print("Random sum: ")
print(res["random_sum"] == X)

# Медиана
print("Median: ")
print(rand_numbers[50])
