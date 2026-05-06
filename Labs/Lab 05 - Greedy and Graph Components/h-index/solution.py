import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

n = int(data[0])
cites = list(map(int, data[1:1 + n]))

cites.sort(reverse=True)  # biggest first

h = 0
for i, val in enumerate(cites, 1):
    if val >= i:
        h = i  # still ok
    else:
        break

print(h)
