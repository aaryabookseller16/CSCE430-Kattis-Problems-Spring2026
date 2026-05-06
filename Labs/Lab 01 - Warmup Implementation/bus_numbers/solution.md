# Solution: Bus Numbers

## Goal
Solve the problem with sorting and run compression. The implementation's main job is: Sorted bus numbers are grouped into consecutive runs. Runs of length at least 3 are printed as a-b; shorter runs print individually.

## Key idea
The solution is built around sorting and run compression. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Sorted bus numbers are grouped into consecutive runs. Runs of length at least 3 are printed as a-b; shorter runs print individually.

## Step-by-step algorithm
1. Read and sort the bus numbers.
2. Start a new run only when the previous number is not present.
3. Extend the run while the next consecutive number exists.
4. Store each complete consecutive run.
5. When printing, compress runs of length at least 3 as start-end.
6. Print runs of length 1 or 2 as individual numbers.
7. Join all printed pieces with spaces.

## Example walkthrough
141 142 143 becomes 141-143, but 10 11 stays 10 11.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n) time and O(n) memory.

## Important details
A set is used to find where each run starts and ends.
