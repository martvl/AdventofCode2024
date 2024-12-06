import re
from read_input import read_day_03

data = read_day_03()

def mul(x, y):
    return x*y


def find_and_perform_multiplication(s):
    results = []
    pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")
    for match in re.findall(pattern, s):
        results.append(eval(match))
    
    return results

# Part 1

results = []
pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")
for line in data:
    results += find_and_perform_multiplication(line)
    

print(f"Result part 1: {sum(results)}")

# Part 2
results = []
pattern = re.compile(r"do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)")
flag = True
for line in data:
    for match in re.findall(pattern, line):
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                results.append(eval(match))
print(f"Result part 2: {sum(results)}")