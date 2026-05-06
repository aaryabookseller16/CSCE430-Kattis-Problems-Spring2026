# Solution: Brocard Point of a Triangle

## Goal
Solve the problem with triangle side lengths and barycentric-style weights. The implementation's main job is: The solution computes side lengths and uses the known first Brocard point weights to average the three vertices.

## Key idea
The solution is built around triangle side lengths and barycentric-style weights. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The solution computes side lengths and uses the known first Brocard point weights to average the three vertices.

## Step-by-step algorithm
1. Read the triangle id and coordinates.
2. Compute side a opposite vertex A, side b opposite B, and side c opposite C.
3. Compute the Brocard weights for A, B, and C.
4. Add the weights to get the denominator.
5. Compute the weighted average of x coordinates.
6. Compute the weighted average of y coordinates.
7. Print the id and the point coordinates.

## Example walkthrough
A vertex with larger weight pulls the final x,y coordinate closer to itself.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(1) per triangle; memory O(1).

## Important details
The input id k is printed back with the computed coordinates.
