import numpy as np
import sys

lines_list = [line.rstrip("\n") for line in sys.stdin]

n = len(lines_list)

# using a numpy array to store output
output_list = np.full((1000, 1000), "0", dtype=str)

# marking start location
j, k = 500, 500 # iterators, start at the middle of the file
j_max, k_max = j, k # right and down extremities
j_min, k_min = j, k # left and up extremities

output_list[j, k] = "S"

for direction in lines_list:
    direction = direction.strip()

    if direction == "down":
        j += 1
        
    elif direction == "left":
        k -= 1
        
    elif direction == "up":
        j -= 1
        
    elif direction == "right":
        k += 1

    #print(f"j = {j}, k = {k} \n")

    # don't overwrite the start marker if we revisit it
    if output_list[j, k] != "S":
        output_list[j, k] = "*"

    j_min = min(j, j_min)
    k_min = min(k, k_min)
    j_max = max(j, j_max)
    k_max = max(k, k_max)
    
# marking end location
output_list[j, k] = "E"

# print the bounds
for rows in range(j_min, j_max+1):
    for columns in range(k_min, k_max+1):
        if output_list[rows, columns] == "0":
            output_list[rows, columns] = " "

# extract final bounded result
final_result = output_list[j_min:j_max+1, k_min:k_max+1]
final_result = np.pad(final_result, 1, mode="constant", constant_values="#")
for row in final_result:
    print("".join(row))