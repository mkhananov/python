import json
firms_profit = {}
firms_wastage = {}
file_name = "text7.txt"
json_file_name_profit = "firms_profit.json"
json_file_name_wastage = "firms_wastage.json"
with open(file_name) as my_f:
    for line in my_f:
        my_str = line.split()
        firm_name = my_str[0]
        proceeds = int(my_str[2])
        costs = int(my_str[3])
        profit = proceeds - costs
        if profit > 0:
            firms_profit.update({firm_name: profit})
        else:
            firms_wastage.update({firm_name: profit})

firms_profit = [firms_profit, {"average_profit": sum(firms_profit.values()) / len(firms_profit)}]
firms_wastage = [firms_wastage, {"average_wastage": sum(firms_wastage.values()) / len(firms_wastage)}]

with open(json_file_name_profit, "w") as write_f:
    json.dump(firms_profit, write_f)

with open(json_file_name_wastage, "w") as write_f:
    json.dump(firms_wastage, write_f)
