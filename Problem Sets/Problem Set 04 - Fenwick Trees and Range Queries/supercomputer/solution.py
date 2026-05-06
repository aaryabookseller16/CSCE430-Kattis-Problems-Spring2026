import sys

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit()

n = int(data[0])
q = int(data[1])
ops = data[2:]

bit = [0] * (n + 2)
state = bytearray(n + 1)  # 0/1 for each position

def add(i, delta):
    # fenwick add
    while i <= n:
        bit[i] += delta
        i += i & -i

def prefix(i):
    # fenwick sum
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

out = []
idx = 0
for _ in range(q):
    cmd = ops[idx].decode()
    if cmd == 'F':
        pos = int(ops[idx + 1])
        if state[pos]:
            state[pos] = 0
            add(pos, -1)
        else:
            state[pos] = 1
            add(pos, 1)
        idx += 2
    else:  # C query
        l = int(ops[idx + 1])
        r = int(ops[idx + 2])
        out.append(str(prefix(r) - prefix(l - 1)))
        idx += 3

sys.stdout.write("\n".join(out))
