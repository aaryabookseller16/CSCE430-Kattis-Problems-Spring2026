import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if not data:
    sys.exit(0)

n = data[0]
l = data[1]
idx = 2
time = 0
pos = 0

for _ in range(n):
    d = data[idx]
    r = data[idx + 1]
    g = data[idx + 2]
    idx += 3

    # drive to this light first
    time += d - pos
    pos = d

    cycle = r + g
    where = time % cycle

    # if we arrive during red, we have to sit there
    if where < r:
        time += r - where

# finish the last stretch
time += l - pos

sys.stdout.write(str(time) + "\n")
