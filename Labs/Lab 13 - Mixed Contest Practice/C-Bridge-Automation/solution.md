# Solution: Bridge Automation

## Goal
Solve the problem with dynamic programming over grouped arrivals. The implementation's main job is: best_time[i] stores the minimum road-closed time for the first i boats. The transition groups a suffix of boats into one bridge opening.

## Key idea
The solution is built around dynamic programming over grouped arrivals. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: best_time[i] stores the minimum road-closed time for the first i boats. The transition groups a suffix of boats into one bridge opening.

## Step-by-step algorithm
1. Define the DP state so it contains exactly the information needed for future choices.
2. Initialize the base case from the simplest input or final decision.
3. Process states in an order where dependencies are already known.
4. For each state, try all legal transitions or choices.
5. Keep the best value according to the problem goal.
6. Store parent choices when the final path or string must be reconstructed.
7. Read and print the answer from the final state.

## Example walkthrough
If boats arrive close together, keeping the bridge raised can be cheaper than lowering and raising again.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N^2) time and O(N) memory.

## Important details
The formula includes 60 seconds up, 60 seconds down, and boat passing/waiting constraints.

## Other implementations in this folder
- `solution_slow.md` has its own markdown explanation.
