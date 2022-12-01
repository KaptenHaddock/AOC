# Path: day1/day1.py
from collections import OrderedDict
import names
elfs_supplies = [({'items': [], 'sum': 0, 'name': names.get_first_name()})] 
elf_no = 0
with open('input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            elf_no +=1
            elfs_supplies.append({'items': [], 'sum': 0, 'name': names.get_first_name()})
            continue
        
        item_calories = int(line)
        elfs_supplies[elf_no]['items'].append(item_calories)
        elfs_supplies[elf_no]['sum'] += item_calories

# Elf with the most calories

sorted_by_total_sum = sorted(elfs_supplies, key=lambda x: x['sum'], reverse=True)
highest_calory_elf = sorted_by_total_sum[0]
top_three = sorted_by_total_sum[:3]
sum_top_three = sum([x['sum'] for x in top_three])
print(
"""
Elf with the most calories: {}
with {} calories.

Sum of the top three elves: {}
""".format(
            highest_calory_elf['name'], 
            highest_calory_elf['sum'], 
            sum_top_three))
