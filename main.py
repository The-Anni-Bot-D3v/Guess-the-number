import random
from typing import Text


lvl1 = 1
lvl2 = 2
lvl3 = 3
a = random.randint(1,10)
b = random.randint(1,100)
c = random.randint(1,500)


while True:
    vhod = int(input('Выбери уровень от 1 до 3: '))
    if vhod == 1:
        while True:
            level1 = int(input('Угадай случайное число от 1 до 10: '))
            if level1 > a:
                print('Загаданное число немного меньше!')
            elif level1 < a:
                print('Загаданное число немного больше!')
            elif level1 == a:
                print('Молодец, ты угадал загаданное число!')
                break


    if vhod == 2:
        while True:
            level2 = int(input('Угадай случайное число от 1 до 100: '))
            if level2 > b:
                print('Загаданное число немного меньше!')
            elif level2 < b:
                print('Загаданное число немного больше!')
            elif level2 == b:
                print('Молодец, ты угадал загаданное число!')
                break


    if vhod == 3:
        while True:
            level3 = int(input('Угадай случайное число от 1 до 500: '))
            if level3 > c:
                print('Загаданное число немного меньше!')
            elif level3 < c:
                print('Загаданное число немного больше!')
            elif level3 == c:
                print('Молодец, ты угадал загаданное число!')
                break