import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if data:
    n = data[0]
    m = data[1]

    # just make the graph with edge ids so we can mark bridges later
    graph = [[] for _ in range(n)]
    pos = 2

    for edge_id in range(m):
        u = data[pos]
        v = data[pos + 1]
        pos += 2

        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))

    tin = [-1] * n
    low = [0] * n
    parent = [-1] * n
    parent_edge = [-1] * n
    next_edge = [0] * n
    is_bridge = [False] * m

    timer = 0
    stack = [0]

    # iterative dfs so the whole thing stays in one script
    while stack:
        node = stack[-1]

        if tin[node] == -1:
            tin[node] = timer
            low[node] = timer
            timer += 1

        if next_edge[node] < len(graph[node]):
            neighbor, edge_id = graph[node][next_edge[node]]
            next_edge[node] += 1

            if edge_id == parent_edge[node]:
                continue

            if tin[neighbor] == -1:
                parent[neighbor] = node
                parent_edge[neighbor] = edge_id
                stack.append(neighbor)
            else:
                # found a way back up, so this can help low-link
                low[node] = min(low[node], tin[neighbor])
        else:
            stack.pop()

            if parent[node] != -1:
                prev = parent[node]
                low[prev] = min(low[prev], low[node])

                # if child can't get back above parent, this edge is a bridge
                if low[node] > tin[prev]:
                    is_bridge[parent_edge[node]] = True

    # now walk from 0 again, but pretend all bridges are gone
    safe_count = 0
    seen = [False] * n
    stack = [0]
    seen[0] = True

    while stack:
        node = stack.pop()
        safe_count += 1

        for neighbor, edge_id in graph[node]:
            if is_bridge[edge_id] or seen[neighbor]:
                continue

            seen[neighbor] = True
            stack.append(neighbor)

    sys.stdout.write(str(safe_count))
