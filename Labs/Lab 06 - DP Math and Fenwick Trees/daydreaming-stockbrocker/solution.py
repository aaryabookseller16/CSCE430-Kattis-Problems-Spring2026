import sys


data = list(map(int, sys.stdin.read().split()))

n = data[0]
prices = data[1:1 + n]

money = 100  # she shows up with a hundred bucks
shares = 0
cap = 100000  # can't own more than this many shares

for i in range(n - 1):
    today = prices[i]
    tomorrow = prices[i + 1]
    # buy low, sell high
    if tomorrow > today:
        can_buy = min(cap - shares, money // today) # int divisiion
        money -= can_buy * today
        shares += can_buy
    elif tomorrow < today:
        money += shares * today
        shares = 0

money += shares * prices[-1]
print(money)

