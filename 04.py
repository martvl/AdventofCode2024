from read_input import read_day_04
from itertools import permutations

data = read_day_04()

# Part 1

all_directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1), (-1,-1)]

def check_in_direction(data, start_x, start_y, direction_x, direction_y):
    for i, letter in enumerate("MAS"):
        try:
            check_y = start_y + (direction_y * (i+1))
            check_x = start_x + (direction_x * (i+1))
            if check_y < 0 or check_x < 0:
                    raise IndexError
            if data[check_y][check_x] != letter:
                return 0
            elif letter == "S":
                return 1
        except IndexError:
            continue
    return 0

xmas_count = 0
for line_no, line in enumerate(data):
    for i, char in enumerate(line):
        if char != "X":
            continue
        for (x, y) in all_directions:
            result = check_in_direction(data, start_x=i, start_y=line_no, direction_x=x, direction_y=y)
            xmas_count += result

print(f"Part 1: {xmas_count}")

# Part 2

all_directions = [(-1, 1), (1, -1), (1,1), (-1,-1)]
xmas_count = 0
for line_no, line in enumerate(data):
    if line_no == 0:
        continue
    for i, char in enumerate(line):
        if i == 0:
            continue
        if char == "A":
            coords_to_get = [(line_no + dy, i + dx) for dy, dx in all_directions ]
            try:
                cross = "".join([data[y][x] for y,x in coords_to_get])
            except IndexError:
                continue
            if cross == "MSSM" or cross == "SMMS" or cross == "MSMS" or cross == "SMSM":
                xmas_count += 1
print(f"Part 2: {xmas_count}")