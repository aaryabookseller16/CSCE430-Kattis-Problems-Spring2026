import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)

tests = data[0]
idx = 1
out = []
INF = 10**9

for _ in range(tests):
    m = data[idx]
    idx += 1
    dist = data[idx:idx + m]
    idx += m

    total = sum(dist)
    prev = [INF] * (total + 1)
    prev[0] = 0

    parent_h = [[-1] * (total + 1) for _ in range(m + 1)]
    parent_move = [[""] * (total + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        d = dist[i - 1]
        cur = [INF] * (total + 1)

        for h in range(total + 1):
            if prev[h] == INF:
                continue

            nh = h + d
            peak = prev[h]
            if nh > peak:
                peak = nh
            if peak < cur[nh]:
                cur[nh] = peak
                parent_h[i][nh] = h
                parent_move[i][nh] = "U"  # going up raises the current height

            if h >= d:
                nh = h - d
                peak = prev[h]
                if peak < cur[nh]:
                    cur[nh] = peak
                    parent_h[i][nh] = h
                    parent_move[i][nh] = "D"  # going down keeps the same peak

        prev = cur

    if prev[0] == INF:
        out.append("IMPOSSIBLE")
        continue

    ans = []
    h = 0
    for i in range(m, 0, -1):
        ans.append(parent_move[i][h])
        h = parent_h[i][h]

    ans.reverse()
    out.append("".join(ans))

sys.stdout.write("\n".join(out))
