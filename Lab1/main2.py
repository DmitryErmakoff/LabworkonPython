import random
import statistics

rand_list=[]
n=100
for i in range(n):
    rand_list.append(random.randint(3,9))
print(rand_list)

total = 0
for i in range(0,100):
    total += i
print("Сумма числе этого массив", total)

def median_f(rand_list):
    sortedLst = sorted(rand_list) # Cортировка списка
    lstLen = len(rand_list) # Считаем длину строки 
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

print(median_f(rand_list))
print(statistics.median(rand_list))


