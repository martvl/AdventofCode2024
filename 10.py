from read_input import read_day_10

data = read_day_10()
grid = []
trailheads = []

for y, line in enumerate(data):
    grid.append([])
    for x, height in enumerate(line):
        if height == "0":
            trailheads.append((x,y))
        grid[y].append(int(height))

# Part 1
directions = [(0,1), (1,0), (-1, 0), (0, -1)]
visited = set()
def follow_trail(trailhead):
    x,y = trailhead
    if (x,y) in visited:
        return []
    visited.add((x,y))
    current_value = grid[y][x]
    if current_value == 9:
        return [(x,y)]
    hills_reached = []
    for dy, dx in directions:
        new_y, new_x = y+dy, x+dx
        if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
            next_value = grid[new_y][new_x]
            if next_value == current_value + 1:
                # print(f"Going to {(x+dx, y+dy)} {current_value=} {next_value=}")
                hills_reached.extend(follow_trail((x+dx, y+dy)))
    return hills_reached

score = 0
for t in trailheads:
    all_hills_reached = follow_trail(t)
    score += len(set(all_hills_reached))
    visited.clear()

print(f"Part 1: {score}")

# Part 2
def follow_trail(trailhead):
    x,y = trailhead
    current_value = grid[y][x]
    if current_value == 9:
        return [(x,y)]
    hills_reached = []
    for dy, dx in directions:
        new_y, new_x = y+dy, x+dx
        if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
            next_value = grid[new_y][new_x]
            if next_value == current_value + 1:
                # print(f"Going to {(x+dx, y+dy)} {current_value=} {next_value=}")
                hills_reached.extend(follow_trail((x+dx, y+dy)))
    return hills_reached

rating = 0
for t in trailheads:
    highest_positions_reached = set()
    all_hills_reached = follow_trail(t)
    rating += len(all_hills_reached)

print(f"Part 2: {rating}")
