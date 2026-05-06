# Solution: Haiku

## Goal
Solve the problem with word-break dynamic programming with syllable counts. The implementation's main job is: For each poem line, dp[position] stores which syllable counts can reach that character position. The line is valid if it can end at 5, 7, or 5 syllables.

## Key idea
The solution is built around word-break dynamic programming with syllable counts. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: For each poem line, dp[position] stores which syllable counts can reach that character position. The line is valid if it can end at 5, 7, or 5 syllables.

## Step-by-step algorithm
1. Define the DP state so it contains exactly the information needed for future choices.
2. Initialize the base case from the simplest input or final decision.
3. Process states in an order where dependencies are already known.
4. For each state, try all legal transitions or choices.
5. Keep the best value according to the problem goal.
6. Store parent choices when the final path or string must be reconstructed.
7. Read and print the answer from the final state.

## Example walkthrough
A word may split as spe-lling if both pieces are allowed syllables.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(total line length * matching syllables) time; memory O(line length).

## Important details
Bit masks keep all possible syllable counts compact.
