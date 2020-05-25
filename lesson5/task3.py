my_dict = {}
file_name = "text3.txt"
salary = 20000.0
with open(file_name) as my_f:
    for line in my_f:
        my_str = line.split(" ")
        my_dict.update({my_str[0]: float(my_str[1])})

print(f"Средняя величина дохода сотрудников {sum(my_dict.values()) / len(my_dict)} рублей.")
print(f"Кто из сотрудников имеет оклад менее {salary} рублей:")
for el in my_dict:
    if my_dict.get(el) < salary:
        print(el)
