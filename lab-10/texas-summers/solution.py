import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if not data:
    sys.exit(0)

n = data[0]
points = []
idx = 1

for _ in range(n + 2):
    x = data[idx]
    y = data[idx + 1]
    idx += 2
    points.append((x, y))

start = n
target = n + 1
total = n + 2
dist = [10**30] * total
parent = [-1] * total
used = [False] * total
dist[start] = 0

# dense dijkstra is enough here
for _ in range(total):
    best = -1
    for i in range(total):
        if not used[i] and (best == -1 or dist[i] < dist[best]):
            best = i

    if best == -1 or dist[best] == 10**30:
        break

    used[best] = True
    if best == target:
        break

    x1, y1 = points[best]

    for nxt in range(total):
        if used[nxt] or nxt == best:
            continue

        x2, y2 = points[nxt]
        dx = x1 - x2
        dy = y1 - y2
        cost = dx * dx + dy * dy
        cand = dist[best] + cost

        if cand < dist[nxt]:
            dist[nxt] = cand
            parent[nxt] = best

path = []
cur = target

while cur != -1:
    path.append(cur)
    cur = parent[cur]

path.reverse()
out = []

for node in path:
    if 0 <= node < n:
        out.append(str(node))

if out:
    sys.stdout.write("\n".join(out) + "\n")
else:
    sys.stdout.write("-\n")
