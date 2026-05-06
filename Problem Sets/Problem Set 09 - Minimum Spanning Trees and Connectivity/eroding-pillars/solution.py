import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if data:
    n = data[0]

    x = [0]
    y = [0]
    pos = 1

    for _ in range(n):
        x.append(data[pos])
        y.append(data[pos + 1])
        pos += 2

    total = n + 1

    # the answer has to be one of the actual pair distances, so just collect those
    vals = []
    for i in range(total):
        for j in range(i + 1, total):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            vals.append(dx * dx + dy * dy)

    vals.sort()

    # remove duplicates so the binary search has fewer things to check
    unique_vals = []
    last = -1
    for d in vals:
        if d != last:
            unique_vals.append(d)
            last = d

    vals = unique_vals

    left = 0
    right = len(vals) - 1

    while left < right:
        mid = (left + right) // 2
        limit2 = vals[mid]

        graph = [[] for _ in range(total)]

        # build the graph for this jump distance
        for i in range(total):
            for j in range(i + 1, total):
                dx = x[i] - x[j]
                dy = y[i] - y[j]

                if dx * dx + dy * dy <= limit2:
                    graph[i].append(j)
                    graph[j].append(i)

        tin = [-1] * total
        low = [0] * total
        parent = [-1] * total
        next_edge = [0] * total

        timer = 0
        stack = [0]
        bad = False

        # if some pillar becomes an articulation point, then anything behind it is a problem
        while stack:
            node = stack[-1]

            if tin[node] == -1:
                tin[node] = timer
                low[node] = timer
                timer += 1

            if next_edge[node] < len(graph[node]):
                neighbor = graph[node][next_edge[node]]
                next_edge[node] += 1

                if neighbor == parent[node]:
                    continue

                if tin[neighbor] == -1:
                    parent[neighbor] = node
                    stack.append(neighbor)
                else:
                    if tin[neighbor] < low[node]:
                        low[node] = tin[neighbor]
            else:
                stack.pop()

                if parent[node] != -1:
                    prev = parent[node]

                    if low[node] < low[prev]:
                        low[prev] = low[node]

                    # node's parent is only bad if it is a pillar, not the starting rock
                    if prev != 0 and low[node] >= tin[prev]:
                        bad = True
                        break

        ok = not bad

        # also need every pillar to be reachable in the first place
        if ok:
            for time_seen in tin:
                if time_seen == -1:
                    ok = False
                    break

        if ok:
            right = mid
        else:
            left = mid + 1

    sys.stdout.write(str(vals[left] ** 0.5))
