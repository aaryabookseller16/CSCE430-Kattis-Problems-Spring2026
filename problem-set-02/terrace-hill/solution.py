import sys

DEBUG = False

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit(0)

n = int(data[0])
heights = list(map(int, data[1:1 + n]))

# stack keeps [height, last_index], heights in decreasing order
stack = []
total = 0

for i, h in enumerate(heights):
    if DEBUG:
        print("i", i, "h", h, "stack", stack, file=sys.stderr)

    # pop smaller heights (they can't bridge past a taller one)
    while stack and stack[-1][0] < h:
        if DEBUG:
            print("pop", stack[-1], "because", h, "is taller", file=sys.stderr)
        stack.pop()

    if stack and stack[-1][0] == h:
        # same height, all between are lower -> valid bridge
        prev_idx = stack[-1][1]
        length = i - prev_idx - 1
        total += length
        if DEBUG:
            print("bridge", prev_idx, "->", i, "len", length, "total", total, file=sys.stderr)
        stack[-1][1] = i  # update last seen
    else:
        stack.append([h, i])
        if DEBUG:
            print("push", h, i, file=sys.stderr)

print(total)
