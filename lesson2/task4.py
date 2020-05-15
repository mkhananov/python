print("Практическое задание 4. "
      "\nНумерация слов текста с обрезкой слов до 10 символов.")

my_string = input("Введите предложение: ")

for ind, el in enumerate(my_string.split()):
    print(ind + 1, el[:10])
