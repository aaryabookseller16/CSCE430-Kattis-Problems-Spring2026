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

        # make the four corners after rotating the board clockwise
        for a in [-0.5, 0.5]:
            for b in [-0.5, 0.5]:
                px = a * w
                py = b * h
                nx = x + px * c + py * s
                ny = y - px * s + py * c
                points.append((nx, ny))

        # print("last board corners:", points[-4:])

    points = sorted(set(points))

    low = []
    for p in points:
        while len(low) >= 2:
            a = low[-2]
            b = low[-1]
            turn = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
            if turn <= 1e-10:
                low.pop()
            else:
                break
        low.append(p)

    up = []
    for p in reversed(points):
        while len(up) >= 2:
            a = up[-2]
            b = up[-1]
            turn = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
            if turn <= 1e-10:
                up.pop()
            else:
                break
        up.append(p)

    hull = low[:-1] + up[:-1]

    mould_area = 0.0
    for i in range(len(hull)):
        j = (i + 1) % len(hull)
        mould_area += hull[i][0] * hull[j][1] - hull[j][0] * hull[i][1]

    mould_area = abs(mould_area) / 2.0

    # print("used:", board_area, "mould:", mould_area)
    print(f"{board_area / mould_area * 100:.1f} %")
