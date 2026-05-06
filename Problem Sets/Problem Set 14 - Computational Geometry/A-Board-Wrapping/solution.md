# Solution: Board Wrapping

## Goal
Solve the problem with computational geometry: rotated rectangles, convex hull, shoelace area. The implementation's main job is: The code converts every board into its four rotated corner points, builds the convex hull of all corners, then compares total board area with hull area.

## Key idea
The solution is built around computational geometry: rotated rectangles, convex hull, shoelace area. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code converts every board into its four rotated corner points, builds the convex hull of all corners, then compares total board area with hull area.

## Step-by-step algorithm
1. Read every rectangle and add its area to the running board-area total.
2. Compute the four rotated corner coordinates for each rectangle.
3. Sort and deduplicate all corner points.
4. Build the lower and upper hulls with cross products, removing turns that would bend inward.
5. Join the hull halves into one polygon.
6. Use the shoelace formula on the hull polygon to get the mould area.
7. Print board area divided by mould area as a percentage.

## Example walkthrough
If two boards sit at different angles, their eight corners are the only points that can define the outside frame. The hull around those points gives the mould area.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(B log B) per test case for B corner points; memory O(B).

## Important details
The monotonic-chain hull removes clockwise or collinear turns, then the shoelace formula measures polygon area.

## Other implementations in this folder
- `solution_slow.md` has its own markdown explanation.
