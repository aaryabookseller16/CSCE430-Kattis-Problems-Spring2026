class UnionFind:
    """
    Disjoint Set Union (Union-Find) with:
      - Union by size (attach smaller tree under larger tree)
      - Path compression (flatten trees during find)
    """

    def __init__(self, n: int):
        # n = number of elements (we assume elements are labeled 0..n-1)
        if n <= 0:
            raise ValueError("Size <= 0 is not allowed")

        self._n = n                       # total number of elements
        self._components = n              # number of disjoint sets currently

        # parent[i] = parent pointer of i
        # if parent[i] == i, then i is the root (representative) of its set
        self.parent = list(range(n))

        # size[i] = size of the component ONLY if i is a root
        # (we will keep size[non_root] = 0 to mirror your Java code)
        self.size = [1] * n

    def find(self, x: int) -> int:
        """
        Return the root (representative) of the set containing x.
        Uses iterative path compression.
        """

        # -------- Step 1: climb parent pointers until we reach the root --------
        root = x
        while root != self.parent[root]: # a root cannot be its own parent in a union operation
            root = self.parent[root]

        # -------- Step 2: path compression (flatten path x -> root) --------
        # Walk again from x up to root, rewriting each node's parent to root.
        while x != root:
            nxt = self.parent[x]          # save where x was pointing (so we don't lose the path)
            self.parent[x] = root         # make x point directly to the root
            x = nxt                       # move upward one step

        return root

    def connected(self, a: int, b: int) -> bool:
        """
        Two elements are connected iff they have the same root.
        """
        return self.find(a) == self.find(b)

    def component_size(self, x: int) -> int:
        """
        Size of the set containing x.
        We look up size at the root only.
        """
        return self.size[self.find(x)]

    def num_components(self) -> int:
        """
        Number of disjoint sets currently.
        """
        return self._components

    def unify(self, a: int, b: int) -> None:
        """
        Merge the sets containing a and b.
        If already in the same set, do nothing.
        """

        # -------- Step 1: find the roots (representatives) --------
        root_a = self.find(a)
        root_b = self.find(b)

        # -------- Step 2: if roots match, they are already unified --------
        if root_a == root_b:
            return

        # -------- Step 3: union by size (attach smaller root under larger root) --------
        if self.size[root_a] < self.size[root_b]:
            # Attach A's tree under B's root
            self.parent[root_a] = root_b              # root_a is no longer a root
            self.size[root_b] += self.size[root_a]    # update B's component size
            self.size[root_a] = 0                     # optional cleanup (non-root size = 0)
        else:
            # Attach B's tree under A's root
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
            self.size[root_b] = 0

        # -------- Step 4: merging two components reduces component count by 1 --------
        self._components -= 1