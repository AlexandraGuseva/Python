#Задача 1 HARD по желанию Напишите программу, 
#которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.

from math import log10

n = int(input('Input a number:   '));
dgtCount = int (log10(n) + 1)
print (f'Count numbers: {dgtCount}')
