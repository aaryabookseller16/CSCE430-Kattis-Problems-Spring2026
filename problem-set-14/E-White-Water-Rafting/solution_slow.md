# Slow Solution: White Water Rafting

## What this version changes
This markdown explains `solution_slow.py`. The approach is all edge-pair endpoint distance checks. For every inner edge and outer edge pair, this version checks both endpoints of each edge against the other edge.

## Step-by-step algorithm
1. Read the inner and outer polygons.
2. Initialize the smallest gap to a very large number.
3. For each inner edge and outer edge, project the inner edge endpoints onto the outer edge.
4. Clamp each projection to the segment and update the smallest distance.
5. Project the outer edge endpoints onto the inner edge in the same way.
6. After all edge pairs, divide the smallest boundary distance by two to get the raft radius.

## Example walkthrough
If an outer corner is closest to the middle of an inner wall, the outer-endpoint-to-inner-segment projection finds that gap.

## Complexity
O(I*O) edge pairs with constant work per pair; memory O(I+O).

## Important details
The main solution expresses the same closest-distance idea as corner-to-opposite-edge loops.
