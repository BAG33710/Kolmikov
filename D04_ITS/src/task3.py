people_limit = 4
people = set()

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
        if len(people) < people_limit:
            fio = input("Введите ФИО пациента: ").strip()
            people.add(fio)
        else:
            print("Очередь наполнена!")
            print(f"Текущая очередь - {people}")
            break
    elif choice == '2':
        fio = input("Введите ФИО пациента, которого надо удалить из очереди: ")
        if fio in people:
            people.remove(fio)
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