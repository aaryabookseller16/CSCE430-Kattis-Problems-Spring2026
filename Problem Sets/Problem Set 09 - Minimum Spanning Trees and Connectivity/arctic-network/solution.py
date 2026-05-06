import sys
import heapq

data = sys.stdin.read().strip().split()
idx = 0

t = int(data[idx])
idx += 1

for _ in range(t):
    S = int(data[idx])  # satellite connections
    idx += 1

    P = int(data[idx])  # points
    idx += 1

    points = []

    for _ in range(P):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        points.append((x, y))

    if S >= P:
        print("0.00")
        continue

    graph = [[] for _ in range(P)]

    for i in range(P):
        x1, y1 = points[i]
        for j in range(i + 1, P):
            x2, y2 = points[j]
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

            graph[i].append((dist, j))
            graph[j].append((dist, i))

    visited = [False] * P
    heap = []
    mst = []

    visited[0] = True

    # every edge leaving 0 is a candidate
    for weight, neighbor in graph[0]:
        heapq.heappush(heap, (weight, neighbor))

    while heap and len(mst) < P - 1:
        weight, node = heapq.heappop(heap)  # take the smallest edge

        if visited[node]:  # if node is already in the tree, we dont need the edge
            continue

        visited[node] = True  # new node joins the MST
        mst.append(weight)  # so does the edge

        # all edges leaving the node are candidates
        for next_weight, neighbor in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(heap, (next_weight, neighbor))

    mst.sort()
    answer = mst[P - S - 1]
    print(f"{answer:.2f}")