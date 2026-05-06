# Solution: Phone List

## Goal
Solve the problem with sorting and prefix check. The implementation's main job is: Phone numbers are sorted lexicographically. If any number is a prefix of the next number, the list is inconsistent.

## Key idea
The solution is built around sorting and prefix check. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Phone numbers are sorted lexicographically. If any number is a prefix of the next number, the list is inconsistent.

## Step-by-step algorithm
1. Map each value in the first sequence to its position.
2. Scan the second sequence and keep only values that also appear in the first sequence.
3. Replace each kept value by its first-sequence position.
4. Run the standard LIS tail-array algorithm on those positions.
5. Use binary search to update the first tail value that is not smaller.
6. The number of tails is the length of the longest common valid route.
7. Print that length in the required format.

## Example walkthrough
After sorting, 911 appears directly before 91125426, so the prefix conflict is easy to detect.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n + total digits) time and O(n) memory.

## Important details
The union-find arrays in the code are unnecessary for the final yes/no result.
