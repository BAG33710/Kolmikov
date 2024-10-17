people_limit = 4
people = ""

while (True):
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите посмотреть текущую очередь;")
    print(" - 3, если хотите прекратить работу программы и посмотреть получившуюся очередь.")
    print("-" * 50)

    choice = input()

    if choice == '1':
        if len(people.split(", ")) < people_limit:
            fio = input("Введите ФИО пациента: ").strip()
            if people:
                people += f", {fio}"
            else:
                people = fio
        else:
            print("Очередь наполнена!")
            print(f"Текущая очередь - {people}")
            break
    elif choice == '2':
        if people:
            print(f"Текущая очередь - {people}")
        else:
            print("Очередь пустая!")
    elif choice == '3': 
        if len(people) > 0:
            print(f"Текущая очередь - {people}")
        else:
            print("Очередь пустая!")
        break