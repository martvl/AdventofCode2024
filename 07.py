from read_input import read_day_07
from operator import add, mul

data = read_day_07()

# Part 1

def check_options(target_num, running_total, nums_to_check, operators):
    if not nums_to_check:
        if running_total == target_num:  
            return target_num
        else: 
            return 0
    
    num_to_use = nums_to_check[0]
    
    for o in operators:
        new_total = o(running_total, num_to_use)
        if new_total > target_num:
            continue
        result = check_options(target_num, new_total, nums_to_check[1:], operators)
        if result:
            return result
    return 0

total_result = 0
for target, numbers in data.items():
    total_result += check_options(target, numbers[0], numbers[1:], operators=[add, mul])
print(f"Part 1: {total_result}")


def concat(x, y):
    return int(f"{x}{y}")

total_result = 0
operators_p2 = [add, mul, concat]
for target, numbers in data.items():
    total_result += check_options(target, numbers[0], numbers[1:], operators=operators_p2)
print(f"Part 2: {total_result}")