# Solution: Cookie Selection

## Goal
Solve the problem with two heaps for upper median. The implementation's main job is: The lower half is a max-heap and the upper half is a min-heap. The upper median is always the top of the upper heap.

## Key idea
The solution is built around two heaps for upper median. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The lower half is a max-heap and the upper half is a min-heap. The upper median is always the top of the upper heap.

## Step-by-step algorithm
1. Build the initial state and push every current candidate into a heap.
2. Each heap entry stores enough information to detect whether it is still current later.
3. Repeatedly pop the best candidate from the heap.
4. If the popped entry is stale, discard it and pop again.
5. Apply the chosen operation to the live data structure.
6. Update only the neighboring or affected candidates and push their new heap entries.
7. Continue until the required number of operations has been performed.

## Example walkthrough
With cookies 1,2,3,4, the upper median is 3.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(log n) per insert or # request; memory O(n).

## Important details
Rebalancing keeps high either equal size to low or one larger.
