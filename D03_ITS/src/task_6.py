"""
Пример кода с ошибкой № 6
"""
import sys


print('Программа для визуализации работы индексов\n')
test_string = 'Тестовая строчка'
print(test_string)

is_index_flag = bool(int(input('\nВведи\n - 0, если хочешь прекратить программу;\n - 1, если хочешь задать индекс.\n')))

if is_index_flag:
    index = input('Введи индекс: ')
    print(f'Элемент, стоящий под этим индексом - "{test_string.index(index)}"')
    # print("'Такого индекса нет в этой строке!'")

else:
    sys.exit()
