# Solution: Thanos the Hero

## Goal
Solve the problem with right-to-left greedy adjustment. The implementation's main job is: Populations must be strictly increasing in preference order after reductions. The code walks from right to left, lowering any population that is too high.

## Key idea
The solution is built around right-to-left greedy adjustment. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Populations must be strictly increasing in preference order after reductions. The code walks from right to left, lowering any population that is too high.

## Step-by-step algorithm
1. Read the ordered populations.
2. Scan from the second-to-last world toward the first.
3. Each world must have population strictly less than the world to its right.
4. If it is too large, reduce it to right_population - 1.
5. Add the removed people to the running total.
6. If a population would need to become negative, print 1 for impossible.
7. Otherwise print the number of people removed, with the problem-specific 1 output if no removals happen.

## Example walkthrough
For 5 2 3, the 5 must be reduced to 1 so it is below 2.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(n) memory.

## Important details
If a population would have to become negative, it prints 1.
