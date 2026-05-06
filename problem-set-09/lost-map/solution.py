import sys
from array import array

input = sys.stdin.readline

line = input().strip()

if line:
    n = int(line)

    dist = []
    for _ in range(n):
        # using a 64-bit array keeps memory down without risking overflow on bigger distances
        dist.append(array('Q', map(int, input().split())))

    used = [False] * n
    best = [10**18] * n
    parent = [-1] * n

    best[0] = 0
    answer = []

    # this is just Prim on the complete graph whose edge weights are the table values
    for _ in range(n):
        node = -1

        for i in range(n):
            if used[i]:
                continue
            if node == -1 or best[i] < best[node]:
                node = i

        used[node] = True

        if parent[node] != -1:
            # print villages 1-based like the statement wants
            answer.append(str(parent[node] + 1) + " " + str(node + 1))

        row = dist[node]

        # now this node can maybe give cheaper ways to attach everybody else
        for neighbor in range(n):
            if used[neighbor]:
                continue
            if row[neighbor] < best[neighbor]:
                best[neighbor] = row[neighbor]
                parent[neighbor] = node

    sys.stdout.write("\n".join(answer))
