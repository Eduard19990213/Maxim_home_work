# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
in_month_28_days = [2]
in_month_30_days = [4, 6, 9, 11]
in_month_31_days = [1, 3, 5, 7, 8, 10, 12]
while True:
    print('Для выхода введите -13')
    user_input = int(input('Введите, пожалуйста, номер месяца: '))
    if user_input == -13:
        break
    if user_input in in_month_31_days:
        print(f'В {user_input}-ом месяце 31 день')
    elif user_input in in_month_30_days:
        print(f'В {user_input}-ом месяце 30 дней')
    elif user_input in in_month_28_days:
        print(f'Во {user_input}-ом месяце 28 дней')
    else:
        print(f'В {user_input}-ом месяце пока что, к сожалению, ноль дней')

