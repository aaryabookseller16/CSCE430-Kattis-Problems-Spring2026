import sys

first = input().strip()
if not first:
    sys.exit(0)

total_candies_str, num_children_str = first.split()
total_candies = int(total_candies_str)
num_children = int(num_children_str)

wish = []
for _ in range(num_children):
    wish.append(int(input()))

total_wish = sum(wish)
total_deprivation = total_wish - total_candies

if total_deprivation <= 0:
    print(0)
    sys.exit(0)

# Sort wishes to perform water-filling with caps.
wish.sort()

anger = 0
level = 0
remaining = num_children
idx = 0
D = total_deprivation

# Raise the equal deprivation level until we run out of D or hit caps.
while idx < num_children:
    next_level = wish[idx]
    gap = next_level - level
    if gap == 0:
        # This child is already capped at the current level.
        anger += next_level * next_level
        idx += 1
        remaining -= 1
        continue

    cost = gap * remaining
    if D >= cost:
        D -= cost
        level = next_level
        # All children with wish == level are now capped.
        while idx < num_children and wish[idx] == level:
            anger += level * level
            idx += 1
            remaining -= 1
        continue

    # Not enough D to reach the next cap: distribute evenly at this stage.
    add = D // remaining
    rem = D % remaining
    level += add
    # remaining children: rem get level+1, rest get level
    anger += rem * (level + 1) * (level + 1)
    anger += (remaining - rem) * level * level
    D = 0
    break

if D == 0:
    print(anger)
    sys.exit(0)

print(anger)
