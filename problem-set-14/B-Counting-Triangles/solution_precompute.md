# Precompute Solution: Counting Triangles

## What this version changes
This markdown explains `solution_precompute.py`. The approach is pairwise segment-intersection precomputation. Instead of recomputing segment intersections inside every triple, this version first stores whether every pair of segments intersects.

## Step-by-step algorithm
1. Read all segments for one test case.
2. Create an n by n boolean table called intersects.
3. For every pair of segments, use orientation/cross-product tests to decide whether they touch.
4. Store the result in both symmetric table positions.
5. Loop over all triples of segment indexes.
6. A triple forms a triangle exactly when all three pairwise table entries are true.

## Example walkthrough
For segments 0, 1, and 2, the triple is counted only if intersects[0][1], intersects[0][2], and intersects[1][2] are all true.

## Complexity
O(n^2) precomputation plus O(n^3) triple counting; memory O(n^2).

## Important details
The total asymptotic time is still cubic, but the code avoids repeating the same pair test many times.
