# Solution: Terrace Hill

## Goal
Solve the problem with monotonic stack. The implementation's main job is: The stack keeps decreasing heights. When the same height appears again with only lower terraces between, the bridge length is added.

## Key idea
The solution is built around monotonic stack. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The stack keeps decreasing heights. When the same height appears again with only lower terraces between, the bridge length is added.

## Step-by-step algorithm
1. Scan terrace heights from left to right.
2. Maintain a stack of heights in decreasing order, storing the last index for each height.
3. Pop smaller heights because a taller current terrace blocks their future bridge.
4. If the top stack height equals the current height, all terraces between are lower, so add the bridge length.
5. Update the last index for that height.
6. Otherwise push the current height and index.
7. Print the accumulated bridge length.

## Example walkthrough
Heights 5 3 2 3 allow a bridge between the two 3s over one lower terrace.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(n) memory.

## Important details
Taller terraces pop shorter ones because those shorter terraces cannot bridge past the taller point.
