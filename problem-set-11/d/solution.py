import sys
from collections import deque

tokens = sys.stdin.buffer.read().split()
index = 0
answers = []

while index < len(tokens):
    n = int(tokens[index])
    m = int(tokens[index + 1])
    s = int(tokens[index + 2])
    v = int(tokens[index + 3])
    index += 4

    gophers = []
    for _ in range(n):
        x = float(tokens[index])
        y = float(tokens[index + 1])
        index += 2
        gophers.append((x, y))

    holes = []
    for _ in range(m):
        x = float(tokens[index])
        y = float(tokens[index + 1])
        index += 2
        holes.append((x, y))

    # a gopher can use a hole if it can reach it within s seconds
    limit = float(s * v)
    limit_squared = limit * limit
    graph = [[] for _ in range(n)]

    for gopher in range(n):
        gx, gy = gophers[gopher]

        for hole in range(m):
            hx, hy = holes[hole]
            dx = gx - hx
            dy = gy - hy

            if dx * dx + dy * dy <= limit_squared + 1e-9:
                graph[gopher].append(hole)

    # repeatedly find augmenting paths in the bipartite graph
    match_hole = [-1] * m
    saved = 0

    for start in range(n):
        prev_gopher = [-1] * n
        prev_hole = [-1] * m
        queue = deque([start])
        prev_gopher[start] = -2
        free_hole = -1

        while queue and free_hole == -1:
            gopher = queue.popleft()

            for hole in graph[gopher]:
                if prev_hole[hole] != -1:
                    continue

                prev_hole[hole] = gopher

                if match_hole[hole] == -1:
                    free_hole = hole
                    break

                next_gopher = match_hole[hole]

                if prev_gopher[next_gopher] == -1:
                    prev_gopher[next_gopher] = hole
                    queue.append(next_gopher)

        if free_hole == -1:
            continue

        saved += 1
        hole = free_hole

        while True:
            gopher = prev_hole[hole]
            previous_hole = prev_gopher[gopher]
            match_hole[hole] = gopher

            if previous_hole == -2:
                break

            hole = previous_hole

    answers.append(str(n - saved))

sys.stdout.write("\n".join(answers))
