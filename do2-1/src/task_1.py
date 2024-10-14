import math

days = int(input("Введите количество дней в курсе лечения: "))

total = days * 250 
packages_needed = math.ceil(total / (50 * 250)) 


print(f"Необходимо {packages_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения.")
