from read_input import read_day_05
from collections import defaultdict, deque
from math import floor

rules, updates = read_day_05()

order = defaultdict(list)
for rule in rules:
    order[rule[0]].append(rule[1])

valid_updates_index = []
invalid_updates_index = []
for update_no, update in enumerate(updates):
    for i, page in enumerate(update):
        if not set(update[i+1:]).issubset(order[page]):
            invalid_updates_index.append(update_no)
            break
    else:
        valid_updates_index.append(update_no)

valid_middle_numbers = 0
for update_no in valid_updates_index:
    valid_middle_numbers += updates[update_no][floor(len(updates[update_no])/2)]
print(f"Part 1: {valid_middle_numbers}")


def merge_rules(rules):
    # Create a graph from the rule subset
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for a, b in rules:
        graph[a].append(b)
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0
    
    # Topological sort
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result


middle_numbers_fixed_updates = 0
for update_no in invalid_updates_index:
    # Subset rules bc otherwise it will be cyclical
    merged_rules = merge_rules([rule for rule in rules if rule[0] in updates[update_no]])
    ordered_update = [page for page in merged_rules if page in updates[update_no]]
    middle_numbers_fixed_updates += ordered_update[floor(len(ordered_update)/2)]

print(f"Part 2: {middle_numbers_fixed_updates}")
