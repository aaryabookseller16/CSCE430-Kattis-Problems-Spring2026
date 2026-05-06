import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if not data:
    sys.exit(0)

n = data[0]
m = data[1]

# these are the edges Barney can waste inside cycles
extra = m - (n - 1)
pos = 0
answer = 0

for added in range(1, n):
    # this edge must join a new city to the growing component
    pos += 1
    answer += pos

    # after that we can spend some cheap labels on useless cycle edges
    can = added - 1
    if extra < can:
        can = extra
    pos += can
    extra -= can

sys.stdout.write(str(answer) + "\n")