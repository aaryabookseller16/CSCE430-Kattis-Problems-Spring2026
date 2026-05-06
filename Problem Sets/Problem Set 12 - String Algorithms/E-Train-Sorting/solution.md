# Solution: Train Sorting

## Goal
Solve the problem with dynamic programming for increasing and decreasing subsequences. The implementation's main job is: For each car chosen as the middle/front decision point, the code computes how many heavier later cars can go on one side and lighter later cars on the other.

## Key idea
The solution is built around dynamic programming for increasing and decreasing subsequences. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: For each car chosen as the middle/front decision point, the code computes how many heavier later cars can go on one side and lighter later cars on the other.

## Step-by-step algorithm
1. Define the DP state so it contains exactly the information needed for future choices.
2. Initialize the base case from the simplest input or final decision.
3. Process states in an order where dependencies are already known.
4. For each state, try all legal transitions or choices.
5. Keep the best value according to the problem goal.
6. Store parent choices when the final path or string must be reconstructed.
7. Read and print the answer from the final state.

## Example walkthrough
For weights 1,2,3, car 1 can be kept and later heavier cars can be added to the front, giving length 3.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n^2) time and O(n) memory.

## Important details
The answer is inc[i] + dec[i] - 1 because car i is counted in both sides.
