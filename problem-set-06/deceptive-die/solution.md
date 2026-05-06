# Solution: Deceptive Dice

## Goal
Solve the problem with expected value dynamic programming. The implementation's main job is: With one roll left, the expected value is the die average. With more rolls, the optimal rule is keep a roll only if it is at least the expected value of rerolling.

## Key idea
The solution is built around expected value dynamic programming. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: With one roll left, the expected value is the die average. With more rolls, the optimal rule is keep a roll only if it is at least the expected value of rerolling.

## Step-by-step algorithm
1. Define the DP state so it contains exactly the information needed for future choices.
2. Initialize the base case from the simplest input or final decision.
3. Process states in an order where dependencies are already known.
4. For each state, try all legal transitions or choices.
5. Keep the best value according to the problem goal.
6. Store parent choices when the final path or string must be reconstructed.
7. Read and print the answer from the final state.

## Example walkthrough
On a 2-sided die with rerolls, rolling 1 is worse than the future expectation, so you reroll.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(k) time using arithmetic sums over die faces; memory O(1).

## Important details
The code computes E[max(roll, previous_expected)].
