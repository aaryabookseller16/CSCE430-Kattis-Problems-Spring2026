import math

n = int(input())

for i in range(n):

    data = input().split()
    k = int(data[0])
    ax = float(data[1])
    ay = float(data[2])
    bx = float(data[3])
    by = float(data[4])
    cx = float(data[5])
    cy = float(data[6])
    # side opposite A is BC, opposite B is CA, opposite C is AB
    a = math.sqrt((bx - cx) ** 2 + (by - cy) ** 2)
    b = math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
    c = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
    # first brocard point weights, order matters
    wa = c * c * a * a
    wb = a * a * b * b
    wc = b * b * c * c
    total = wa + wb + wc

    x = (wa * ax + wb * bx + wc * cx) / total
    y = (wa * ay + wb * by + wc * cy) / total

    # print("debug:", k, a, b, c, wa, wb, wc)
    print(k, "{:.6f}".format(x), "{:.6f}".format(y))