people = ["Nikolay","Vanya","Petya"]

a = 0

def add():
    name = input("Введите имя человека")
    people.append(name)
def check():
    for i in range(len(people)):
        print(people[i] + ", ", end='')

while(True):
    print("-" * 50, end='\n')
    a = int(input("Введите действие 1)Добавить человека в очередь 2)Посмотреть очередь 3)Выйти >>>"))
    if(a == 1):
        print("-" * 50)
        add()
    elif(a == 2):
        check()
    elif(a == 3):
        print("Выход")
        break
    else:
        print("Не то число, давай ещё раз")
