import sys

line = sys.stdin.readline

first = line().strip()
if not first:
    sys.exit(0)

n = int(first)
lo = 1
hi = n

for _ in range(16):
    if lo == hi:
        sys.stdout.write(f"A {lo}\n")
        sys.stdout.flush()
        sys.exit(0)

    next_lo = max(1, lo - 1)
    next_hi = min(n, hi + 1)
    length = next_hi - next_lo + 1

    if length == 2:
        # just tell the two landing spots apart
        sys.stdout.write(f"Q {next_hi} {next_hi} {next_lo} {next_lo}\n")
        sys.stdout.flush()

        reply = line().split()
        if not reply:
            sys.exit(0)
        u1 = int(reply[0])
        u2 = int(reply[1])
        if u1 < 0 or u2 < 0:
            sys.exit(0)

        if u1 == 1:
            lo = next_hi
            hi = next_hi
        else:
            lo = next_lo
            hi = next_lo
        continue

    if length == 3:
        # three spots fit in three different answers
        mid = next_lo + 1
        sys.stdout.write(f"Q {mid} {next_hi} {next_hi} {next_hi}\n")
        sys.stdout.flush()

        reply = line().split()
        if not reply:
            sys.exit(0)
        u1 = int(reply[0])
        u2 = int(reply[1])
        if u1 < 0 or u2 < 0:
            sys.exit(0)

        if u1 == 0 and u2 == 0:
            lo = next_lo
            hi = next_lo
        elif u1 == 1 and u2 == 0:
            lo = mid
            hi = mid
        else:
            lo = next_hi
            hi = next_hi
        continue

    base = length // 4
    extra = length % 4
    sizes = [base, base, base, base]

    for i in range(extra):
        sizes[i] += 1

    a0 = next_lo
    b0 = a0 + sizes[0] - 1
    a1 = b0 + 1
    b1 = a1 + sizes[1] - 1
    a2 = b1 + 1
    b2 = a2 + sizes[2] - 1
    a3 = b2 + 1
    b3 = next_hi

    # 00, 10, 11, 01 line up with the four chunks
    sys.stdout.write(f"Q {a1} {b2} {a2} {b3}\n")
    sys.stdout.flush()

    reply = line().split()
    if not reply:
        sys.exit(0)
    u1 = int(reply[0])
    u2 = int(reply[1])
    if u1 < 0 or u2 < 0:
        sys.exit(0)

    if u1 == 0 and u2 == 0:
        lo = a0
        hi = b0
    elif u1 == 1 and u2 == 0:
        lo = a1
        hi = b1
    elif u1 == 1 and u2 == 1:
        lo = a2
        hi = b2
    else:
        lo = a3
        hi = b3

sys.stdout.write(f"A {lo}\n")
sys.stdout.flush()
