# Solution: Dice Cup

## Goal
Solve the problem with enumerating most likely sums. The implementation's main job is: The code computes how many outcomes produce each possible sum of two dice, then prints sums with maximum probability.

## Key idea
The solution is built around enumerating most likely sums. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code computes how many outcomes produce each possible sum of two dice, then prints sums with maximum probability.

## Step-by-step algorithm
1. Read the two die sizes.
2. Every possible sum is between 2 and n+m.
3. For each pair of die faces, compute the sum and count how many ways that sum appears.
4. Find the largest count over all sums.
5. Collect every sum whose count equals that largest count.
6. Print those sums in increasing order.

## Example walkthrough
With d6 and d6, sum 7 has the most combinations.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n*m) time in the loops, though the ways formula is constant for each sum; memory O(n+m).

## Important details
The output can contain multiple equally likely sums.
