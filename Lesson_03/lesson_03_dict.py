our_dict = {
    'first': 45,
    'second': 13,
    'third': 19
}
# print(our_dict['third'])
# Замена значения по ключу

our_dict['second'] = '78'
# print(type(our_dict['second']))

# Перебор словаря

# for key in our_dict.keys():
#     print(key)

# for value in our_dict.values():
#     print(type(value))

# for key, value in our_dict.items():
#     print(key, value)

# удадение и добавление одного элемента

del our_dict['first']
print(our_dict)

our_dict['fourth'] = 'New Element'
print(our_dict)

our_dict.popitem()  # удаление последнего элемент
print(our_dict)

users = {
    'Nick': 12533,
    'Maxim': 12347,
    'Ann': 78442,
    'Gerald': 45125,
    'Nickolay': 77911
}
print(users.setdefault('Nick2', 'Has not this user'))
