# Содержание ДЗ_1
# По каждому заданию делать коммит с указанием задание __ сделано в названии коммита
#
# Задание 1
# С помощью функций print и pprint вывести построчно текст:
#
# Передо мной явилась ты,
# Как мимолетное виденье,
# Как гений чистой красоты.
#
# Задание 2
# Вывести то же самое, но с использованием только одного print сразу все три строки в виде абзаца
#
# Задание 3
# С помощью f-строк вывести текст, который содержал бы действие 4^5 и его результат без предварительного вычисления
#
# Задание 4
# Дописать такой print, чтобы результат каждой итерации выводило в консоль с текстом
# Результат итерации номер __ равен __
# Номер итерации должен быть человеческим, то есть начинаться с 1 в самом сообщении о расчете

# print('Передо мной явилась ты,')
# print('Как мимолетное виденье,')
# print('Как гений чистой красоты.')
#
# print('''
# Передо мной явилась ты,
# Как мимолетное виденье,
# Как гений чистой красоты.
# ''')

# print(f'В одном Мегабайте {4**5} Килобайт')

for number in range(13):
    result = number**(number/(number + 1))
print(number)