import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if not data:
    sys.exit(0)

n = data[0]
cards = data[1:1 + n]

best = 0.0
running = 0

# try taking only a prefix
for i in range(n):
    running += cards[i]
    avg = running / (i + 1)
    if avg > best:
        best = avg

running = 0

# try taking only a suffix
for taken in range(1, n + 1):
    running += cards[n - taken]
    avg = running / taken
    if avg > best:
        best = avg

sys.stdout.write(f"{best:.10f}\n")
