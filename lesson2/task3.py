#Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.
n = int(input('Input a restriction number:   '))
m = 1
while m <= n:
    print(m, end=' ')
    m = m * 2