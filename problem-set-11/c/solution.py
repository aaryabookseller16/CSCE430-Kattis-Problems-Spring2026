import sys
from collections import deque

lines = sys.stdin.buffer.read().splitlines()

if lines:
    index = 0

    while index < len(lines) and not lines[index].strip():
        index += 1

    test_cases = int(lines[index])
    index += 1
    outputs = []

    for _ in range(test_cases):
        while index < len(lines) and not lines[index].strip():
            index += 1

        resident_count = int(lines[index])
        index += 1

        people = []
        person_party = []
        person_clubs = []
        parties = {}
        clubs = {}
        club_names = []

        for _ in range(resident_count):
            while index < len(lines) and not lines[index].strip():
                index += 1

            parts = lines[index].decode().split()
            index += 1

            name = parts[0]
            party = parts[1]
            count = int(parts[2])
            memberships = parts[3:3 + count]

            person_id = len(people)
            people.append(name)
            person_clubs.append(memberships)

            if party not in parties:
                parties[party] = len(parties)
            person_party.append(parties[party])

            for club in memberships:
                if club not in clubs:
                    clubs[club] = len(clubs)
                    club_names.append(club)

        club_count = len(clubs)
        party_count = len(parties)
        person_count = len(people)

        source = 0
        party_base = 1
        person_base = party_base + party_count
        club_base = person_base + person_count
        sink = club_base + club_count
        node_count = sink + 1

        head = [-1] * node_count
        to = []
        cap = []
        nxt = []

        # add source to party edges with the party limit
        if club_count == 0:
            party_limit = 0
        else:
            party_limit = (club_count - 1) // 2

        for party_id in range(party_count):
            u = source
            v = party_base + party_id
            edge = len(to)
            to.append(v)
            cap.append(party_limit)
            nxt.append(head[u])
            head[u] = edge
            to.append(u)
            cap.append(0)
            nxt.append(head[v])
            head[v] = edge + 1

        # each person belongs to exactly one party and can represent at most one club
        for person_id in range(person_count):
            u = party_base + person_party[person_id]
            v = person_base + person_id
            edge = len(to)
            to.append(v)
            cap.append(1)
            nxt.append(head[u])
            head[u] = edge
            to.append(u)
            cap.append(0)
            nxt.append(head[v])
            head[v] = edge + 1

        # a person can represent any club they belong to
        person_club_edges = []

        for person_id in range(person_count):
            u = person_base + person_id

            for club in person_clubs[person_id]:
                v = club_base + clubs[club]
                edge = len(to)
                to.append(v)
                cap.append(1)
                nxt.append(head[u])
                head[u] = edge
                to.append(u)
                cap.append(0)
                nxt.append(head[v])
                head[v] = edge + 1
                person_club_edges.append((edge, person_id, clubs[club]))

        # each club needs exactly one representative
        for club_id in range(club_count):
            u = club_base + club_id
            v = sink
            edge = len(to)
            to.append(v)
            cap.append(1)
            nxt.append(head[u])
            head[u] = edge
            to.append(u)
            cap.append(0)
            nxt.append(head[v])
            head[v] = edge + 1

        flow = 0

        # run Dinic
        while True:
            level = [-1] * node_count
            level[source] = 0
            queue = deque([source])

            while queue:
                node = queue.popleft()
                edge = head[node]

                while edge != -1:
                    neighbor = to[edge]

                    if cap[edge] > 0 and level[neighbor] == -1:
                        level[neighbor] = level[node] + 1
                        queue.append(neighbor)

                    edge = nxt[edge]

            if level[sink] == -1:
                break

            it = head[:]

            while True:
                stack_nodes = [source]
                stack_edges = []
                path_cap = [club_count - flow]
                found = False

                while stack_nodes:
                    node = stack_nodes[-1]

                    if node == sink:
                        found = True
                        break

                    edge = it[node]

                    while edge != -1:
                        neighbor = to[edge]

                        if cap[edge] > 0 and level[neighbor] == level[node] + 1:
                            stack_edges.append(edge)
                            stack_nodes.append(neighbor)

                            if path_cap[-1] < cap[edge]:
                                path_cap.append(path_cap[-1])
                            else:
                                path_cap.append(cap[edge])

                            break

                        edge = nxt[edge]

                    it[node] = edge

                    if edge != -1:
                        continue

                    stack_nodes.pop()

                    if not stack_edges:
                        continue

                    last_edge = stack_edges.pop()
                    path_cap.pop()
                    parent = stack_nodes[-1]
                    it[parent] = nxt[last_edge]

                if not found:
                    break

                pushed = path_cap[-1]
                flow += pushed

                for edge in stack_edges:
                    cap[edge] -= pushed
                    cap[edge ^ 1] += pushed

                if flow == club_count:
                    break

            if flow == club_count:
                break

        if flow != club_count:
            outputs.append("Impossible.")
            continue

        answer = []

        for edge, person_id, club_id in person_club_edges:
            if cap[edge] == 0:
                answer.append(people[person_id] + " " + club_names[club_id])

        answer.sort(key=lambda item: item.split()[1])
        outputs.append("\n".join(answer))

    sys.stdout.write("\n\n".join(outputs))
