from read_input import read_day_06
from itertools import cycle

data = read_day_06()
def index_map(data):
    obstacle_coords = []
    starting_position = ()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "^":
                starting_position = x,y
            elif char == "#":
                obstacle_coords.append((x,y))
    
    bounds = x, y
    return set(obstacle_coords), starting_position, bounds

OBSTACLE_COORDS, STARTING_POSITION, BOUNDS = index_map(data)
POSITIONS_VISITED = set()

def move_in_direction(position, direction):
    new_x = position[0] + direction[0]
    new_y = position[1] + direction[1]
    return new_x, new_y
            
def find_next_obstacle(position, direction, obstacle_coords):
    while True:
        new_position = move_in_direction(position, direction)
        if new_position in obstacle_coords:
            relevant_obstacle = new_position
            return position, relevant_obstacle
        elif new_position[0] > BOUNDS[0] or new_position[1] > BOUNDS[1] or any([i < 0 for i in new_position]):
            return None, None
        position = new_position
        POSITIONS_VISITED.add(position)
    

POSITIONS_VISITED.add(STARTING_POSITION)
def patrol(break_on_loop = False, obstacle_coords = OBSTACLE_COORDS, obstacles_encountered = None):
    
    directions = cycle([(0,-1), (1,0), (0,1), (-1, 0)])
    new_position = STARTING_POSITION

    while True:
        direction = next(directions)
        new_position, relevant_obstacle = find_next_obstacle(new_position, direction, obstacle_coords)
        if break_on_loop:
            if (relevant_obstacle, direction) in obstacles_encountered:
                return True
            else:
                obstacles_encountered.add((relevant_obstacle, direction))
        if new_position is None:
            break
    return False
patrol()
print(f"Part 1: {len(POSITIONS_VISITED)} positions visited")
    
# Part 2
loops_detected = []
for x in range(BOUNDS[0]+1):
    for y in range(BOUNDS[1]+1):
        POSITIONS_VISITED = set()
        
        if (x,y) in OBSTACLE_COORDS:
            continue
        current_obstacles = OBSTACLE_COORDS.copy()
        current_obstacles.add((x,y))
        obstacles_encountered = set()
        loops_detected.append(patrol(break_on_loop=True, obstacle_coords=current_obstacles, obstacles_encountered=obstacles_encountered))
print(f"Part 2: {sum(loops_detected)} possible loops detected")