import random # Подключение модуля рандом
import statistics # Подключение модуля для вычисления медианы 

rand_list=[] # Создание списка
n=100
for i in range(n): # Задаем цикл с диапозоном от 0 до 100
    rand_list.append(random.randint(3,9)) # Добавляем в конец списка числа, которые располагаются в диапозоне от 3 до 9 (включая эти значения)
print(rand_list)

total = 0
for i in range(0,100): # Цикл, при помощи которого идет счет суммы чисел в списке
    total += i
print("Сумма чисел списка", total)

def median_f(rand_list): # Функция, необходимая для нахождения медианы 
    sortedLst = sorted(rand_list) # Cортировка списка 
    lstLen = len(rand_list) # Считаем длину строки 
    index = (lstLen - 1) // 2 # Находим элемент располагающийся в середине списка, если же кол-во их четное, то найденный суммируется со следующим и делится на два
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

print(median_f(rand_list)) # Вывод медианы, нейденной через созданную функцию 
print(statistics.median(rand_list)) # Вывод медианы через готовую функцию 


