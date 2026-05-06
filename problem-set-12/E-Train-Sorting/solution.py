import sys

data = sys.stdin.buffer.read().split()

if not data:
    sys.exit(0)

n = int(data[0])
weights = [int(x) for x in data[1:1 + n]]

inc = [1] * n
dec = [1] * n

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        # bigger cars can keep growing the front side
        if weights[j] > weights[i] and inc[j] + 1 > inc[i]:
            inc[i] = inc[j] + 1
        # smaller cars can keep growing the back side
        if weights[j] < weights[i] and dec[j] + 1 > dec[i]:
            dec[i] = dec[j] + 1

answer = 0

for i in range(n):
    # car i is the first car we decide to keep
    length = inc[i] + dec[i] - 1
    if length > answer:
        answer = length

sys.stdout.write(str(answer) + "\n")
