# Solution: Narrow Art Gallery

## Goal
Solve the problem with dynamic programming over rows and closure state. The implementation's main job is: The DP minimizes the value of closed rooms while tracking whether the previous row closed left, right, or none. Invalid diagonal blocks are skipped.

## Key idea
The solution is built around dynamic programming over rows and closure state. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The DP minimizes the value of closed rooms while tracking whether the previous row closed left, right, or none. Invalid diagonal blocks are skipped.

## Step-by-step algorithm
1. Define the DP state so it contains exactly the information needed for future choices.
2. Initialize the base case from the simplest input or final decision.
3. Process states in an order where dependencies are already known.
4. For each state, try all legal transitions or choices.
5. Keep the best value according to the problem goal.
6. Store parent choices when the final path or string must be reconstructed.
7. Read and print the answer from the final state.

## Example walkthrough
If the left room was closed in the previous row, the current row cannot close the right room.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n*k) time and O(k) memory.

## Important details
The final answer is total gallery value minus minimum closed value.
