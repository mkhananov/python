from itertools import count
from itertools import cycle

for el in count(3):
    if el >= 10:
        print(el)
        break
    else:
        print(el, end=" ")

my_list = ["a", "b", "c"]
count = 0
for word in cycle(my_list):
    if count > 10:
        break
    print(word, end="")
    count += 1
