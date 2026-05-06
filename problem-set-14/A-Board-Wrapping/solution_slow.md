# Slow Solution: Board Wrapping

## What this version changes
This markdown explains `solution_slow.py`. The approach is Jarvis march / gift wrapping convex hull. This version still computes every rotated board corner, but it builds the convex hull by walking around the outside one hull point at a time.

## Step-by-step algorithm
1. Read each board and add its area to the total board area.
2. Rotate the four local rectangle corners into global coordinates and collect them.
3. Pick the leftmost, then lowest, point as the hull start.
4. Repeatedly choose the next point that keeps all other points on the same side, using the cross product.
5. Break ties among collinear points by taking the farther point so the hull stays outside.
6. Compute hull area with the shoelace formula and print board_area / hull_area as a percentage.

## Example walkthrough
If the outside frame touches only four of twenty collected corners, gift wrapping visits just those four hull corners in circular order.

## Complexity
O(P*H) time, where P is the number of unique corner points and H is the number of hull points; memory O(P).

## Important details
This is simpler to understand than monotonic chain, but slower when many points lie on the hull.
