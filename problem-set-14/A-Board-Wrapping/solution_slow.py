import math

t = int(input())

for case in range(t):
    n = int(input())
    points = []
    board_area = 0.0

    for i in range(n):
        x, y, w, h, v = map(float, input().split())
        board_area += w * h
        ang = math.radians(v)
        c = math.cos(ang)
        s = math.sin(ang)

        for a in [-0.5, 0.5]:
            for b in [-0.5, 0.5]:
                px = a * w
                py = b * h
                points.append((x + px * c + py * s, y - px * s + py * c))
        # print("corners so far:", points)
    points = sorted(set(points))

    start = 0
    for i in range(len(points)):
        if points[i][0] < points[start][0] or (points[i][0] == points[start][0] and points[i][1] < points[start][1]):
            start = i

    hull = []
    here = start

    while True:
        hull.append(points[here])

        nxt = 0
        if nxt == here:
            nxt = 1

        for i in range(len(points)):
            if i == here:
                continue
            a = points[here]
            b = points[nxt]
            c = points[i]
            turn = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
            old_dist = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
            new_dist = (c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2

            if turn < -1e-10 or (abs(turn) <= 1e-10 and new_dist > old_dist):
                nxt = i
        here = nxt
        if here == start:
            break
    mould_area = 0.0
    for i in range(len(hull)):
        j = (i + 1) % len(hull)
        mould_area += hull[i][0] * hull[j][1] - hull[j][0] * hull[i][1]
    mould_area = abs(mould_area) / 2.0

    # print("slow hull:", hull)
    print(f"{board_area / mould_area * 100:.1f} %")
