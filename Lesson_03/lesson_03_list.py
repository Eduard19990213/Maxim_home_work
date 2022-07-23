# Расширение списка другим списком
list_for_extended = [1, 2, 3, 4]
list_to_extended = [5, 6, 7, 8]
extended_list = list_for_extended
extended_list.extend(list_to_extended)
# print(extended_list)
# внедрение элемента под некоторым номером

element_to_insert = 10
extended_list.insert(5, element_to_insert)
# print(extended_list)

# удаление первого элемента, имеющего указанное значение
list_to_destract = ['life, my life ', '45', 45, 'zusammen', 'extended man']
list_to_destract.remove(45)
# print(list_to_destract)

# передает удаленный элемент в переменную

pop_element = list_to_destract.pop(2)
# print(pop_element)
# print(list_to_destract)

# функция index

# my_element = '451'
# if my_element in list_to_destract:
#     index_my_element = list_to_destract.index(my_element)
#     print(f'Element {my_element} has index: {index_my_element}')
# else:
#     print(f'{my_element} not in list')
# Число элементов определенного значения в списке
list_of_my_class = ['Alex', 'Ann', 'Nick', 'Guntter', 'Ferdoves', 'Galptilfart', 'Djafar', 'Alladin', 'Ann', 'Ann']
count_of_Ann = list_of_my_class.count('Ann')
print(count_of_Ann)



