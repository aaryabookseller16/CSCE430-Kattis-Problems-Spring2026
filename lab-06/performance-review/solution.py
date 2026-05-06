import sys
sys.setrecursionlimit(1_000_000)

nums = list(map(int, sys.stdin.read().split()))
if not nums:
    sys.exit(0)

n = nums[0]
manager, rank, cost = [], [], []
idx = 1
for _ in range(n):
    m, r, t = nums[idx], nums[idx + 1], nums[idx + 2]
    manager.append(m)
    rank.append(r)
    cost.append(t)
    idx += 3

# build children lists 
children = [[] for _ in range(n)]
root = -1
for i, m in enumerate(manager):
    if m == -1:
        root = i  # director sits at the top
    else:
        children[m - 1].append(i)  # ids are 1-based in input

tin = [0] * n
tout = [0] * n
order = []

def dfs(u):
    # simple Euler tour to map subtree -> [tin, tout]
    tin[u] = len(order)
    order.append(u)
    for v in children[u]:
        dfs(v)
    tout[u] = len(order) - 1

dfs(root)

class Fenwick:
    def __init__(self, size):
        self.n = size
        self.bit = [0] * (size + 1)

    def add(self, idx, delta):
        i = idx + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum_prefix(self, idx):
        res = 0
        i = idx + 1
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        if r < l:
            return 0
        return self.sum_prefix(r) - (self.sum_prefix(l - 1) if l > 0 else 0)

# sort employees by rank so we add lower ranks first
nodes_by_rank = sorted(range(n), key=lambda x: rank[x])
bit = Fenwick(n)
ans = [0] * n

i = 0
while i < n:
    r_val = rank[nodes_by_rank[i]]
    j = i
    # first compute answers for this rank using only lower ranks in the tree
    while j < n and rank[nodes_by_rank[j]] == r_val:
        u = nodes_by_rank[j]
        ans[u] = bit.range_sum(tin[u], tout[u])
        j += 1
    # now add this rank's nodes for higher ranks to see
    k = i
    while k < j:
        u = nodes_by_rank[k]
        bit.add(tin[u], cost[u])
        k += 1
    i = j

sys.stdout.write("\n".join(str(x) for x in ans))
