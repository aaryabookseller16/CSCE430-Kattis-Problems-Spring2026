import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

n = int(data[0])
ships = int(data[1])
finn = list(map(int, data[2:2 + n]))

finn.sort()  # beat cheapest systems first

wins = 0
for need in finn:
    if ships > need:
        wins += 1
        ships -= need + 1  # spend one more than Finn
    else:
        break

print(wins)
