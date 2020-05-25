file_in_name = "text4in.txt"
file_out_name = "text4out.txt"
dict_en_ru = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open(file_in_name) as file_in:
    text = file_in.read()

for el in dict_en_ru:
    text = text.replace(el, dict_en_ru.get(el))

with open(file_out_name, "w") as file_out:
    file_out.write(text)
