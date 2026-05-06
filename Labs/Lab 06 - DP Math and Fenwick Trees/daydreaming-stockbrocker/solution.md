# Solution: Daydreaming Stockbroker

## Goal
Solve the problem with greedy stock trading with known future prices. The implementation's main job is: If tomorrow is higher, buy as many shares as possible today. If tomorrow is lower, sell all today.

## Key idea
The solution is built around greedy stock trading with known future prices. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: If tomorrow is higher, buy as many shares as possible today. If tomorrow is lower, sell all today.

## Step-by-step algorithm
1. Start with 100 dollars and zero shares.
2. Look at each day and the next day price.
3. If tomorrow is higher, buy as many shares as possible today within the share cap.
4. If tomorrow is lower, sell all currently held shares today.
5. If prices are equal, do nothing.
6. After the last day, sell any remaining shares at the final price.
7. Print the final amount of money.

## Example walkthrough
Prices 1, 3, 2 mean buy at 1, sell at 3, then do not buy before 2.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(1) memory.

## Important details
The code respects the 100000-share cap.
