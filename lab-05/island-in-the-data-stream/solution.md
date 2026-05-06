# Solution: Island in the Data Stream

## Goal
Solve the problem with brute-force subarray counting. The implementation's main job is: The code checks every interior subarray and counts it if every value inside is higher than both neighboring boundary values.

## Key idea
The solution is built around brute-force subarray counting. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code checks every interior subarray and counts it if every value inside is higher than both neighboring boundary values.

## Step-by-step algorithm
1. Read the dataset id and the 12 height values.
2. Try every subarray that does not touch the first or last value.
3. For a candidate subarray, find the minimum height inside it.
4. Compare that minimum with the height immediately before and after the subarray.
5. If the inside minimum is higher than both outside neighbors, count one island.
6. Print the dataset id and the island count.

## Example walkthrough
In 1 3 4 2, subarray 3 4 is an island because both values are above 1 and 2.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(12^3) per dataset as written, which is constant for the fixed 12 values; memory O(1).

## Important details
The first printed number is the dataset id.
