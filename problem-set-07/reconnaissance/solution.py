import sys

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit(0)

n = int(data[0])

position = [0]*n
speed = [0]*n
distance = [0]*n

idx = 1
for i in range(n):
    position[i] = int(data[idx]); idx += 1
    speed[i] = int(data[idx]); idx += 1

left = 0.0
right = 200000.0  # safe upper bound for time

for _ in range(200):  # ternary search iterations
    m1 = left + (right-left)/3.0
    m2 = right - (right-left)/3.0

    min_pos = float("inf")
    max_pos = float("-inf")
    for i in range(n):
        distance[i] = position[i] + speed[i]*m1  # position of vehicle at time m1
        min_pos = min(min_pos, distance[i])
        max_pos = max(max_pos, distance[i])
    d1 = max_pos - min_pos  # spread at m1

    min_pos = float("inf")
    max_pos = float("-inf")
    for i in range(n):
        distance[i] = position[i] + speed[i]*m2  # position of vehicle at time m2
        min_pos = min(min_pos, distance[i])
        max_pos = max(max_pos, distance[i])
    d2 = max_pos - min_pos  # spread at m2

    if d1 <= d2:
        right = m2  # minimum lies left
    else:
        left = m1  # minimum lies right

t = (left+right)/2.0  # best time

min_pos = float("inf")
max_pos = float("-inf")
for i in range(n):
    distance[i] = position[i] + speed[i]*t
    min_pos = min(min_pos, distance[i])
    max_pos = max(max_pos, distance[i])

ans = max_pos - min_pos  # minimum sensor range
sys.stdout.write(f"{ans:.6f}\n")