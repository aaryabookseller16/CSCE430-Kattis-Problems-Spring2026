# Solution: Counting Triangles

## Goal
Solve the problem with segment intersection with orientation tests. The implementation's main job is: The solution checks every triple of segments and counts it when all three pairs intersect.

## Key idea
The solution is built around segment intersection with orientation tests. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The solution checks every triple of segments and counts it when all three pairs intersect.

## Step-by-step algorithm
1. Read all line segments.
2. For each triple of segment indexes, inspect the three segment pairs.
3. For each pair, compute cross products to see whether endpoints lie on opposite sides.
4. Also handle endpoint-on-segment cases using bounding-box checks and a small epsilon.
5. Count the triple only if all three pairs intersect.
6. Print the number of counted triples.

## Example walkthrough
For three sticks A, B, and C, they form a triangle only if A meets B, A meets C, and B meets C.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n^3) triples, with constant-time intersection checks; memory O(n).

## Important details
A small epsilon is used because the coordinates are real numbers.

## Other implementations in this folder
- `solution_precompute.md` has its own markdown explanation.
