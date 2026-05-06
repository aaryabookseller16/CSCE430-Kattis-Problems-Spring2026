import sys

raw = sys.stdin.buffer.read().split()

if not raw:
    sys.exit()

queries = []
top = 0

for item in raw:
    value = int(item)
    if value == 0:
        break
    queries.append(value)
    if value > top:
        top = value

if top < 25:
    for value in queries:
        sys.stdout.write(str(value) + " 0\n")
    sys.exit()

h_composite = bytearray(top + 1)

# first pass finds the numbers that are not H-prime
a = 5
while a <= top:
    b = a
    while a * b <= top:
        h_composite[a * b] = 1
        b += 4
    a += 4

h_primes = []
num = 5
while num <= top:
    if h_composite[num] == 0:
        h_primes.append(num)
    num += 4

semi = bytearray(top + 1)
left = 0

# second pass only uses the strange primes from this H-world
while left < len(h_primes):
    first = h_primes[left]
    right = left
    while right < len(h_primes) and first * h_primes[right] <= top:
        semi[first * h_primes[right]] = 1
        right += 1
    left += 1

count_so_far = 0
prefix = [0] * (top + 1)
walk = 1

while walk <= top:
    if semi[walk]:
        count_so_far += 1
    prefix[walk] = count_so_far
    walk += 1

out = []
for value in queries:
    out.append(str(value) + " " + str(prefix[value]))

sys.stdout.write("\n".join(out))
