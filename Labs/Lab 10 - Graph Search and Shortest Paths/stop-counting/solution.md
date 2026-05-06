# Solution: Stop Counting

## Goal
Solve the problem with best prefix or suffix average. The implementation's main job is: Counting a prefix, a suffix, or nothing is enough because any prefix-plus-suffix average cannot exceed the better of its two parts. The code checks all prefixes and suffixes.

## Key idea
The solution is built around best prefix or suffix average. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Counting a prefix, a suffix, or nothing is enough because any prefix-plus-suffix average cannot exceed the better of its two parts. The code checks all prefixes and suffixes.

## Step-by-step algorithm
1. Start with best payout 0, because counting no cards is allowed.
2. Scan prefixes from the front and track prefix sum and average.
3. Update best with every prefix average.
4. Scan suffixes from the back and track suffix sum and average.
5. Update best with every suffix average.
6. Print the largest average found.

## Example walkthrough
For 10 10 -10 -4 10, the best counted average is 10.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N) time and O(1) memory.

## Important details
The answer is at least 0 because counting no cards is allowed.
