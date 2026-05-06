import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
k = int(next(it))
board_lines = [next(it) for _ in range(n)]
ship_sizes = [int(next(it)) for _ in range(k)]

hits = set()
misses = set()
for r in range(n):
    for c, ch in enumerate(board_lines[r]):
        if ch in ('0', 'o', 'O'):
            hits.add((r, c))
        elif ch in ('x', 'X'):
            misses.add((r, c))

grid_used = [[False] * n for _ in range(n)]
total_ways = 0

def can_place(r, c, dr, dc, length):
    for t in range(length):
        nr = r + dr * t
        nc = c + dc * t
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            return False
        if grid_used[nr][nc]:
            return False
        if (nr, nc) in misses:
            return False
    return True

def place_ship(r, c, dr, dc, length, val):
    for t in range(length):
        nr = r + dr * t
        nc = c + dc * t
        grid_used[nr][nc] = val

def dfs(idx):
    global total_ways
    if idx == k:
        for hr, hc in hits:
            if not grid_used[hr][hc]:
                return
        total_ways += 1
        return
    length = ship_sizes[idx]
    for r in range(n):
        for c in range(n):
            # horizontal
            if can_place(r, c, 0, 1, length):
                place_ship(r, c, 0, 1, length, True)
                dfs(idx + 1)
                place_ship(r, c, 0, 1, length, False)
            # vertical (skip duplicate when length 1)
            if length > 1 and can_place(r, c, 1, 0, length):
                place_ship(r, c, 1, 0, length, True)
                dfs(idx + 1)
                place_ship(r, c, 1, 0, length, False)

dfs(0)
print(total_ways)
