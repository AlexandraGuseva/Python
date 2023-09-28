# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import os

os.system('cls')
n = int(input('Please input lenght the firast set: '))
m = int(input('Please input lenght the second set: '))
arr1 = set(map(int, input('Input the first set (separated by a space) :').split()[:n]))
arr2 = set(map(int, input('Input the second set (separated by a space) :').split()[:m]))
set = sorted(arr1.intersection(arr2))
print(f"Result set: {set}")