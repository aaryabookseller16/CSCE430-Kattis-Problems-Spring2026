# Solution: Prince and Princess

## Goal
Solve the problem with longest increasing subsequence after coordinate mapping. The implementation's main job is: The prince route gives each square a position number. The princess route is converted into those positions, and the longest common route becomes an LIS.

## Key idea
The solution is built around longest increasing subsequence after coordinate mapping. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The prince route gives each square a position number. The princess route is converted into those positions, and the longest common route becomes an LIS.

## Step-by-step algorithm
1. Map each value in the first sequence to its position.
2. Scan the second sequence and keep only values that also appear in the first sequence.
3. Replace each kept value by its first-sequence position.
4. Run the standard LIS tail-array algorithm on those positions.
5. Use binary search to update the first tail value that is not smaller.
6. The number of tails is the length of the longest common valid route.
7. Print that length in the required format.

## Example walkthrough
If the common squares appear in prince order 1,4,8,9 along the princess route, they form a shared route of length 4.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O((p+q) log p) per test case; memory O(n^2) for the position array bound.

## Important details
This is a standard LCS-to-LIS reduction when one sequence has unique values.
