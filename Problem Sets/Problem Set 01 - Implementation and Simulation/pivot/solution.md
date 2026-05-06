# Solution: Pivot

## Goal
Solve the problem with prefix maxima and suffix minima. The implementation's main job is: A value can be the pivot if every value left of it is smaller and every value right of it is larger. The code precomputes those two facts.

## Key idea
The solution is built around prefix maxima and suffix minima. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: A value can be the pivot if every value left of it is smaller and every value right of it is larger. The code precomputes those two facts.

## Step-by-step algorithm
1. Read the array.
2. Build left_max_at_idx[i], the largest value strictly left of i.
3. Build right_min_at_idx[i], the smallest value strictly right of i.
4. For each position i, check left_max_at_idx[i] < A[i] < right_min_at_idx[i].
5. If true, A[i] could be the partition pivot.
6. Count and print all such positions.

## Example walkthrough
In 2 1 3 4 7 5 6 8, value 4 works because left max is 3 and right min is 5.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(n) memory.

## Important details
The input numbers are distinct, so strict comparisons are enough.
