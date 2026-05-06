# Solution: Mr. Plow King

## Goal
Solve the problem with combinatorial greedy counting. The implementation's main job is: The code assigns labels so cheap labels are wasted inside cycles whenever possible, forcing the spanning tree labels to be as expensive as possible.

## Key idea
The solution is built around combinatorial greedy counting. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code assigns labels so cheap labels are wasted inside cycles whenever possible, forcing the spanning tree labels to be as expensive as possible.

## Step-by-step algorithm
1. Compute how many upgraded edges are extra beyond the n-1 edges needed for connectivity.
2. Imagine growing a connected component one city at a time.
3. Each time a new city must be connected, the current label is forced into the spanning tree cost.
4. After that, spend as many cheap labels as possible on cycle edges that do not help the spanning tree.
5. The number of such cycle edges available grows with the size of the already connected component.
6. Continue until all cities are connected.
7. Print the total label cost forced into Mr. Plow's MST.

## Example walkthrough
After connecting a new city, extra edges among already connected cities can consume low labels.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(1) memory.

## Important details
extra = m-(n-1) counts how many upgraded roads do not need to be in the spanning tree.
