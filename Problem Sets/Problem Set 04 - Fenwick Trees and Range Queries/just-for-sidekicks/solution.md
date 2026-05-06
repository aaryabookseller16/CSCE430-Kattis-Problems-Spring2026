# Solution: Just for Sidekicks

## Goal
Solve the problem with Fenwick trees by gem type. The implementation's main job is: Six Fenwick trees store counts of each gem type by position. Type-change queries update two trees; value-change queries only update the value table.

## Key idea
The solution is built around Fenwick trees by gem type. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Six Fenwick trees store counts of each gem type by position. Type-change queries update two trees; value-change queries only update the value table.

## Step-by-step algorithm
1. Create a Fenwick tree, or one Fenwick tree per category.
2. Initialize the tree with the starting array values or counts.
3. For point updates, add the difference at the affected index.
4. For prefix sums, walk down the Fenwick tree accumulating stored values.
5. For a range query, compute prefix(right) - prefix(left-1).
6. Combine category counts with current values if the query asks for weighted sums.
7. Print one line for every query that asks for output.

## Example walkthrough
For a range [L,R], count type 1 gems, multiply by value 1, and repeat for all six types.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(log n) for type updates, O(1) for value updates, and O(6 log n) for range queries; memory O(6n).

## Important details
This separates positions from values cleanly.
