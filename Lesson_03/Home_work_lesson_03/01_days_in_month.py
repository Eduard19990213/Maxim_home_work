# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = int(input('Введите, пожалуйста, номер месяца: '))
if user_input == 1 or user_input == 3 or user_input == 5 or user_input == 7 or user_input == 8 or user_input == 10 or user_input == 12:
    print(f'В {user_input}-ом месяце 31 день')
elif user_input == 4 or user_input == 6 or user_input == 9 or user_input == 11:
    print(f'В {user_input}-ом месяце 30 дней')
elif user_input > 12 or user_input == 0 or user_input <= 0:
    print(f'В {user_input}-ом месяце пока что, к сожалению, ноль дней')
else:
    print(f'Во {user_input}-ом месяце 28 дней')
print('Для выхода введите -13')
