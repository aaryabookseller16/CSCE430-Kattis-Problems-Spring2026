# Solution: Guess the Data Structure

## Goal
Solve the problem with parallel simulation of stack, queue, and max-heap. The implementation's main job is: The code keeps all three candidate structures alive until an output contradicts one.

## Key idea
The solution is built around parallel simulation of stack, queue, and max-heap. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code keeps all three candidate structures alive until an output contradicts one.

## Step-by-step algorithm
1. Build the initial state and push every current candidate into a heap.
2. Each heap entry stores enough information to detect whether it is still current later.
3. Repeatedly pop the best candidate from the heap.
4. If the popped entry is stale, discard it and pop again.
5. Apply the chosen operation to the live data structure.
6. Update only the neighboring or affected candidates and push their new heap entries.
7. Continue until the required number of operations has been performed.

## Example walkthrough
If the next removed value is the most recently inserted one, stack remains possible; otherwise it is ruled out.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n) because priority queue operations use a heap; memory O(n).

## Important details
At the end, zero, one, or many possible structures decide the printed answer.
