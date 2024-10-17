people_limit = 4
people = []

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
            print("-" * 50)
            print("Введите:")
            print(" - 1, если хотите добавить пациента в конец очереди;")
            print(" - 2, если хотите добавить пациента в начало или середину очереди.")
            print("-" * 50)
            sub_choice = input()

            fio = input("Введите ФИО пациента: ")

            if fio in people:
                print("Такой пациент уже есть в очереди!")
            else:
                if sub_choice == '1':
                    people.append(fio)
                elif sub_choice == '2':
                    pos = int(input("Введите на какое место очереди хотите вставить пациента: ")) - 1
                    people.insert(pos, fio)
        else:
            print("Очередь наполнена!")
            print(f"Текущая очередь - {people}")
            break
    elif choice == '2':
        print("-" * 50)
        print("Введите:")
        print(" - 1, если хотите удалить пациента по ФИО;")
        print(" - 2, если хотите удалить пациента по его номеру в очереди.")
        print("-" * 50)
        sub_choice = input()

        if sub_choice == '1':
            fio = input("Введите ФИО пациента: ")
            if fio in people:
                people.remove(fio)
            else:
                print("Такого пациента нет в очереди!")
        elif sub_choice == '2':
            index = int(input("Введите порядковый номер человека в очереди: ")) - 1
            if 0 <= index < len(people):
                people.pop(index)
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