while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    seen = {}
    x = a
    step = 0
    # print("starting a side", a)

    while True:
        seen[x] = step
        if x == 1:
            break
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1
        step = step + 1
        # if step % 50 == 0:
        #     print("a side step", step, x)
    y = b
    bsteps = 0
    # print("starting b side", b)
    while y not in seen:
        if y % 2 == 0:
            y = y // 2
        else:
            y = 3*y + 1
        bsteps = bsteps + 1
        # if bsteps % 50 == 0:
        #     print("b side step", bsteps, y)

    print(str(a) + " needs " + str(seen[y]) + " steps, " + str(b) + " needs " + str(bsteps) + " steps, they meet at " + str(y))
