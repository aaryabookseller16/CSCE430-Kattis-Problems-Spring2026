import sys

lines = sys.stdin.read().strip().splitlines()
if not lines:
    sys.exit()

n = int(lines[0])
stmts = [line.strip() for line in lines[1:]]

# grab words
words = []
parsed = []
for s in stmts:
    a, rel, b = s.split()
    words.append(a)
    words.append(b)
    parsed.append((a, rel, b))

words = list(dict.fromkeys(words))  # keep unique
idx = {w: i for i, w in enumerate(words)}
cnt = len(words)

parent = list(range(cnt))
size = [1] * cnt

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

# store suffixes
len_arr = [len(w) for w in words]
suf1 = [w[-1:] for w in words]
suf2 = [w[-2:] if len(w) >= 2 else "" for w in words]
suf3 = [w[-3:] if len(w) >= 3 else "" for w in words]

# buckets for rhyme unions
bucket1 = {}
bucket2 = {}
bucket3 = {}
for i, w in enumerate(words):
    bucket1.setdefault(suf1[i], []).append(i)
    if len_arr[i] >= 2:
        bucket2.setdefault(suf2[i], []).append(i)
    if len_arr[i] >= 3:
        bucket3.setdefault(suf3[i], []).append(i)

# union by suffix length =1 if there's a len1 word present
for suf, lst in bucket1.items():
    has_len1 = any(len_arr[i] == 1 for i in lst)
    if has_len1:
        root = lst[0]
        for i in lst[1:]:
            unite(root, i)

# union by suffix length =2 if there's a len2 word present
for suf, lst in bucket2.items():
    has_len2 = any(len_arr[i] == 2 for i in lst)
    if has_len2:
        root = lst[0]
        for i in lst[1:]:
            unite(root, i)

# union by suffix length =3 among len>=3 words
for suf, lst in bucket3.items():
    if len(lst) > 1:
        root = lst[0]
        for i in lst[1:]:
            unite(root, i)

# union explicit "is"
for a, rel, b in parsed:
    if rel == "is":
        unite(idx[a], idx[b])

# check contradictions
ok = True
for a, rel, b in parsed:
    if rel == "is":
        if find(idx[a]) != find(idx[b]):
            ok = False
            break
    else:  # not
        if find(idx[a]) == find(idx[b]):
            ok = False
            break

print("yes" if ok else "wait what?")
