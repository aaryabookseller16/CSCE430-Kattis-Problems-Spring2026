import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

p = int(data[0])  # number of data sets
idx = 1
out = []

for _ in range(p):
    k = int(data[idx])  # data set id
    idx += 1
    nums = list(map(int, data[idx:idx + 12]))
    idx += 12

    islands = 0
    n = len(nums)
    # try every subarray not touching the ends
    for l in range(1, n - 1):
        for r in range(l, n - 1):
            inside_min = min(nums[l:r + 1])
            if inside_min > nums[l - 1] and inside_min > nums[r + 1]:
                islands += 1

    out.append(f"{k} {islands}")

sys.stdout.write("\n".join(out))
