import sys
from collections import deque

input = sys.stdin.readline

line = input().strip()
if not line:
    sys.exit(0)

t = int(line)
out = []
INF = 10**9
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(t):
    h, w = map(int, input().split())

    grid = ["." * (w + 2)]
    prisoners = []

    for i in range(h):
        row = list("." + input().strip() + ".")
        for j in range(1, w + 1):
            if row[j] == "$":
                prisoners.append((i + 1, j))
                row[j] = "."  # treat prisoner spot like empty floor
        grid.append("".join(row))

    grid.append("." * (w + 2))

    h += 2
    w += 2

    starts = [(0, 0), prisoners[0], prisoners[1]]
    dist_all = []

    # run 0-1 bfs from outside and both prisoners
    for sr, sc in starts:
        dist = [[INF] * w for _ in range(h)]
        dq = deque()
        dq.append((sr, sc))
        dist[sr][sc] = 0

        while dq:
            r, c = dq.popleft()

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if nr < 0 or nr >= h or nc < 0 or nc >= w:
                    continue
                if grid[nr][nc] == "*":
                    continue

                nd = dist[r][c]
                if grid[nr][nc] == "#":
                    nd += 1

                if nd >= dist[nr][nc]:
                    continue

                dist[nr][nc] = nd
                if grid[nr][nc] == "#":
                    dq.append((nr, nc))  # doors cost 1, so push back
                else:
                    dq.appendleft((nr, nc))  # empty cells cost 0

        dist_all.append(dist)

    ans = INF

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "*":
                continue

            total = dist_all[0][i][j] + dist_all[1][i][j] + dist_all[2][i][j]
            if total >= INF:
                continue

            if grid[i][j] == "#":
                total -= 2  # same door got counted once per path

            if total < ans:
                ans = total

    out.append(str(ans))

sys.stdout.write("\n".join(out))
