file_name = "text1.txt"
my_list = [input("Введите первую строку которая будет записана в файл: ") + "\n"]
while True:
    my_str = input("Введите следующую строку: ")
    if my_str == "":
        break
    my_list.append(my_str + "\n")

with open(file_name, "w") as f_obj:
    f_obj.writelines(my_list)

print(f"Строки записаны в {file_name}")
