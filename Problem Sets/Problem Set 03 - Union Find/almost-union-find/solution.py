import sys


class AlmostUnionFind:
    def __init__(self, n: int, max_ops: int):
        total = n + max_ops + 5

        self.parent = list(range(total))
        self.size = [0] * total
        self.sum = [0] * total

        # pos[p] = current node id that represents element p in the DSU.
        self.pos = [0] * (n + 1)

        # Initialize each element as its own set.
        for p in range(1, n + 1):
            self.pos[p] = p
            self.size[p] = 1
            self.sum[p] = p

        # Next available node id for "moved" elements.
        self.next_id = n + 1

    def find(self, x: int) -> int:
        # Standard path compression find.
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def _union_roots(self, ra: int, rb: int) -> None:
        # Union by size. Assumes ra and rb are roots already.
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.sum[ra] += self.sum[rb]

    def union(self, p: int, q: int) -> None:
        # Merge the sets containing p and q.
        self._union_roots(self.find(self.pos[p]), self.find(self.pos[q]))

    def move(self, p: int, q: int) -> None:
        # Move p into q's set. If already same set, do nothing.
        rp = self.find(self.pos[p])
        rq = self.find(self.pos[q])
        if rp == rq:
            return

        # Remove p's contribution from its old root.
        self.size[rp] -= 1
        self.sum[rp] -= p

        # Create a brand new node to represent p in its new home.
        new_id = self.next_id
        self.next_id += 1

        self.pos[p] = new_id
        self.parent[new_id] = new_id
        self.size[new_id] = 1
        self.sum[new_id] = p

        # Attach the new node to q's set.
        self._union_roots(new_id, rq)

    def query(self, p: int) -> tuple[int, int]:
        # Return (size, sum) for the set containing p.
        r = self.find(self.pos[p])
        return self.size[r], self.sum[r]


def accept_input() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    # Convert all tokens to ints
    nums = list(map(int, data))
    out_lines = []

    i = 0
    n_nums = len(nums)

    while i < n_nums:
        n = nums[i]
        m = nums[i + 1]
        i += 2

        # Fresh DSU per test case.
        uf = AlmostUnionFind(n, m)

        for _ in range(m):
            op = nums[i]
            i += 1
            if op == 1:
                # Union
                p = nums[i]
                q = nums[i + 1]
                i += 2
                uf.union(p, q)
            elif op == 2:
                # Move
                p = nums[i]
                q = nums[i + 1]
                i += 2
                uf.move(p, q)
            else:
                # Query
                p = nums[i]
                i += 1
                cnt, total = uf.query(p)
                out_lines.append(f"{cnt} {total}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    accept_input()
