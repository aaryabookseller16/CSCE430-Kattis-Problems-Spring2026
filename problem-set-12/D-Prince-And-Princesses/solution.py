import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if not data:
    sys.exit(0)

t = data[0]
idx = 1
out = []

for case in range(1, t + 1):
    n = data[idx]
    p = data[idx + 1]
    q = data[idx + 2]
    idx += 3

    total = n * n
    pos = [-1] * (total + 1)

    # remember where each prince square appears
    for i in range(p + 1):
        value = data[idx + i]
        pos[value] = i
    idx += p + 1

    tails = []

    # turn the princess route into prince positions
    for i in range(q + 1):
        value = data[idx + i]
        if value > total or pos[value] == -1:
            continue

        x = pos[value]
        left = 0
        right = len(tails)

        # plain lower_bound
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < x:
                left = mid + 1
            else:
                right = mid

        if left == len(tails):
            tails.append(x)
        else:
            tails[left] = x

    idx += q + 1
    out.append(f"Case {case}: {len(tails)}")

sys.stdout.write("\n".join(out) + "\n")
