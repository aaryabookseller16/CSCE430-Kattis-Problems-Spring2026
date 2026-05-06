# Solution: White Water Rafting

## Goal
Solve the problem with point-to-segment distance between two polygons. The implementation's main job is: The smallest gap between the inner and outer boundaries is found by checking every corner against every opposite edge in both directions. The raft radius is half that gap.

## Key idea
The solution is built around point-to-segment distance between two polygons. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The smallest gap between the inner and outer boundaries is found by checking every corner against every opposite edge in both directions. The raft radius is half that gap.

## Step-by-step algorithm
1. Read both polygons as ordered vertex lists.
2. Initialize the smallest boundary gap to a very large value.
3. For each relevant corner and opposite edge, project the corner onto the edge line.
4. Clamp the projection parameter to the segment range [0, 1].
5. Compute the Euclidean distance from the corner to that closest point.
6. Keep the minimum distance over all checks.
7. Divide the narrowest boundary gap by two to get the maximum raft radius.

## Example walkthrough
If the closest place is an inner corner near an outer wall, the point-to-segment projection finds that exact narrow spot.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(I*O) per test case, where I and O are polygon vertex counts; memory O(I+O).

## Important details
Checking both directions matters because the closest pair can be outer-corner to inner-edge or inner-corner to outer-edge.

## Other implementations in this folder
- `solution_slow.md` has its own markdown explanation.
