import sys

lines = sys.stdin.read().strip().splitlines()
if not lines:
    sys.exit()

out = []
for line in lines:
    n = int(line.split('/')[1])
    x = n
    exps = []
    p = 2
    while p * p <= x:
        c = 0
        while x % p == 0:
            x //= p
            c += 1
        if c:
            exps.append(c)
        p += 1
    if x > 1:
        exps.append(1)
    ways = 1  # divisor count of n^2
    for c in exps:
        ways *= 2 * c + 1
    ways = (ways + 1) // 2  # unordered pairs
    out.append(str(ways))

sys.stdout.write("\n".join(out))
