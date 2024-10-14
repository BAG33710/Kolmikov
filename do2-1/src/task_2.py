import math

# Ввод данных от врача
weight = float(input("Введите вес пациента: "))
days = int(input("Введите количество дней в курсе лечения: "))

# Рассчет среднесуточной дозы
dayDose = (weight * 10) / 2

# Рассчет из миллиграм в день, в таблетки с округлением на прием в день
tablets_inDay = round(dayDose / 250, 1)

# Рассчет общего количества таблеток 
total_tablets = tablets_inDay * 2 * days

# Рассчет количества упаковок 
packages_needed = math.ceil(total_tablets / 50)

# Вывод результата
print(f"Нужно принимать по {tablets_inDay} таблетки(-e) 2 раза в день.")
print(f"Необходимо {packages_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения.") 
