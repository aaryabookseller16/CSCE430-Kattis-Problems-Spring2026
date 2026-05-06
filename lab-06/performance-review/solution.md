# Solution: Performance Review

## Goal
Solve the problem with Euler tour plus Fenwick tree sorted by rank. The implementation's main job is: A subtree becomes a contiguous Euler interval. Employees are processed by increasing rank; the Fenwick tree contains costs of strictly lower-ranked employees.

## Key idea
The solution is built around Euler tour plus Fenwick tree sorted by rank. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: A subtree becomes a contiguous Euler interval. Employees are processed by increasing rank; the Fenwick tree contains costs of strictly lower-ranked employees.

## Step-by-step algorithm
1. Create a Fenwick tree, or one Fenwick tree per category.
2. Initialize the tree with the starting array values or counts.
3. For point updates, add the difference at the affected index.
4. For prefix sums, walk down the Fenwick tree accumulating stored values.
5. For a range query, compute prefix(right) - prefix(left-1).
6. Combine category counts with current values if the query asks for weighted sums.
7. Print one line for every query that asks for output.

## Example walkthrough
For a manager, querying its subtree interval sums lower-ranked employee costs inside that subtree.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n) time and O(n) memory.

## Important details
Equal ranks are queried before being added, so they do not count each other.
