import sys

line = sys.stdin.buffer.readline().split()

if not line:
    sys.exit(0)

r = int(line[0])
c = int(line[1])
grid = []
fire_q = []
joe_q = []
start = -1

for i in range(r):
    row = bytearray(sys.stdin.buffer.readline().strip())
    for j in range(c):
        if row[j] == 74:
            start = i * c + j
            row[j] = 46
        elif row[j] == 70:
            fire_q.append(i * c + j)
    grid.append(row)

joe_q.append(start)
seen = bytearray(r * c)
seen[start] = 1
joe_head = 0
fire_head = 0
time = 0

# do Joe first each minute, then spread the fire
while joe_head < len(joe_q):
    joe_end = len(joe_q)

    for idx in range(joe_head, joe_end):
        pos = joe_q[idx]
        x = pos // c
        y = pos % c

        # if this spot burned last minute, Joe can't keep going
        if grid[x][y] == 70:
            continue

        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            sys.stdout.write(str(time + 1) + "\n")
            sys.exit(0)

        up = pos - c
        if not seen[up] and grid[x - 1][y] == 46:
            seen[up] = 1
            joe_q.append(up)

        down = pos + c
        if not seen[down] and grid[x + 1][y] == 46:
            seen[down] = 1
            joe_q.append(down)

        left = pos - 1
        if not seen[left] and grid[x][y - 1] == 46:
            seen[left] = 1
            joe_q.append(left)

        right = pos + 1
        if not seen[right] and grid[x][y + 1] == 46:
            seen[right] = 1
            joe_q.append(right)

    joe_head = joe_end
    fire_end = len(fire_q)

    for idx in range(fire_head, fire_end):
        pos = fire_q[idx]
        x = pos // c
        y = pos % c

        if x > 0 and grid[x - 1][y] != 35 and grid[x - 1][y] != 70:
            grid[x - 1][y] = 70
            fire_q.append(pos - c)
        if x + 1 < r and grid[x + 1][y] != 35 and grid[x + 1][y] != 70:
            grid[x + 1][y] = 70
            fire_q.append(pos + c)
        if y > 0 and grid[x][y - 1] != 35 and grid[x][y - 1] != 70:
            grid[x][y - 1] = 70
            fire_q.append(pos - 1)
        if y + 1 < c and grid[x][y + 1] != 35 and grid[x][y + 1] != 70:
            grid[x][y + 1] = 70
            fire_q.append(pos + 1)

    fire_head = fire_end
    time += 1

sys.stdout.write("IMPOSSIBLE\n")
