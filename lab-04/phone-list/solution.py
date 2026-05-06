import sys

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit(0)

t = int(data[0])
ptr = 1
out = []

for _ in range(t):
    n = int(data[ptr])
    ptr += 1

    nums = data[ptr:ptr + n]
    ptr += n

    # keeping union-find arrays
    uf_parent = list(range(n))
    uf_size = [1] * n

    # sort so we only cechk small before big
    nums.sort()
    bad = False

    for i in range(n - 1):
        a = nums[i]
        b = nums[i + 1]

        # prefix conflict found
        if b.startswith(a):
            # find root of i
            x = i
            while uf_parent[x] != x:
                uf_parent[x] = uf_parent[uf_parent[x]]
                x = uf_parent[x]
            rx = x

            # find root of i+1
            x = i + 1
            while uf_parent[x] != x:
                uf_parent[x] = uf_parent[uf_parent[x]]
                x = uf_parent[x]
            ry = x

            # union by size
            if rx != ry:
                if uf_size[rx] < uf_size[ry]:
                    rx, ry = ry, rx
                uf_parent[ry] = rx
                uf_size[rx] += uf_size[ry]

            # bad pair invalidates it
            bad = True
            break

    if bad:
        out.append("NO")
    else:
        out.append("YES")
sys.stdout.write("\n".join(out))
