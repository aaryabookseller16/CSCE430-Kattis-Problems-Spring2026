import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

n = int(data[0])
heights = list(map(int, data[1:1 + n]))

left_high = [0] * n
best_left = 0
for i in range(n):
    # tallest we saw so far on the left
    left_high[i] = best_left
    if heights[i] > best_left:
        best_left = heights[i]

right_high = [0] * n
best_right = 0
for i in range(n - 1, -1, -1):
    # tallest we saw so far on the right
    right_high[i] = best_right
    if heights[i] > best_right:
        best_right = heights[i]

max_jump = 0
for i in range(n):
    # bridge height is limited by the shorter side
    lower_side = left_high[i]
    if right_high[i] < lower_side:
        lower_side = right_high[i]
    if lower_side > heights[i]:
        jump = lower_side - heights[i]
        if jump > max_jump:
            max_jump = jump

print(max_jump)
