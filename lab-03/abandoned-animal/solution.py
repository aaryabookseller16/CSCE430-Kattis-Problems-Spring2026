# accept input
import sys
from bisect import bisect_left, bisect_right

line = sys.stdin.readline().strip()
number_of_stores = int(line) #N
K = int(sys.stdin.readline().strip())
stores = [set() for _ in range(number_of_stores)] # list of sets

item_to_stores = {}
for _ in range(K):
    parts = sys.stdin.readline().strip().split()
    i = int(parts[0])
    item = parts[1]
    stores[i].add(item)
    item_to_stores.setdefault(item, []).append(i)

# sort store lists once for fast binary search
for lst in item_to_stores.values():
    lst.sort()

number_of_items_bought = int(sys.stdin.readline().strip()) #M
purchases = [] #what items she bought

for _ in range(number_of_items_bought):
    purchases.append(sys.stdin.readline().strip())
    
# print("N =", number_of_stores)
# print("Stores =", stores)
# print("M =", number_of_items_bought)
# print("Purchases =", purchases)

#logic
#if she bought nothing, there isn't really a path to check
if number_of_items_bought == 0:
    print("impossible")
    sys.exit(0)

# earliest possible stores
earliest = []
prev_store = -1
for item in purchases:
    lst = item_to_stores.get(item)
    if not lst:
        print("impossible")
        sys.exit(0)
    idx = bisect_left(lst, prev_store)
    if idx == len(lst):
        print("impossible")
        sys.exit(0)
    prev_store = lst[idx]
    earliest.append(prev_store)

#  latest possible stores (from the end)
latest = [0] * number_of_items_bought
next_store = number_of_stores  # upper bound (>= max store index)
for i in range(number_of_items_bought - 1, -1, -1):
    item = purchases[i]
    lst = item_to_stores[item]
    idx = bisect_right(lst, next_store) - 1
    if idx < 0:
        print("impossible")
        sys.exit(0)
    next_store = lst[idx]
    latest[i] = next_store

if earliest == latest:
    print("unique")
else:
    print("ambiguous")
