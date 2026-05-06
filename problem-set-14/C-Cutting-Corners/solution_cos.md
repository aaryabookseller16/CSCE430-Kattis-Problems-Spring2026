# Cosine Solution: Cutting Corners

## What this version changes
This markdown explains `solution_cos.py`. The approach is angle comparison by cosine values. A smaller angle has a larger cosine, so this version compares corner sharpness without calling acos.

## Step-by-step algorithm
1. Read the polygon vertices.
2. For each corner, build vectors from the corner to its two neighbors.
3. Compute dot/(length1*length2), which is the cosine of the interior angle.
4. Pick the corner with the largest cosine as the sharpest corner.
5. Remove that corner temporarily and recompute sharpness values.
6. Keep the removal only if the new maximum cosine is smaller, meaning the new smallest angle is larger.
7. Stop at three vertices or when the cut no longer improves the polygon.

## Example walkthrough
If one corner has cosine 0.9 and all others are 0.2 or lower, the 0.9 corner is the sharpest and is tried first.

## Complexity
O(n^3) in the small input limit; memory O(n).

## Important details
This is mathematically equivalent to comparing angles, but faster and avoids inverse cosine precision issues.
