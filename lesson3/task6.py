print("Практическое задание 6")
my_word = "word"
my_text = "first word second word and etc"


def int_func(my_str):
    return my_str.capitalize()


print(int_func(my_word))
print(" ".join(list(map(int_func, my_text.split()))))
