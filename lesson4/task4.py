from collections import Counter
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)
print([el for el in my_list if Counter(my_list)[el] == 1])
