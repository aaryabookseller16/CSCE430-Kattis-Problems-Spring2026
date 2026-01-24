import sys

data = sys.stdin.read().strip().split()
number_of_buses = int(data[0]) # size
numbers = list(map(int, data[1:])) # make a list
numbers.sort() # sort it for easy lookup
nums_set = set(numbers) # set for shorter search time

answer = []

for num in numbers:
    # skip duplicates
    if num - 1 in nums_set:
        continue

    current = num
    collection = [current]

    # while a given number has a sequence
    while current + 1 in nums_set:
        current += 1
        collection.append(current)

    answer.append(collection)


output = []

for subcollection in answer:
    if len(subcollection) >= 3: # condition for special output
        output.append(f"{subcollection[0]}-{subcollection[-1]}")
    else:
        output.append(" ".join(map(str, subcollection)))

print(" ".join(output))