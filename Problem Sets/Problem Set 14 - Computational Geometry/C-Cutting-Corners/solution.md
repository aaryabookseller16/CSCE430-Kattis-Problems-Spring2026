# Solution: Cutting Corners

## Goal
Solve the problem with polygon angle computation and iterative simulation. The implementation's main job is: The code repeatedly finds the smallest interior angle, tries removing that corner, and keeps the cut only when the new smallest angle improves.

## Key idea
The solution is built around polygon angle computation and iterative simulation. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code repeatedly finds the smallest interior angle, tries removing that corner, and keeps the cut only when the new smallest angle improves.

## Step-by-step algorithm
1. Read the polygon vertices in order.
2. For each vertex, form vectors to the previous and next vertices.
3. Compute the interior angle using dot product, vector lengths, and acos.
4. Find the vertex with the smallest angle.
5. Temporarily remove that vertex and recompute all angles.
6. Keep the removal only if the new smallest angle is strictly larger.
7. Repeat until only three vertices remain or no cut improves the shape.

## Example walkthrough
If a pentagon has one very sharp corner, the algorithm removes that vertex and checks whether the remaining polygon is actually less sharp.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n^3) in the small input limit, because each possible cut recomputes all angles; memory O(n).

## Important details
Cosine values are clamped to [-1, 1] before acos to avoid floating-point noise.

## Other implementations in this folder
- `solution_cos.md` has its own markdown explanation.
