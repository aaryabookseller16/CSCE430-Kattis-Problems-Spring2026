import sys
import math

MOD = 1000000007

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)

k = data[0]
n = data[1]

if n == 1:
    sys.stdout.write(str(k) + "\n")
    sys.exit(0)

base = [[0] * k for _ in range(k)]

for i in range(k):
    for j in range(k):
        if math.gcd(i + 1, j + 1) == 1:
            base[i][j] = 1  # these two heights can sit next to each other

vec = [1] * k  # one way to end at each height with just one dune
power = n - 1

while power > 0:
    if power & 1:
        new_vec = [0] * k
        for i in range(k):
            if vec[i] == 0:
                continue
            cur = vec[i]
            row = base[i]
            for j in range(k):
                if row[j]:
                    new_vec[j] = (new_vec[j] + cur * row[j]) % MOD
        vec = new_vec

    power >>= 1
    if power == 0:
        break

    new_base = [[0] * k for _ in range(k)]
    for i in range(k):
        row_i = base[i]
        new_row = new_base[i]
        for m in range(k):
            if row_i[m] == 0:
                continue
            cur = row_i[m]
            row_m = base[m]
            for j in range(k):
                if row_m[j]:
                    new_row[j] = (new_row[j] + cur * row_m[j]) % MOD
    base = new_base

ans = sum(vec) % MOD
sys.stdout.write(str(ans) + "\n")
