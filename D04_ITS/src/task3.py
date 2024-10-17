people_limit = 4
people = set()
client = 0

while (client < people_limit):
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите удалить пациента из очереди;")
    print(" - 3, если хотите посмотреть текущую очередь;")
    print(" - 4, если хотите прекратить работу программы и посмотреть получившуюся очередь.")
    print("-" * 50)

    choice = input()

    if choice == '1':
        client += 1
        newpeople = input("Введите ФИО пациента: ").title()
        people.add(newpeople)
    elif choice == '2':
        newpeople = input("Введите ФИО пациента, которого надо удалить из очереди: ").title()
        if newpeople in people:
            client -= 1
            people.remove(newpeople)
        else:
            print("Такого пациента нет в очереди!")
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