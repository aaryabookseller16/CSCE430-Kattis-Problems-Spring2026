import sys

lines = sys.stdin.buffer.read().splitlines()

if lines:
    n = int(lines[0])
    spoken = []
    understood = []

    for i in range(1, n + 1):
        parts = lines[i].decode().split()
        language = parts[1]
        spoken.append(language)
        known = set(parts[1:])
        understood.append(known)

    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]

    # person j can receive messages from person i if j understands i's spoken language
    for i in range(n):
        language = spoken[i]

        for j in range(n):
            if language in understood[j]:
                graph[i].append(j)
                reverse_graph[j].append(i)

    visited = [False] * n
    order = []

    # first pass of Kosaraju to get nodes in reverse finishing order
    for start in range(n):
        if visited[start]:
            continue

        stack = [(start, 0)]
        visited[start] = True

        while stack:
            node, next_index = stack[-1]

            if next_index == len(graph[node]):
                order.append(node)
                stack.pop()
                continue

            neighbor = graph[node][next_index]
            stack[-1] = (node, next_index + 1)

            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append((neighbor, 0))

    largest = 0
    assigned = [False] * n

    # second pass finds the size of each strongly connected component
    for start in reversed(order):
        if assigned[start]:
            continue

        size = 0
        stack = [start]
        assigned[start] = True

        while stack:
            node = stack.pop()
            size += 1

            for neighbor in reverse_graph[node]:
                if not assigned[neighbor]:
                    assigned[neighbor] = True
                    stack.append(neighbor)

        if size > largest:
            largest = size

    sys.stdout.write(str(n - largest))
