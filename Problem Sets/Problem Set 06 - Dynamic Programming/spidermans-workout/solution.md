# Solution: Spiderman Workout

## Goal
Solve the problem with height DP with parent reconstruction. The implementation's main job is: The DP tracks reachable current heights and the smallest peak used so far. Parent tables reconstruct U/D moves.

## Key idea
The solution is built around height DP with parent reconstruction. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The DP tracks reachable current heights and the smallest peak used so far. Parent tables reconstruct U/D moves.

## Step-by-step algorithm
1. Define the DP state so it contains exactly the information needed for future choices.
2. Initialize the base case from the simplest input or final decision.
3. Process states in an order where dependencies are already known.
4. For each state, try all legal transitions or choices.
5. Keep the best value according to the problem goal.
6. Store parent choices when the final path or string must be reconstructed.
7. Read and print the answer from the final state.

## Example walkthrough
For 20 20 20 20, UDUD returns to height 0 with peak 20.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(M*S) time and memory, where S is the total distance.

## Important details
Heights below zero are never allowed.
