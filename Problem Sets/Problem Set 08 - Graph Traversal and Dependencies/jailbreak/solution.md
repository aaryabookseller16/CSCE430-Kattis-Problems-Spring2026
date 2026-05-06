# Solution: Jailbreak

## Goal
Solve the problem with 0-1 BFS from three starting points. The implementation's main job is: The code computes door-opening distances from outside and from each prisoner. It then tries every meeting cell and subtracts duplicate door costs.

## Key idea
The solution is built around 0-1 BFS from three starting points. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code computes door-opening distances from outside and from each prisoner. It then tries every meeting cell and subtracts duplicate door costs.

## Step-by-step algorithm
1. Build the grid or graph with edge costs of only 0 and 1.
2. Start BFS from each required source.
3. Use a deque instead of a normal queue.
4. Push zero-cost moves to the front and one-cost moves to the back.
5. Store the smallest cost to each cell.
6. Combine distance maps from multiple sources if needed.
7. Adjust duplicated costs and print the minimum.

## Example walkthrough
If both prisoners and John all pass through the same door, that door is counted three times in the sums but should be opened once.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(hw) per BFS, so O(hw) overall per case; memory O(hw).

## Important details
Padding the map with outside floor makes escape just another path to the outside component.
