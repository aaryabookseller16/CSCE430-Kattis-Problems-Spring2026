import sys
import bisect

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

n = int(data[0])
k = int(data[1])
vals = list(map(int, data[2:]))
acts = []
for i in range(0, len(vals), 2):
    s = vals[i]
    f = vals[i + 1]
    acts.append((s, f))

acts.sort(key=lambda x: (x[1], x[0]))  # sort by end time

rooms = []  # end times of rooms in use
ans = 0

for s, f in acts:
    pos = bisect.bisect_right(rooms, s)  # latest room that ends before start
    if pos:
        rooms.pop(pos - 1)
        rooms.append(f)  # f is non-decreasing, so append keeps order
        ans += 1
    elif len(rooms) < k:
        rooms.append(f)
        ans += 1

sys.stdout.write(str(ans))
