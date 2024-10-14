import math
# Ввод данных от врача
doze = int(input("Введите дозировку на кг >>> разрешено пока что 10мг/кг, и 15мг/кг"))
weight = float(input("Введите вес пациента: "))
days = int(input("Введите количество дней в курсе лечения: "))

# Рассчет среднесуточной дозы
if(doze == 10):
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
elif(doze == 15):
    dayDose = (weight * 15) / 2
    # Рассчет из миллиграм в день, в таблетки с округлением на прием в день
    tablets_inDay = round(dayDose / 250, 1)

    # Рассчет общего количества таблеток 
    total_tablets = tablets_inDay * 2 * days

    # Рассчет количества упаковок 
    packages_needed = math.ceil(total_tablets / 50)

    # Вывод результата
    print(f"Нужно принимать по {tablets_inDay} таблетки(-e) 2 раза в день.")
    print(f"Необходимо {packages_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения.")
else:
    print("других дозировок нет, попробуйте ещё раз")
 