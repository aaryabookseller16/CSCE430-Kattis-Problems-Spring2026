import sys
from collections import Counter

data = sys.stdin.read().strip().splitlines()
if not data:
    sys.exit()

n = int(data[0])
dom = data[1:1 + n]
kattis = data[1 + n:1 + 2 * n]

count_dom = Counter(dom)
count_kattis = Counter(kattis)

matches = 0
for word, cnt in count_dom.items():
    if word in count_kattis:
        # overlap between the two counts
        common = cnt if cnt < count_kattis[word] else count_kattis[word]
        matches += common

print(matches)
