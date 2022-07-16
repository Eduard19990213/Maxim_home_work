#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что) спасибо
#my_family = []


# список списков приблизителного роста членов вашей семьи
#my_family_height = []

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
# Зачет!

my_family = []
my_family_height = []
my_family.append('Мамы')
my_family.append('Папы')
my_family.append('Сестры')
my_family.append('Меня')
my_family_height.append(170)
my_family_height.append(185)
my_family_height.append(140)
my_family_height.append(175)
print('Рост', my_family[1], '-', my_family_height[1])
print(f'Общий рост моей Семьи - {sum(my_family_height)}')