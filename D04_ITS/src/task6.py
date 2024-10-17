people_limit = 4
people = {}

while True:
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите удалить пациента из очереди;")
    print(" - 3, если хотите посмотреть текущую очередь;")
    print(" - 4, если хотите прекратить работу программы и посмотреть получившуюся очередь.")
    print("-" * 50)

    choice = input()

    if choice == '1':
        if choice == '1':
            time,name = input("Введите время и ФИО пациента (через запятую и пробел - '08:00, Иванов А.А.'): ").title().split(sep=", ")
        if name in people:
            print("Такой пациент уже есть в очереди!")
        elif time in people:
            print("Такое Время уже занято!")
        else:
            people[time] = name
    elif choice == '2':
        print("-" * 50)
        print("Введите:")
        print(" - 1, если хотите удалить пациента по ФИО;")
        print(" - 2, если хотите удалить пациента по его времени в очереди.")
        print("-" * 50)
        sub_choice = input()

        if sub_choice == '1':
            surname = input("Введите ФИО пациента: ").title()
            keys = []
            for time,name in people.items():
                if surname in name:
                    keys.append(time)
            if not keys:
                print("Такого пациента нет в очереди!")
            else:
                del people[keys[0]]            
        elif sub_choice == '2':
            data = input("Введите Время очереди человека: ")
            if data in people:
                del people[data]
            else:
                print("Такое время в очереди не занято!")
    elif choice == '3':
        if people:
            print(f"Текущая очередь - {people}")
        else:
            print("Очередь пустая!")
    elif choice == '4':
        if people:
            print(f"Текущая очередь - {people}")
        else:
            print("Очередь пустая!")
        break

