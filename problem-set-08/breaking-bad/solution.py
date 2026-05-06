import sys
from collections import deque

input = sys.stdin.readline

line = input().strip()
if not line:
    sys.exit(0)

item_count = int(line)
item_names = [input().strip() for _ in range(item_count)]

name_to_index = {}
for i in range(item_count):
    name_to_index[item_names[i]] = i

edge_count = int(input())
graph = [[] for _ in range(item_count)]

for _ in range(edge_count):
    first_name, second_name = input().split()
    first_index = name_to_index[first_name]
    second_index = name_to_index[second_name]
    graph[first_index].append(second_index)
    graph[second_index].append(first_index)

group = [-1] * item_count
possible = True

for start in range(item_count):
    if group[start] != -1:
        continue

    group[start] = 0
    queue = deque([start])

    # just color the graph like a normal bipartite check
    while queue and possible:
        current = queue.popleft()

        for next_item in graph[current]:
            if group[next_item] == -1:
                group[next_item] = 1 - group[current]
                queue.append(next_item)
            elif group[next_item] == group[current]:
                possible = False
                break

    if not possible:
        break

if not possible:
    sys.stdout.write("impossible")
    sys.exit(0)

walter_items = []
jesse_items = []

for i in range(item_count):
    if group[i] == 0:
        walter_items.append(item_names[i])
    else:
        jesse_items.append(item_names[i])

sys.stdout.write(" ".join(walter_items) + "\n" + " ".join(jesse_items))
