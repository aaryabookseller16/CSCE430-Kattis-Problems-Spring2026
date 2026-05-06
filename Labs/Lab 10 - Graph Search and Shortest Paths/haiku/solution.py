import sys

lines = sys.stdin.buffer.read().splitlines()
if not lines:
    sys.exit(0)

s = int(lines[0])
poem = lines[-3:]

# the statement and samples disagree on line breaks, so accept both styles
syllables = b" ".join(lines[1:-3]).split()[:s]

# bucket syllables by first letter so we do less matching work
by_first = [[] for _ in range(26)]
for syllable in syllables:
    by_first[syllable[0] - 97].append(syllable)

targets = (5, 7, 5)
is_haiku = True

for line_index in range(3):
    line = poem[line_index]
    target = targets[line_index]
    limit_mask = (1 << (target + 1)) - 1

    # bit k means we can reach this spot using exactly k syllables
    dp = [0] * (len(line) + 1)
    dp[0] = 1

    for i in range(len(line)):
        mask = dp[i]
        if not mask:
            continue

        if line[i] == 32:
            dp[i + 1] |= mask
            continue

        for syllable in by_first[line[i] - 97]:
            if line.startswith(syllable, i):
                dp[i + len(syllable)] |= (mask << 1) & limit_mask

    if not (dp[len(line)] >> target) & 1:
        is_haiku = False
        break

sys.stdout.write("haiku\n" if is_haiku else "come back next year\n")
