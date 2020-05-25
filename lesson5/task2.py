count_words = ""
count_strings = 0
file_name = "text2.txt"
with open(file_name) as my_f:
    for line in my_f:
        count_words += str(len(line.split(" "))) + ", "
        count_strings += 1

print(f"В файле {file_name} {count_strings} строк(и) с количеством слов в каждой {count_words[:-2]} соответственно.")
