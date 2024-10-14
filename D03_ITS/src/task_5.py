"""
Пример кода с ошибкой № 5
"""
from random import randint  # И опять повод загуглить незнакомый модуль
import math


input_number = int(input('Введите целое число от -10 до 10: '))

random_number = randint(-10, 10)
print(f'Случайное число = {random_number}')

difference_numbers = input_number - random_number
print(f'{input_number} - ({random_number}) = {difference_numbers}')

if(difference_numbers >= 0):
    sqlt_number = round(math.sqrt(difference_numbers), 2)
    print(f'Корень из {difference_numbers} = {sqlt_number}')
else:
    print("из отрицательного числа нельзя вычислить корень")

