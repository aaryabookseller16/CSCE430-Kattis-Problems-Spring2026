import sys

lines = sys.stdin.read().splitlines()
out = []

mod1 = 1000000007
mod2 = 1000000009
base = 911382323

for raw in lines:
    if raw == "":
        break

    s = raw.replace(" ", "")
    n = len(s)

    if n == 0:
        out.append("")
        continue

    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)
    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)

    for i in range(n):
        code = ord(s[i]) - 64
        pref1[i + 1] = (pref1[i] * base + code) % mod1
        pref2[i + 1] = (pref2[i] * base + code) % mod2
        pow1[i + 1] = (pow1[i] * base) % mod1
        pow2[i + 1] = (pow2[i] * base) % mod2

    for length in range(1, n + 1):
        seen = {}
        best = 1

        for start in range(n - length + 1):
            h1 = (pref1[start + length] - pref1[start] * pow1[length]) % mod1
            h2 = (pref2[start + length] - pref2[start] * pow2[length]) % mod2
            key = (h1, h2)

            if key in seen:
                seen[key] += 1
            else:
                seen[key] = 1

            if seen[key] > best:
                best = seen[key]

        if best == 1:
            out.append("")
            break

        out.append(str(best))

if out:
    sys.stdout.write("\n".join(out) + "\n")
