import math
import sys

s = sys.stdin.buffer.read().strip()

if not s:
    sys.exit()

digits = len(s)

# small factorials are annoying because some have the same length
small = {
    b"1": "1",
    b"2": "2",
    b"6": "3",
    b"24": "4",
    b"120": "5",
    b"720": "6",
    b"5040": "7",
    b"40320": "8",
    b"362880": "9",
    b"3628800": "10",
}

if s in small:
    sys.stdout.write(small[s])
    sys.exit()

total = 0.0
ans = 1
made_digits = 1

# just count how many digits n! would have
while made_digits < digits:
    ans += 1
    total += math.log10(ans)
    made_digits = int(total) + 1

sys.stdout.write(str(ans))