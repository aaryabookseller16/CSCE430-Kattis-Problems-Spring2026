from array import array

n,m,q = map(int,input().split())

strokes = []
tot = n*m
paint = array("H",[0]) * tot

# print("grid is", n, m, "with", q, "strokes")

for i in range(q):
    x1,y1,x2,y2 = map(int,input().split())
    strokes.append((x1,y1,x2,y2))

    if x1 == x2:
        base = (x1-1)*m
        y = y1
        while y <= y2:
            paint[base + y-1] = paint[base + y-1] + 1
            y = y + 1
    else:
        x = x1
        col = y1-1
        while x <= x2:
            paint[(x-1)*m + col] = paint[(x-1)*m + col] + 1
            x = x + 1

    # if i % 1000 == 0:
    #     print("read stroke", i)

parent = array("i", range(tot))
rank = bytearray(tot)
white = bytearray(tot)
parts = 0

i = 0
while i < tot:
    if paint[i] == 0:
        white[i] = 1
        parts = parts + 1
    i = i + 1

# print("white squares at end:", parts)

pos = 0
while pos < tot:
    if white[pos]:
        if pos % m != m-1 and white[pos+1]:
            a = pos
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            b = pos+1
            while parent[b] != b:
                parent[b] = parent[parent[b]]
                b = parent[b]
            if a != b:
                if rank[a] < rank[b]:
                    parent[a] = b
                elif rank[a] > rank[b]:
                    parent[b] = a
                else:
                    parent[b] = a
                    rank[a] = rank[a] + 1
                parts = parts - 1

        if pos + m < tot and white[pos+m]:
            a = pos
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            b = pos+m
            while parent[b] != b:
                parent[b] = parent[parent[b]]
                b = parent[b]
            if a != b:
                if rank[a] < rank[b]:
                    parent[a] = b
                elif rank[a] > rank[b]:
                    parent[b] = a
                else:
                    parent[b] = a
                    rank[a] = rank[a] + 1
                parts = parts - 1
    pos = pos + 1

ans = [0]*q
turn = q-1

while turn >= 0:
    ans[turn] = parts
    x1,y1,x2,y2 = strokes[turn]

    # undoing one line from the painting
    if x1 == x2:
        x = x1
        y = y1
        while y <= y2:
            spot = (x-1)*m + y-1
            paint[spot] = paint[spot] - 1

            if paint[spot] == 0:
                white[spot] = 1
                parts = parts + 1

                around = []
                if spot % m != 0:
                    around.append(spot-1)
                if spot % m != m-1:
                    around.append(spot+1)
                if spot >= m:
                    around.append(spot-m)
                if spot + m < tot:
                    around.append(spot+m)
                for other in around:
                    ok = True
                    if other < 0 or other >= tot:
                        ok = False
                    if ok and other == spot-1 and spot % m == 0:
                        ok = False
                    if ok and other == spot+1 and spot % m == m-1:
                        ok = False

                    if ok and white[other]:
                        a = spot
                        while parent[a] != a:
                            parent[a] = parent[parent[a]]
                            a = parent[a]
                        b = other
                        while parent[b] != b:
                            parent[b] = parent[parent[b]]
                            b = parent[b]

                        if a != b:
                            if rank[a] < rank[b]:
                                parent[a] = b
                            elif rank[a] > rank[b]:
                                parent[b] = a
                            else:
                                parent[b] = a
                                rank[a] = rank[a] + 1
                            parts = parts - 1
            y = y + 1
    else:
        x = x1
        y = y1
        while x <= x2:
            spot = (x-1)*m + y-1
            paint[spot] = paint[spot] - 1

            if paint[spot] == 0:
                white[spot] = 1
                parts = parts + 1

                around = []
                if spot % m != 0:
                    around.append(spot-1)
                if spot % m != m-1:
                    around.append(spot+1)
                if spot >= m:
                    around.append(spot-m)
                if spot + m < tot:
                    around.append(spot+m)
                for other in around:
                    ok = True
                    if other < 0 or other >= tot:
                        ok = False
                    if ok and other == spot-1 and spot % m == 0:
                        ok = False
                    if ok and other == spot+1 and spot % m == m-1:
                        ok = False

                    if ok and white[other]:
                        a = spot
                        while parent[a] != a:
                            parent[a] = parent[parent[a]]
                            a = parent[a]
                        b = other
                        while parent[b] != b:
                            parent[b] = parent[parent[b]]
                            b = parent[b]

                        if a != b:
                            if rank[a] < rank[b]:
                                parent[a] = b
                            elif rank[a] > rank[b]:
                                parent[b] = a
                            else:
                                parent[b] = a
                                rank[a] = rank[a] + 1
                            parts = parts - 1
            x = x + 1

    # print("after undo", turn, "parts", parts)
    turn = turn - 1

for x in ans:
    print(x)
