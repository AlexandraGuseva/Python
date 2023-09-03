# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

n = int(input('Input count coins:  '))
a = 0
b = 0
for i in range(n):
    side = randint(0, 1)
    print(side, end=' ')
    if side > 0:
        a += 1
    else: 
        b += 1
print()
if a > b:
    print(f'Need to flip {b} coins')
else:
    print(f'Need to flip {a} coins')