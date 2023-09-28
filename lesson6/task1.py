# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import os
os.system('cls')

firstElement = int(input('Input the first element:   '));
differensElements = int(input('Input a differents:   '));
countElements = int(input('Input a count elements:   '));
print('Result massive: \n')
for i in range(countElements):
    print(firstElement + i * differensElements, end=' ')