import sys

lines = sys.stdin.read().splitlines()

if len(lines) < 2:
    sys.exit(0)

message = lines[0].strip()
fragment = lines[1].strip()

n = len(message)
m = len(fragment)

if m > n:
    sys.stdout.write("0\n")
    sys.exit(0)

mod1 = 1000000007
mod2 = 1000000009
base = 911382323
inv1 = pow(base, mod1 - 2, mod1)
inv2 = pow(base, mod2 - 2, mod2)

frag1 = [0] * 26
frag2 = [0] * 26
pow1 = 1
pow2 = 1

for ch in fragment:
    idx = ord(ch) - 97
    frag1[idx] = (frag1[idx] + pow1) % mod1
    frag2[idx] = (frag2[idx] + pow2) % mod2
    pow1 = (pow1 * base) % mod1
    pow2 = (pow2 * base) % mod2

# same occurrence shapes means the strings are isomorphic
target = tuple(sorted((frag1[i], frag2[i]) for i in range(26)))

cur1 = [0] * 26
cur2 = [0] * 26
left1 = 1
left2 = 1
right1 = 1
right2 = 1

for i in range(m):
    idx = ord(message[i]) - 97
    cur1[idx] = (cur1[idx] + right1) % mod1
    cur2[idx] = (cur2[idx] + right2) % mod2
    right1 = (right1 * base) % mod1
    right2 = (right2 * base) % mod2

invpow1 = 1
invpow2 = 1
count = 0
pos = -1

for start in range(n - m + 1):
    now = tuple(sorted((cur1[i] * invpow1 % mod1, cur2[i] * invpow2 % mod2) for i in range(26)))

    if now == target:
        count += 1
        if pos == -1:
            pos = start

    if start == n - m:
        continue

    out_idx = ord(message[start]) - 97
    in_idx = ord(message[start + m]) - 97

    # drop the left char and add the new right char in absolute coordinates
    cur1[out_idx] = (cur1[out_idx] - left1) % mod1
    cur2[out_idx] = (cur2[out_idx] - left2) % mod2
    cur1[in_idx] = (cur1[in_idx] + right1) % mod1
    cur2[in_idx] = (cur2[in_idx] + right2) % mod2

    left1 = (left1 * base) % mod1
    left2 = (left2 * base) % mod2
    right1 = (right1 * base) % mod1
    right2 = (right2 * base) % mod2
    invpow1 = (invpow1 * inv1) % mod1
    invpow2 = (invpow2 * inv2) % mod2

if count == 1:
    sys.stdout.write(message[pos:pos + m] + "\n")
else:
    sys.stdout.write(str(count) + "\n")
