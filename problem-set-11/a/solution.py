import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))

if data:
    test_cases = data[0]
    index = 1
    answers = []

    for _ in range(test_cases):
        n = data[index]
        index += 1

        start = data[index] - 1
        people = data[index + 1]
        limit = data[index + 2]
        index += 3

        medical_count = data[index]
        index += 1

        medical = []
        for _ in range(medical_count):
            medical.append(data[index] - 1)
            index += 1

        road_count = data[index]
        index += 1

        roads = []
        for _ in range(road_count):
            a = data[index] - 1
            b = data[index + 1] - 1
            capacity = data[index + 2]
            travel = data[index + 3]
            index += 4
            if travel <= limit:
                roads.append((a, b, capacity if capacity < people else people, travel))

        layers = limit + 1
        source = n * layers
        sink = source + 1
        node_count = sink + 1

        head = [-1] * node_count
        to = []
        cap = []
        nxt = []

        # connect the source to the starting location at time 0
        edge_index = len(to)
        to.append(start)
        cap.append(people)
        nxt.append(head[source])
        head[source] = edge_index
        to.append(source)
        cap.append(0)
        nxt.append(head[start])
        head[start] = edge_index + 1

        # waiting at a location for one more time step is always allowed
        for time in range(limit):
            current_base = time * n
            next_base = current_base + n

            for node in range(n):
                u = current_base + node
                v = next_base + node

                edge_index = len(to)
                to.append(v)
                cap.append(people)
                nxt.append(head[u])
                head[u] = edge_index
                to.append(u)
                cap.append(0)
                nxt.append(head[v])
                head[v] = edge_index + 1

        # each road can be entered by up to p people at every possible start time
        for a, b, capacity, travel in roads:
            for time in range(limit - travel + 1):
                u = time * n + a
                v = (time + travel) * n + b

                edge_index = len(to)
                to.append(v)
                cap.append(capacity)
                nxt.append(head[u])
                head[u] = edge_index
                to.append(u)
                cap.append(0)
                nxt.append(head[v])
                head[v] = edge_index + 1

        # reaching any medical facility at any time up to the limit is enough
        for location in medical:
            for time in range(layers):
                u = time * n + location

                edge_index = len(to)
                to.append(sink)
                cap.append(people)
                nxt.append(head[u])
                head[u] = edge_index
                to.append(u)
                cap.append(0)
                nxt.append(head[sink])
                head[sink] = edge_index + 1

        total_flow = 0

        # run Dinic on the time-expanded graph
        while total_flow < people:
            level = [-1] * node_count
            level[source] = 0
            queue = deque([source])

            while queue:
                u = queue.popleft()
                edge = head[u]

                while edge != -1:
                    v = to[edge]

                    if cap[edge] > 0 and level[v] == -1:
                        level[v] = level[u] + 1
                        if v == sink:
                            queue.clear()
                            break
                        queue.append(v)

                    edge = nxt[edge]

            if level[sink] == -1:
                break

            current = head[:]

            while total_flow < people:
                stack_nodes = [source]
                stack_edges = []
                path_cap = [people - total_flow]
                found_path = False

                while stack_nodes:
                    u = stack_nodes[-1]

                    if u == sink:
                        found_path = True
                        break

                    edge = current[u]

                    while edge != -1:
                        v = to[edge]

                        if cap[edge] > 0 and level[v] == level[u] + 1:
                            stack_edges.append(edge)
                            stack_nodes.append(v)

                            if path_cap[-1] < cap[edge]:
                                path_cap.append(path_cap[-1])
                            else:
                                path_cap.append(cap[edge])

                            break

                        edge = nxt[edge]

                    current[u] = edge

                    if edge != -1:
                        continue

                    stack_nodes.pop()

                    if not stack_edges:
                        continue

                    edge = stack_edges.pop()
                    path_cap.pop()
                    parent = stack_nodes[-1]
                    current[parent] = nxt[edge]

                if not found_path:
                    break

                pushed = path_cap[-1]
                total_flow += pushed

                for edge in stack_edges:
                    cap[edge] -= pushed
                    cap[edge ^ 1] += pushed

        answers.append(str(total_flow))

    sys.stdout.write("\n".join(answers))
