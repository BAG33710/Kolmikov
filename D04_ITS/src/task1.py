people_limit = 4
client = 0
people = ""

while (client < people_limit):
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите посмотреть текущую очередь.")
    print("-" * 50)

    choice = input()

    if choice == '1':
        newpeople = input("Введите ФИО пациента: ").title()
        if people:
            people += f", {newpeople}"
            client += 1
        else:
            client += 1
            people = newpeople
    elif choice == '2':
        if people:
            print(f"Текущая очередь - {people}")
        else:
            print("Очередь пустая!")
