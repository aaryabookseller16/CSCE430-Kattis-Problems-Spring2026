# Solution: Bungee Builder

## Goal
Solve the problem with prefix/suffix maxima. The implementation's main job is: For each valley, the best bridge height is limited by the shorter tallest mountain on its left and right. The largest positive drop is the answer.

## Key idea
The solution is built around prefix/suffix maxima. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: For each valley, the best bridge height is limited by the shorter tallest mountain on its left and right. The largest positive drop is the answer.

## Step-by-step algorithm
1. Read all mountain heights.
2. Build left_high[i], the tallest mountain strictly to the left of i.
3. Build right_high[i], the tallest mountain strictly to the right of i.
4. For each mountain i, the bridge height is limited by min(left_high[i], right_high[i]).
5. If that limit is above height[i], the jump distance is limit - height[i].
6. Keep the largest such jump over all mountains.
7. Print that maximum, or 0 if none exists.

## Example walkthrough
Heights 5 1 4 allow a jump of min(5,4)-1 = 3 at the middle mountain.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(n) memory.

## Important details
No valid positive drop gives answer 0.
