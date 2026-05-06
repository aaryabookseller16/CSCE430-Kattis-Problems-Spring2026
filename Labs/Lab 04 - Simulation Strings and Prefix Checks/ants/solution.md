# Solution: Ants

## Goal
Solve the problem with min/max fall time observation. The implementation's main job is: Because ants swapping directions is equivalent to passing through each other, earliest time uses each ant nearest end, latest uses farthest end.

## Key idea
The solution is built around min/max fall time observation. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Because ants swapping directions is equivalent to passing through each other, earliest time uses each ant nearest end, latest uses farthest end.

## Step-by-step algorithm
1. Read pole length and ant positions.
2. For each ant, compute distance to the left end and right end.
3. For the earliest all-fall time, this ant can head toward the closer end.
4. For the latest all-fall time, this ant can head toward the farther end.
5. Take the maximum earliest value over all ants.
6. Take the maximum latest value over all ants.
7. Print both values.

## Example walkthrough
An ant at 3 on a pole of 10 can fall in 3 seconds earliest or 7 seconds latest.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(a) per test case; memory O(1).

## Important details
The answer is the max over all ants for earliest and latest scenarios.
