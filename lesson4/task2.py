import random
my_list = [random.randint(0, 100) for el in range(1, 14)]
print(my_list)
print([my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]])
