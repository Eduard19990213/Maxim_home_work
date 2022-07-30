# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные



#envelop_x, envelop_y = 10, 7
#paper_x, paper_y = 10, 1
#paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
#paper_x, paper_y = 9, 8
# if envelop_x == paper_x and envelop_y == paper_y or envelop_x == paper_y and envelop_y == paper_x:
#     print('Да, лист входит в конверт впритирку')
# elif envelop_x > paper_x and envelop_y > paper_y or envelop_x > paper_y and envelop_y > paper_x:
#     print('Да, лист помещается в конверт')
# elif envelop_x >= paper_x and envelop_y >= paper_y or envelop_x >= paper_y and envelop_y >= paper_x:
#     print('Да, лист помещается в конверт')
# elif envelop_x < paper_x and envelop_x < paper_y:
#     print('Нет, лист слишком широкий')
# elif envelop_y < paper_x and envelop_y < paper_y:
#     print('Нет, лист слишком длинный')
# else:
#     print('Нет, лист не вмещается в конверт')


# (просто раскоментировать нужную строку и проверить свой код)


# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 10, 9, 8
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
if (hole_x >= brick_z and hole_y >= brick_y) or (hole_x >= brick_y and hole_y >= brick_z) or (hole_x >= brick_z and hole_y >= brick_x) or (hole_x >= brick_x and hole_y >= brick_z):
    print('Да, кирпичик проходит')
else:
    print('Нет, приходите в следующий раз')
#это все можно было сделать в несколько строк, однако содержание было бы идентичным, а я не знаю, как писать выгоднее
