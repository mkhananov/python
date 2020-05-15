print("Практическое задание 6."
      "\nТаблица товаров."
      "\nЕсли при занесении товара будет не заполнено хотя бы одно значение, "
      "\nто последний товар не будет занесен и заполнение таблицы закончится")

number = 1
my_dict = []

while True:

    product_name = input(f"Введите название {number} товара: ")
    product_cost = input("Введите его стоимость числом: ")
    product_count = input("Введите его количество числом: ")
    product_unit = input("Введите единицу измерения: ")
    if product_name == "" or product_cost == "" or product_count == "" or product_unit == "":
        print("Так как при заполнении последнего были пустые значения, "
              "товар не занесен и заполнение таблицы закончено")
        break
    new_my_dict = dict(название=product_name, цена=float(product_cost),
                       количество=float(product_count), eд=product_unit)
    new_my_dict_row = [number, new_my_dict]
    my_dict.append(tuple(new_my_dict_row))
    number += 1

print("Таблица товаров:", my_dict)

my_dict_arr = {"название": [], "цена": [], "количество": [], "eд": []}

for i in range(len(my_dict)):
    for name_field in list(set(my_dict_arr)):
        my_dict_arr[name_field].append(my_dict[i][1].get(name_field))

print("Аналитика о товарах:", my_dict_arr)
