import sys
from collections import deque

input = sys.stdin.readline

line = input().strip()
if not line:
    sys.exit(0)

n, m = map(int, line.split())
grid = [input().strip() for _ in range(n)]

depth = [[0] * m for _ in range(n)]
dq = deque()

for i in range(n):
    row = grid[i]
    for j in range(m):
        if row[j] != "X":
            continue

        exposed = False

        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            exposed = True  # pan boundary always gets chipified
        elif grid[i - 1][j] != "X" or grid[i + 1][j] != "X" or grid[i][j - 1] != "X" or grid[i][j + 1] != "X":
            exposed = True  # touching empty space means this layer can be made now

        if exposed:
            depth[i][j] = 1
            dq.append(i * m + j)

ans = 0

# bfs inward from every currently exposed square
while dq:
    cur = dq.popleft()
    r = cur // m
    c = cur % m

    if depth[r][c] > ans:
        ans = depth[r][c]

    if r > 0 and grid[r - 1][c] == "X" and depth[r - 1][c] == 0:
        depth[r - 1][c] = depth[r][c] + 1
        dq.append((r - 1) * m + c)
    if r + 1 < n and grid[r + 1][c] == "X" and depth[r + 1][c] == 0:
        depth[r + 1][c] = depth[r][c] + 1
        dq.append((r + 1) * m + c)
    if c > 0 and grid[r][c - 1] == "X" and depth[r][c - 1] == 0:
        depth[r][c - 1] = depth[r][c] + 1
        dq.append(r * m + (c - 1))
    if c + 1 < m and grid[r][c + 1] == "X" and depth[r][c + 1] == 0:
        depth[r][c + 1] = depth[r][c] + 1
        dq.append(r * m + (c + 1))

sys.stdout.write(str(ans))
