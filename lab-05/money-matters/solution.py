import sys
sys.setrecursionlimit(2000000)

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
m = int(next(it))
balance = [int(next(it)) for _ in range(n)]

adj = [[] for _ in range(n)]
for _ in range(m):
    a = int(next(it))
    b = int(next(it))
    adj[a].append(b)
    adj[b].append(a)

seen = [False] * n
ok = True

def dfs(start):
    stack = [start]
    total = 0
    while stack:
        u = stack.pop()
        if seen[u]:
            continue
        seen[u] = True
        total += balance[u]
        for v in adj[u]:
            if not seen[v]:
                stack.append(v)
    return total

for i in range(n):
    if not seen[i]:
        if dfs(i) != 0:
            ok = False
            break

print("POSSIBLE" if ok else "IMPOSSIBLE")
