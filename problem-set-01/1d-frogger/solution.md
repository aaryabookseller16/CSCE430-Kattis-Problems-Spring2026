# Solution: 1-D Frogger

## Goal
Solve the problem with direct simulation with cycle detection. The implementation's main job is: The frog follows board jumps until it hits magic, falls left/right, or revisits a square.

## Key idea
The solution is built around direct simulation with cycle detection. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The frog follows board jumps until it hits magic, falls left/right, or revisits a square.

## Step-by-step algorithm
1. Generate values in order while recording the first index where each value appeared.
2. If N values are generated before a repeat, count the values directly.
3. If a repeat appears, split the generated list into a prefix and a cycle.
4. Count the prefix once.
5. Add full-cycle repetitions using integer division.
6. Add the leftover cycle prefix using the remainder.
7. Process the counted values in sorted order for the final greedy calculation.

## Example walkthrough
If square 2 contains -1, the next hop goes one square left.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(number of visited squares), at most O(n); memory O(n).

## Important details
The code uses 0-based indexes internally while input start is 1-based.
