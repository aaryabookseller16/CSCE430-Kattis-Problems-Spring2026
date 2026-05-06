# Solution: Minimum Scalar Product

## Goal
Solve the problem with greedy sorting by rearrangement inequality. The implementation's main job is: To minimize the sum of products, pair the smallest values of one vector with the largest values of the other.

## Key idea
The solution is built around greedy sorting by rearrangement inequality. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: To minimize the sum of products, pair the smallest values of one vector with the largest values of the other.

## Step-by-step algorithm
1. Read both vectors.
2. Sort the first vector in increasing order.
3. Sort the second vector in decreasing order.
4. Pair elements at the same index after those two sorts.
5. Multiply each pair and add it to the total.
6. Print the total with the case number.

## Example walkthrough
Pairing [-5,1,3] with [10,2,-1] in opposite order reduces the total.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n) per case; memory O(n).

## Important details
The output follows Google Code Jam style Case #x.
