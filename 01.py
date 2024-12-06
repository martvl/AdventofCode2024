from read_input import read_day_01

arr_1, arr_2 = read_day_01()

# Part 1
distance = 0
for l, r in zip(sorted(arr_1), sorted(arr_2)):
    distance += abs(l-r)

print(f"Distance: {distance}")

# Part 2
from collections import Counter

arr_2_count = Counter(arr_2)

similarity = 0
for num in arr_1:
    similarity += num*arr_2_count[num]
    
print(f"Similarity: {similarity}")
