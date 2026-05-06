import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if not data:
    sys.exit(0)

n = data[0]
m = data[1]

adj = [[] for _ in range(n + 1)]
idx = 2

for _ in range(m):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    adj[a].append(b)
    adj[b].append(a)

seen = [False] * (n + 1)
stack = [1]
seen[1] = True

# plain iterative dfs
while stack:
    node = stack.pop()
    for nxt in adj[node]:
        if not seen[nxt]:
            seen[nxt] = True
            stack.append(nxt)

out = []

for house in range(1, n + 1):
    if not seen[house]:
        out.append(str(house))

if out:
    sys.stdout.write("\n".join(out) + "\n")
else:
    sys.stdout.write("Connected\n")
