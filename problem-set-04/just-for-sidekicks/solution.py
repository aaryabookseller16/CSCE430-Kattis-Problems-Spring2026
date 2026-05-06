import sys

inp = sys.stdin.buffer
line = inp.readline().split()
if not line:
    sys.exit()
n = int(line[0])
q = int(line[1])
values = list(map(int, inp.readline().split()))
types_line = inp.readline().strip().decode()
types = [int(ch) for ch in types_line]

bit = [[0] * (n + 2) for _ in range(6)]

def add(tree, i, delta):
    # basic fenwick update
    while i <= n:
        tree[i] += delta
        i += i & -i

def prefix(tree, i):
    # fenwick prefix sum
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s

# build counts for each type
for idx, t in enumerate(types, 1):
    add(bit[t - 1], idx, 1)

out_lines = []
for _ in range(q):
    parts = inp.readline().split()
    if not parts:
        break
    kind = int(parts[0])
    if kind == 1:
        # change gem type
        k = int(parts[1])
        new_t = int(parts[2])
        old_t = types[k - 1]
        if old_t != new_t:
            add(bit[old_t - 1], k, -1)
            add(bit[new_t - 1], k, 1)
            types[k - 1] = new_t
    elif kind == 2:
        # change value for a type
        p = int(parts[1])
        v = int(parts[2])
        values[p - 1] = v
    else:
        # query total value in range
        l = int(parts[1])
        r = int(parts[2])
        total = 0
        for t in range(6):
            cnt = prefix(bit[t], r) - prefix(bit[t], l - 1)
            total += cnt * values[t]
        out_lines.append(str(total))

sys.stdout.write("\n".join(out_lines))
