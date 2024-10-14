import math
# Ввод данных от врача
doze = int(input("Введите дозировку на кг >>> разрешено пока что 10мг/кг, и 15мг/кг"))
weight = float(input("Введите вес пациента: "))
days = int(input("Введите количество дней в курсе лечения: "))

class momo:
    tablets_inDay = 0
    packages_needed = 0

    def __init__(self ,doze1,weight1,days1):
        self.doze = doze1
        self.weight = weight1
        self.days = days1

    def raschet(self):
        # Рассчет среднесуточной дозы
        if(doze == 10 or doze == 15):
            dayDose = (weight * doze)
        else:   
            print("других дозировок нет, попробуйте ещё раз")
        # Рассчет из миллиграм в день, в таблетки с округлением на прием в день
        self.tablets_inDay = round(dayDose / 250, 1)
        print(self.tablets_inDay)
        # Рассчет общего количества таблеток 
        total_tablets = self.tablets_inDay * 2 * days
        print(total_tablets)
        # Рассчет количества упаковок 
        self.packages_needed = math.ceil(total_tablets / 50)


    def printAnswer(self):
        if(self.tablets_inDay % 2 == 0):
            print(f"Нужно принимать по {self.tablets_inDay / 2} таблетки(-e) 2 раза в день.")
            print(f"Необходимо {self.packages_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения.")
        else:
            evening = math.ceil(self.tablets_inDay / 2)
            morning = math.floor(self.tablets_inDay / 2)
            print(f"fНужно принимать по {morning} утром таблетки(-e) 2 раза в день.")
            print(f"Нужно принимать по {evening} вечером таблетки(-e) 2 раза в день.")
            print(f"Необходимо {self.packages_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения.")



vrach = momo(doze, weight, days)
vrach.raschet()
vrach.printAnswer()