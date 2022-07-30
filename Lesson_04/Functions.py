# -*- coding: utf-8 -*-
def fibbonachi_numbers(number: int) -> list:
    fib_list = [1, 1]
    a = 1
    b = 1
    for _ in range(number - 2):
        a, b = b, a + b
        fib_list.append(b)
    return fib_list


# fibbonachi = my_first_func(50)
# print(fibbonachi)

def trancformer_list_to_set(some_list: list) -> set:
    """
    This function convert any list in set
    :param some_list:
    :return: my_set
    """
    my_set = set()
    for element in some_list:
        my_set.add(element)
    return my_set
