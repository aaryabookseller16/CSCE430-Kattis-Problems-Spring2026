# Solution: Kindergarten Excursion

## Goal
Solve the problem with inversion counting for three symbols. The implementation's main job is: The minimum adjacent swaps equals the number of out-of-order pairs. The code counts how many 1s and 2s each 0 must pass, and how many 2s each 1 must pass.

## Key idea
The solution is built around inversion counting for three symbols. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The minimum adjacent swaps equals the number of out-of-order pairs. The code counts how many 1s and 2s each 0 must pass, and how many 2s each 1 must pass.

## Step-by-step algorithm
1. Scan the line from left to right.
2. Keep counts of larger destination groups already seen.
3. When a smaller group appears, add the number of larger groups it must pass.
4. Update the count for the current group.
5. At the end, the accumulated count is the minimum adjacent swaps.
6. Print that count.

## Example walkthrough
In 210, the 0 must pass both 2 and 1, and the 1 must pass 2, for 3 swaps.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(1) memory.

## Important details
This works because only destinations 0, 1, and 2 exist.
