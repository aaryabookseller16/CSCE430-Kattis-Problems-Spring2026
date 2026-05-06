# Solution: Polyline Simplification

## Goal
Solve the problem with priority queue with lazy updates and a linked list. The implementation's main job is: Each removable point is keyed by the area of the triangle formed with its current neighbors. The smallest area point is removed, and only its two neighbors need new areas.

## Key idea
The solution is built around priority queue with lazy updates and a linked list. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Each removable point is keyed by the area of the triangle formed with its current neighbors. The smallest area point is removed, and only its two neighbors need new areas.

## Step-by-step algorithm
1. Build the initial state and push every current candidate into a heap.
2. Each heap entry stores enough information to detect whether it is still current later.
3. Repeatedly pop the best candidate from the heap.
4. If the popped entry is stale, discard it and pop again.
5. Apply the chosen operation to the live data structure.
6. Update only the neighboring or affected candidates and push their new heap entries.
7. Continue until the required number of operations has been performed.

## Example walkthrough
If points 4, 5, and 6 almost form a straight line, point 5 has tiny triangle area and is removed early.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O((n-m) log n) time and O(n) memory.

## Important details
Version numbers discard stale heap entries after neighboring points change.

## Other implementations in this folder
- `solution_slow.md` has its own markdown explanation.
