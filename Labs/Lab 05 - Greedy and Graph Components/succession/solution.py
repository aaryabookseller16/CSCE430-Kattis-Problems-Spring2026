import sys
from collections import defaultdict, deque

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])
founder = data[2]

pos = 3
children = defaultdict(list)
parents = {}
for _ in range(n):
    child = data[pos]
    p1 = data[pos + 1]
    p2 = data[pos + 2]
    pos += 3
    children[p1].append(child)
    children[p2].append(child)
    parents[child] = (p1, p2)

claimants = data[pos:]

blood = defaultdict(float)
blood[founder] = 1.0

# topological order: process parents before child
indeg = defaultdict(int)
for c, (p1, p2) in parents.items():
    indeg[c] += 2
    indeg[p1] += 0
    indeg[p2] += 0

q = deque()
for name in indeg:
    if indeg[name] == 0:
        q.append(name)
if founder not in indeg:
    indeg[founder] = 0
    q.append(founder)

while q:
    person = q.popleft()
    for child in children[person]:
        indeg[child] -= 1
        if indeg[child] == 0:
            p1, p2 = parents[child]
            blood[child] = blood[p1] / 2 + blood[p2] / 2
            q.append(child)

best = None
best_val = -1
for name in claimants:
    val = blood[name]
    if val > best_val:
        best_val = val
        best = name

print(best)
