import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if data:
    pos = 0
    n = data[pos]
    pos += 1
    m = data[pos]
    pos += 1
    p = data[pos]
    pos += 1

    insecure = [False] * (n + 1)

    for _ in range(p):
        insecure[data[pos]] = True
        pos += 1

    secure_count = 0
    for building in range(1, n + 1):
        if insecure[building] is False:
            secure_count += 1

    secure_edges = []
    best_insecure = [10**18] * (n + 1)

    for _ in range(m):
        a = data[pos]
        b = data[pos + 1]
        w = data[pos + 2]
        pos += 3

        if insecure[a] is False and insecure[b] is False:
            secure_edges.append((w, a, b))
        elif insecure[a] and (insecure[b] is False):
            if w < best_insecure[a]:
                best_insecure[a] = w
        elif insecure[b] and (insecure[a] is False):
            if w < best_insecure[b]:
                best_insecure[b] = w

    total_cost = 0
    possible = True

    # every insecure building has to hang off the secure part like a leaf
    for building in range(1, n + 1):
        if insecure[building]:
            if best_insecure[building] == 10**18:
                possible = False
                break
            total_cost += best_insecure[building]

    if possible:
        secure_edges.sort()

        parent = list(range(n + 1))
        size = [1] * (n + 1)
        used_secure_edges = 0

        # now just connect all secure buildings as cheaply as possible
        for w, a, b in secure_edges:
            ra = a
            while ra != parent[ra]:
                ra = parent[ra]

            rb = b
            while rb != parent[rb]:
                rb = parent[rb]

            if ra == rb:
                continue

            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]
            total_cost += w
            used_secure_edges += 1

            if used_secure_edges == secure_count - 1:
                break

        if used_secure_edges != secure_count - 1:
            possible = False

    if possible:
        sys.stdout.write(str(total_cost))
    else:
        sys.stdout.write("impossible")
