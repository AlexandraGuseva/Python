# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import os
import random
os.system('cls')

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# list_2 = []
list1 = [random.randint(-20, 20) for i in range(10)]
list2 = []
max = 10
min = 6
for i in range(len(list1)):
    if list1[i] >= min and list1[i] <= max:
        list2.append(i)
print(f'Your list:\n{list1}\nmax:  {max}\nmin:  {min}\n')
print(f'Result index list:\n{list2}\n')