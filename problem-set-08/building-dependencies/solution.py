import sys
from collections import deque

input = sys.stdin.readline

line = input().strip()
if not line:
    sys.exit(0)

n = int(line)
files = []
deps_text = []

for _ in range(n):
    parts = input().split()
    files.append(parts[0][:-1])
    deps_text.append(parts[1:])

changed = input().strip()

name_to_id = {}
for i in range(n):
    name_to_id[files[i]] = i

deps = [[] for _ in range(n)]
rev = [[] for _ in range(n)]

for i in range(n):
    for dep_name in deps_text[i]:
        dep = name_to_id[dep_name]
        deps[i].append(dep)
        rev[dep].append(i)  # if dep changes, this file also needs rebuild

start = name_to_id[changed]

need = [False] * n
dq = deque([start])
need[start] = True

# find every file that depends on the changed file
while dq:
    cur = dq.popleft()

    for nxt in rev[cur]:
        if need[nxt]:
            continue
        need[nxt] = True
        dq.append(nxt)

indeg = [0] * n

# only count deps that are also getting rebuilt
for i in range(n):
    if not need[i]:
        continue
    for dep in deps[i]:
        if need[dep]:
            indeg[i] += 1

dq = deque()
for i in range(n):
    if need[i] and indeg[i] == 0:
        dq.append(i)

out = []

# regular topo sort on just the affected files
while dq:
    cur = dq.popleft()
    out.append(files[cur])

    for nxt in rev[cur]:
        if not need[nxt]:
            continue
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            dq.append(nxt)

sys.stdout.write("\n".join(out))
