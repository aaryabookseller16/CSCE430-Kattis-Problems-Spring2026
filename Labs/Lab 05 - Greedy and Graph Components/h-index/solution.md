# Solution: H-Index

## Goal
Solve the problem with sorting and scan. The implementation's main job is: After sorting citations descending, the largest index i with citations[i] >= i is the H-index.

## Key idea
The solution is built around sorting and scan. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: After sorting citations descending, the largest index i with citations[i] >= i is the H-index.

## Step-by-step algorithm
1. Read all citation counts.
2. Sort citations from largest to smallest.
3. Scan with 1-based index i, meaning the first i papers are the current candidate set.
4. If citations[i] is at least i, update the H-index to i.
5. As soon as citations[i] is below i, no later paper can rescue a larger H-index.
6. Print the largest valid i.

## Example walkthrough
Citations 7,5,2,1,1 give H=2 because two papers have at least two citations.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n) time and O(n) memory.

## Important details
The scan stops once the condition fails.
