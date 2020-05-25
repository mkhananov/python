from re import findall
my_dict = {}
file_name = "text6.txt"
with open(file_name) as my_f:
    for line in my_f:
        my_str = line.split(":")
        my_dict.update({my_str[0]: sum(list(map(int, findall('\d+', my_str[1]))))})

print(my_dict)
