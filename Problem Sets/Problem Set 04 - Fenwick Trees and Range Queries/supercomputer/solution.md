# Solution: Supercomputer

## Goal
Solve the problem with Fenwick tree for bit flips and range sums. The implementation's main job is: The array starts all zero. Flipping a bit updates the Fenwick tree by +1 or -1, and count queries use prefix sums.

## Key idea
The solution is built around Fenwick tree for bit flips and range sums. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The array starts all zero. Flipping a bit updates the Fenwick tree by +1 or -1, and count queries use prefix sums.

## Step-by-step algorithm
1. Create a Fenwick tree, or one Fenwick tree per category.
2. Initialize the tree with the starting array values or counts.
3. For point updates, add the difference at the affected index.
4. For prefix sums, walk down the Fenwick tree accumulating stored values.
5. For a range query, compute prefix(right) - prefix(left-1).
6. Combine category counts with current values if the query asks for weighted sums.
7. Print one line for every query that asks for output.

## Example walkthrough
If bit 5 flips from 0 to 1, add +1 at index 5; range [3,7] uses prefix(7)-prefix(2).

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(log n) per operation and O(n) memory.

## Important details
A bytearray stores the current bit state.
