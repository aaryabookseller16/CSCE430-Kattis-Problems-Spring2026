import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if data:
    test_cases = data[0]
    index = 1
    answers = []

    for _ in range(test_cases):
        n = data[index]
        m = data[index + 1]
        index += 2

        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]

        for _ in range(m):
            a = data[index] - 1
            b = data[index + 1] - 1
            index += 2
            graph[a].append(b)
            reverse_graph[b].append(a)

        visited = [False] * n
        order = []

        # first pass of Kosaraju to get reverse finishing order
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

        component = [-1] * n
        component_count = 0

        # second pass finds all strongly connected components
        for start in reversed(order):
            if component[start] != -1:
                continue

            stack = [start]
            component[start] = component_count

            while stack:
                node = stack.pop()

                for neighbor in reverse_graph[node]:
                    if component[neighbor] == -1:
                        component[neighbor] = component_count
                        stack.append(neighbor)

            component_count += 1

        if component_count == 1:
            answers.append("0")
            continue

        indegree = [0] * component_count
        outdegree = [0] * component_count

        # build degrees in the condensation graph
        for node in range(n):
            current_component = component[node]

            for neighbor in graph[node]:
                next_component = component[neighbor]

                if current_component != next_component:
                    outdegree[current_component] += 1
                    indegree[next_component] += 1

        sources = 0
        sinks = 0

        for node in range(component_count):
            if indegree[node] == 0:
                sources += 1
            if outdegree[node] == 0:
                sinks += 1

        if sources > sinks:
            answers.append(str(sources))
        else:
            answers.append(str(sinks))

    sys.stdout.write("\n".join(answers))
