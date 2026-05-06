import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)

t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    w = data[idx + 1]
    l = data[idx + 2]
    idx += 3

    freight = data[idx:idx + w]
    idx += w

    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2

        used = 0
        pos = 1
        j = 0

        # count how many trains we need if every Luxembourg train is at most mid long
        while pos <= n and used <= l:
            while j < w and freight[j] < pos:
                j += 1

            if j == w:
                used += 1  # one last train can take all the empty wagons
                break

            if freight[j] - pos + 1 > mid:
                used += 1  # too much empty stuff in front, send it away in one chunk
                pos = freight[j]
            else:
                used += 1  # send a Luxembourg train of length mid from the current front
                pos += mid

        if used <= l:
            right = mid  # this max length works
        else:
            left = mid + 1  # need longer Luxembourg trains

    out.append(str(left))

sys.stdout.write("\n".join(out))
