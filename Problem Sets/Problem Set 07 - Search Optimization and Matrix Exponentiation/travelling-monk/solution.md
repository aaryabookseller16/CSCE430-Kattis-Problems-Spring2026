# Solution: Travelling Monk

## Goal
Solve the problem with binary search on meeting time. The implementation's main job is: The ascent height is nondecreasing and the descent height is nonincreasing. The earliest meeting time is where ascent height catches descent height.

## Key idea
The solution is built around binary search on meeting time. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The ascent height is nondecreasing and the descent height is nonincreasing. The earliest meeting time is where ascent height catches descent height.

## Step-by-step algorithm
1. Choose the answer value to binary search.
2. Set lower and upper bounds that definitely contain the answer.
3. Write a feasibility check for a guessed value.
4. Try the middle value.
5. If the guess works, keep the lower half; otherwise keep the upper half.
6. Repeat until the bounds meet.
7. Print the final bound as the smallest feasible answer.

## Example walkthrough
If the monk climbs from 0 to 10 while the other trip descends from 10 to 0, binary search finds the crossing time.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O((a+d) + iterations * pointer movement) time; memory O(a+d).

## Important details
Piecewise linear interpolation handles rests and varying speeds.
