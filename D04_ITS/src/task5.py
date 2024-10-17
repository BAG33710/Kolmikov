people_limit = 4
people = {}

while (len(people) < people_limit):
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите удалить пациента из очереди;")
    print(" - 3, если хотите посмотреть текущую очередь;")
    print(" - 4, если хотите прекратить работу программы и посмотреть получившуюся очередь.")
    print("-" * 50)

    choice = input()

    if choice == '1':
        time,name = input("Введите время и ФИО пациента (через запятую и пробел - '08:00, Иванов А.А.'): ").title().split(sep=", ")
        if name in people:
            print("Такой пациент уже есть в очереди!")
        elif time in people:
            print("Такое Время уже занято!")
        else:
            people[time] = name
    elif choice == '2':
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

