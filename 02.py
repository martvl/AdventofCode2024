from read_input import read_day_02



data = read_day_02()

# Part 1
results = {"safe": 0, "unsafe": 0}
def check_safety(level_set):
    if sorted(level_set) != level_set and sorted(level_set, reverse=True) != level_set:
        return "unsafe"
    for i, j in zip(level_set, level_set[1:]):
        diff = abs(i-j)
        if diff == 0 or diff >= 4:
            return "unsafe"
    else:
        return "safe"
for level_set in data:
    results[check_safety(level_set)] += 1

print(f"Results part 1: {results}")

def dampener(level_set):
    dampened_levels = []
    for i, item in enumerate(level_set):
        copy_set = level_set.copy()
        copy_set.pop(i)
        dampened_levels.append(copy_set)
    return dampened_levels


# Part 2
results = {"safe": 0, "unsafe": 0}
for level_set in data:
    original_result = check_safety(level_set)
    for dampened_set in dampener(level_set):
        dampened_result = check_safety(dampened_set)
        if dampened_result == "safe" and original_result == "unsafe":
            results[dampened_result] += 1
            break
    else:
        results[original_result] += 1
    

print(f"Results part 2: {results}")

