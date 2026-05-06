# Solution: Uxuhul Voting System

## Goal
Solve the problem with backward induction over game states. The implementation's main job is: There are only 8 possible outcomes. Working from oldest voter backward, the DP records which final outcome each current state leads to under optimal play.

## Key idea
The solution is built around backward induction over game states. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: There are only 8 possible outcomes. Working from oldest voter backward, the DP records which final outcome each current state leads to under optimal play.

## Step-by-step algorithm
1. Define the DP state so it contains exactly the information needed for future choices.
2. Initialize the base case from the simplest input or final decision.
3. Process states in an order where dependencies are already known.
4. For each state, try all legal transitions or choices.
5. Keep the best value according to the problem goal.
6. Store parent choices when the final path or string must be reconstructed.
7. Read and print the answer from the final state.

## Example walkthrough
From NNN, flipping one issue gives one of three next states; the voter chooses the one with best final rank.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(m*8*3) time and O(8) memory.

## Important details
The final state is read from dp[NNN].
