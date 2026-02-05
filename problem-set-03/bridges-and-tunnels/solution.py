import sys


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Path compression to find the root of a given node
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unify(self, a: int, b: int) -> int: # union operation
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return ra
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return ra

    def component_size(self, x: int) -> int:
        return self.size[self.find(x)]


def parse_inputs():
    input = sys.stdin.readline
    first = input().strip()
    if not first:
        return 0, []

    n = int(first)
    pairs = [tuple(input().split()) for _ in range(n)]
    return n, pairs


def main() -> None:
    n, pairs = parse_inputs()
    if n == 0:
        return

    uf = UnionFind(2 * n + 5)

    # We don't know building names ahead of time, so we map each name -> integer id.
    name_to_id = {}
    # Next id to hand out when we see a new building name.
    next_id = 0

    # output sys
    out_lines = []

    for a, b in pairs:
        # If we've never seen this building name before, assign it a new id.
        if a not in name_to_id:
            name_to_id[a] = next_id
            next_id += 1
        if b not in name_to_id:
            name_to_id[b] = next_id
            next_id += 1

        ida = name_to_id[a]
        idb = name_to_id[b]
        
        # Build the new bridge/tunnel by unifying the two endpoints.
        root = uf.unify(ida, idb)
        
        # the number of reachable buildings is just the size
        # of the connected component containing that bridge.
        out_lines.append(str(uf.size[root]))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
