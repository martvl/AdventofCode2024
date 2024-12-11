from collections import defaultdict
from read_input import read_day_11
from multiprocessing import Pool

data = read_day_11(example=True)

# Part 1
def blink(d, n, report_n = [25]):
    result = {}
    for i in range(n):
        new_seq = []
        for num_s in d:
            if num_s == "0":
                new_seq.append("1")
            elif (l:=len(num_s)) % 2 == 0:
                new_seq.extend([num_s[:int(l/2)], str(int(num_s[int(l/2):]))])
            else:
                new_seq.append(str(int(num_s)*2024))
        d = new_seq
        if i+1 in report_n:
            result[i+1] = len(d)
    return result

print(f"Part 1: {blink(data, 25)[25]}")


