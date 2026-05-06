import sys
import math

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

it = iter(data)
out = []
while True:
    try:
        n = int(next(it))
        l = float(next(it))
        w = float(next(it))
    except StopIteration:
        break
    intervals = []
    half_w = w / 2.0
    for _ in range(n):
        x = float(next(it))
        r = float(next(it))
        if r <= half_w:
            continue
        dx = math.sqrt(r * r - half_w * half_w)  # half width of coverage on x
        left = x - dx
        right = x + dx
        if right < 0 or left > l:
            continue
        if left < 0:
            left = 0.0
        if right > l:
            right = l
        intervals.append((left, right))

    intervals.sort()
    covered = 0.0  # how far we've watered
    idx = 0
    used = 0
    ok = True
    while covered < l:
        best = covered  # furthest reach we can extend now
        while idx < len(intervals) and intervals[idx][0] <= covered + 1e-9:
            if intervals[idx][1] > best:
                best = intervals[idx][1]
            idx += 1
        if best == covered:
            ok = False
            break
        used += 1
        covered = best
    out.append(str(used if ok else -1))

sys.stdout.write("\n".join(out))
