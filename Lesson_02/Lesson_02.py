# строки str (string)

number = 78

number_2 = str(number)
# print(number, type(number))
# print(number_2, type(number_2))
# num_del = number / 2
# num_del_2 = number_2 / 2
# print(num_del)
# print(num_del_2)
# num_pro = number * 2
# num_pro_2 = number_2 * 2
# print(num_pro)
# print(num_pro_2)
# num_pro = number + 2
# num_pro_2 = 'Параграф ' + number_2
# print(num_pro)
# print(num_pro_2)
# my_number = 1.26
# # my_number = float(my_number)
# print(f'Число типа int: {int(my_number)}, число типа float: {float(my_number)}')

# Операции

# Возведение в степень

# x = 78**5
# print(f'78 в степени 5 равно {x}')

# целочисленное деление

# print(f'Целочисленное деление 78 на 5 равно {78//5}')
#
# # Остаток от деления
#
# print(f'Остаток от деления 78 на 5 равно {78%5}')

# my_string = '012345678Спокойной, Маша, я - Дубровский!!!'
# print(my_string[9:])  # Спокойной, Маша, я - Дубровский!!!
# print(my_string[4:8])  # 4567
# my_string_to_decode = '51515151Шт551651и51551р477888л78иц1551'
# print(
#     f'''Имя шпиона: {my_string_to_decode[8:10] + my_string_to_decode[16:17] + my_string_to_decode[22:23] + my_string_to_decode[29:30]
#                      + my_string_to_decode[32:34]}'''
#     )  # Имя шпиона: Штирлиц

# Булевы переменные - правда и ложь

# print(78 > 97)
# print(78 + 8 > 20)
# print(56 > 45 and 45 > 36) # Логическое И
# print(56 > 45 & 45 > 36) # Логическое И
# print(89 == 89, 89 != 45)
# print(78 > 45 or 45 > 36) # True # Логическое ИЛИ
# print(78 < 45 or 45 > 36) # True
# print(78 > 45 or 45 < 36) # True
# print(78 < 45 or 45 < 36) # False

# # Списки
#
# # 1
#
# my_list = list()
#
# # 2
#
# my_list_2 = []
#
# # добавление элементов
#
# print(f'''________________________________________________________________________________________________________________________
# Запуск пустых списков\n
# список первый {my_list}
# список второй {my_list_2}
# ________________________________________________________________________________________________________________________''')
#
# my_list.append('моя первая строка в этом списке')
# my_list.append('моя вторая строка в этом списке')
# my_list.append('моя третья строка в этом списке')
# my_list.append('моя четвертая строка в этом списке')
# my_list.append(5)
#
# my_list_2.append('моя первая строка в этом списке')
# my_list_2.append('моя вторая строка в этом списке')
# my_list_2.append('моя третья строка в этом списке')
# my_list_2.append('моя четвертая строка в этом списке')
# my_list_2.append(8)
#
# print(f'''________________________________________________________________________________________________________________________
# Запуск списков с элементами\n
# список первый {my_list}
# # список второй {my_list_2}
# # ________________________________________________________________________________________________________________________''')
#
# # Кортежи или тьюплы
#
# # hello_kitty = (48, 'hello', 78)
# # my_tuple_2 = (58,)
# # print(hello_kitty[0])
#
# # Словари
#
dictionary_1 = dict()
dictionary_2 = {'first_key': 45, 'я передумал': 'Непостоянство'}
print(dictionary_2['first_key'])
# # Добавить новую пару ключ-значение
# print(dictionary_2)
# dictionary_2['third_key'] = 4569
# print(dictionary_2)
#
# # Множества
#
# my_set = set()
# print(my_set)
# my_set.add('Пролог')
# my_set.add('Madaskar')
# my_set.add('Moscow')
# my_set.add('Merlin')
# my_set.add('Mozambik')
# print(my_set)
# my_set.add('Moscow')
# my_set.add('Merlin')
# my_set.add('Mozambik')
# print(len(my_set))

# Условные операторы

# if

# number = 35
#
# if number < 35:
#     print(number)
# else:
#     number = number + 25 # number += 25
# print(number)

# age = int(input())
#
# if age < 18:
#     message = 'Иди домой, товарищ!!!'
# elif age >= 18 and age < 60:
#     message = 'Работа зовет!!!'
# elif age >= 60 and age < 100:
#     message = 'Твой век еще не прошел'
# elif age >= 100 and age < 151:
#     message = 'Рекорд уже близко, а клуб 27 далеко позади'
# else:
#     message = 'Вселенная преветствует тебя, вечный странник!!!'
# print(message)

# for

#for i in range(1, 121, 4):
#    print(f'Число 2 в степени {i} равно {2**i}')

# name = 'Pavel'
#
# list_name = ['Lloyd', 'Ilon', 'Ferdinand', 'Askold', 'Erast', 'Maxim']
#
# for name_in_list in list_name:
#     if name_in_list == name:
#         print(name)
#         break
#     else:
#         continue
# else:
#     print(f'Имени {name} в {list_name} нет')
