from read_input import read_day_09
from collections import defaultdict

data = read_day_09()

# Part 1

def index_disk(data, reverse=False):
    full_disk = dict()
    if reverse:
        full_disk = defaultdict(list)
    file_index = 0
    disk_index = 0
    n_file_blocks = 0
    for i, n in enumerate(data):
        if i % 2 == 0:
            for _ in range(int(n)):
                if not reverse:
                    full_disk[disk_index] = file_index
                else:
                    full_disk[file_index].append(disk_index)
                disk_index += 1
                n_file_blocks += 1
            file_index += 1
        else:
            for _ in range(int(n)):
                if not reverse:
                    full_disk[disk_index] = None
                disk_index += 1
    return full_disk, n_file_blocks

def clean_disk(full_disk, n_file_blocks):
    
    cleaned_disk = dict()
    for k,v in full_disk.items():
        if n_file_blocks == 0:
            break
        if v is not None:
            cleaned_disk[k] = v
        else:
            for rev_k, rev_v in reversed(full_disk.items()):
                if rev_v is None:
                    continue
                else:
                    index_to_insert = rev_k
                    break
            cleaned_disk[k] = full_disk[index_to_insert]
            full_disk[index_to_insert] = None
        n_file_blocks -= 1
    return cleaned_disk

full_disk, n_file_blocks = index_disk(data)
cleaned_disk = clean_disk(full_disk, n_file_blocks)
checksum = sum(k*v for k,v in cleaned_disk.items())
print(f"Part 1: {checksum}")

# Part 2 
# Refresh full_disk index
full_disk, n_file_blocks = index_disk(data)
reverse_disk_index, _ = index_disk(data, reverse=True)

def index_free_space(full_disk, reverse = False):
    free_space_index = dict()
    for k,v in full_disk.items():
        if v is not None:
            contiguous_block = None
        if v is None:
            if contiguous_block is None:
                contiguous_block = k
                free_space_index[contiguous_block] = 1
            else:
                free_space_index[contiguous_block] += 1
    if reverse:
        reverse_free_space_index = defaultdict(list)
        for k,v in free_space_index.items():
            reverse_free_space_index[v].append(k)
        return reverse_free_space_index

    return free_space_index

free_space_index = index_free_space(full_disk)
cleaned_disk = dict()

for file_index, location_array in reversed(reverse_disk_index.items()):
    for free_block_index, block_width in free_space_index.items():
        if free_block_index < min(location_array):
            if block_width >= len(location_array):
                new_location_array = [free_block_index + i for i in range(len(location_array))]
                break
        else:
            new_location_array = None
            break
        new_location_array = None

    if new_location_array is not None:
        free_space_index.pop(free_block_index)
        if len(new_location_array) < block_width:
            free_space_index[free_block_index+len(new_location_array)] = block_width - len(new_location_array)
        reverse_disk_index[file_index] = new_location_array
        free_space_index = dict(sorted(free_space_index.items()))

checksum = 0
for file_index, disk_indices in reverse_disk_index.items():
    for i in disk_indices:
        checksum += (file_index * i)

print(f"Part 2: {checksum}")