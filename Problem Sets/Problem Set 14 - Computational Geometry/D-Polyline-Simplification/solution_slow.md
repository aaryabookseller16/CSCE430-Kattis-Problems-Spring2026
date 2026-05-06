# Slow Solution: Polyline Simplification

## What this version changes
This markdown explains `solution_slow.py`. The approach is direct repeated scan of active points. This version keeps a list of active point indexes and rescans every removable point after each deletion.

## Step-by-step algorithm
1. Read the original points.
2. Store all point indexes in active_points.
3. For each required deletion, scan every interior active point.
4. Compute the triangle area made by its active left and right neighbors.
5. Choose the smallest area; if tied, choose the smaller original index.
6. Print that original index and remove it from active_points.

## Example walkthrough
If active points are [0,1,2,3], point 1 is judged using triangle 0-1-2 and point 2 using triangle 1-2-3.

## Complexity
O((n-m)*n) time in the worst case; memory O(n).

## Important details
The heap-based main solution is faster because only the deleted point neighbors need area updates.
