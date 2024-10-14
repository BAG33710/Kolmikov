import math
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
        # Рассчет общего количества таблеток 
        total_tablets = self.tablets_inDay * 2 * days
        # Рассчет количества упаковок 
        self.packages_needed = math.ceil(total_tablets / 50)

    def tire(a):
        print("-"*a)

    def research(self,analyse, arg):
        t = analyse.lower()
        resualt = float(t[t.find(arg)+6: t.find(arg) + 10])
        print(f' {arg} - {resualt}')


    def printAnswer(self):
        if(self.tablets_inDay % 2 == 0):
            print(f"Нужно принимать по {self.tablets_inDay / 2} таблетки(-e) 2 раза в день.")
            print(f"Необходимо {self.packages_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения.")
        else:
            evening = math.ceil(self.tablets_inDay / 2)
            morning = math.floor(self.tablets_inDay / 2)
            print(f"Нужно принимать по {morning} утром таблетки(-e) 2 раза в день.")
            print(f"Нужно принимать по {evening} вечером таблетки(-e) 2 раза в день.")
            print(f"Необходимо {self.packages_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения.")
vrach = momo(0, 0, 0)
# Ввод данных от врача
#Анализы
textAnalyse = input("Введите результаты Анализов >>")
#Проверка Анализов
print("-"*50)
vrach.alt_num = vrach.research(textAnalyse,"аст")
vrach.ast_num = vrach.research(textAnalyse,"алт")
#Дозировка
print("-"*50)
doze = int(input("Введите дозировку на кг >>> разрешено пока что 10мг/кг, и 15мг/кг >>"))
#Вес
weight = float(input("Введите вес пациента: >>"))
#Кол-во дней 
days = int(input("Введите количество дней в курсе лечения: >>"))
#Полный расчёт курса
vrach.raschet()
print("-"*50)
vrach.printAnswer()






