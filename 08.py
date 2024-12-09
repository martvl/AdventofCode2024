from read_input import read_day_08
from collections import defaultdict
from itertools import permutations

data = read_day_08()

def find_direction(left_antenna, right_antenna):

    direction = (
        left_antenna[0] - right_antenna[0],
        left_antenna[1] - right_antenna[1]
    )

    return direction

def reverse_direction(direction):

    return (direction[0] * -1, direction[1] * -1)

grid = defaultdict(list)
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            grid[char].append((x,y))

bounds = (x,y)

# Part 1
antinodes_p1 = set()
for freq, locations in grid.items():
    for left, right in permutations(locations,2):
        direction = reverse_direction(find_direction(left, right))
        antinode = (right[0] + direction[0], right[1] + direction[1])
        if antinode[0] < 0 or antinode [1] < 0:
            continue
        if antinode[0] > bounds[0] or antinode[1] > bounds[1]:
            continue
        antinodes_p1.add(antinode)

print(len(antinodes_p1))

# Part 2

antinodes_p2 = set()
for freq, locations in grid.items():
    for left, right in permutations(locations,2):
        direction = reverse_direction(find_direction(left, right))
        for i in range(1, bounds[1]):
            antinode = (right[0] + direction[0]*i, right[1] + direction[1]*i)
            if antinode[0] < 0 or antinode [1] < 0:
                continue
            if antinode[0] > bounds[0] or antinode[1] > bounds[1]:
                continue
            antinodes_p2.add(antinode)
            antinodes_p2.add(left)
            antinodes_p2.add(right)

print(len(antinodes_p2))