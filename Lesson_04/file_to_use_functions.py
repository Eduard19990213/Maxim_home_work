# -*- coding: utf-8 -*-
from pprint import pprint

from Functions import fibbonachi_numbers, trancformer_list_to_set

example_1 = fibbonachi_numbers(15)
# pprint(example_1)

list_of_names = ['Ann', 'Sergo', 'Nick', 'Sedrick', 'Sam', 'sam', 'Ann',
                 'Ann', 'Sergo', 'Nick', 'Sedrick', 'Sam', 'sam', 5, '5', 5, 50, 55,
                 'Ann', 'Sergo', 'Nick', 'Sedrick', 'Sam', 'sam']
print(trancformer_list_to_set(list_of_names))
