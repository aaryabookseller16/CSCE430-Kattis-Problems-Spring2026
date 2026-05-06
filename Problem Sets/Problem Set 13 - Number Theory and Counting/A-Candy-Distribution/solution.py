tests = int(input())
biggest = float("inf")

for case in range(tests):
    k, c = map(int, input().split())
    # print("case", case, "k/c:", k, c)
    if c == 1: #if we onlu have one candy, we need to take one bag, and that bag can't be empty
        bags = k + 1
        if bags <= biggest:
            print(bags)
        else:
            print("IMPOSSIBLE")
    elif k == 1: #one kid can use one bag, and that bag can have any number of candies, so we just need to make sure we don't have more than one bag
        print(1)
    else:
        r1 = c
        r2 = k
        x1 = 1
        x2 = 0
        while r2 != 0:
            q = r1 // r2
            temp = r1 - q * r2
            r1 = r2
            r2 = temp
            temp = x1 - q * x2
            x1 = x2
            x2 = temp
            # print("gcd step:", r1, r2, x1, x2)

        if r1 != 1:
            print("IMPOSSIBLE")
        else:
            bags = x1 % k
            if bags == 0:
                bags = bags + k
            if bags <= biggest:
                print(bags)
            else:
                print("IMPOSSIBLE")
