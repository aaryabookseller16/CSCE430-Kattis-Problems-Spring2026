# Formula Solution: Amsterdam Distance

## What this version changes
This markdown explains `solution_formula.py`. The approach is closed-form comparison of center route and smallest shared ring route. The distance as a function of the meeting ring is linear between important boundaries, so the best ring is either the center or the smaller of the two given rings.

## Step-by-step algorithm
1. Compute the radial width of one ring.
2. Compute the angular separation between the two spokes.
3. Compute the route through the center: walk from both points to ring 0.
4. Compute the route that uses the smaller starting ring for the arc.
5. Compare those two distances and print the smaller one.

## Example walkthrough
If two points are far apart angularly, going to the center may beat walking along a large outer arc.

## Complexity
O(1) time and memory.

## Important details
The main solution tries every ring; this formula version uses the shape of the distance function to skip that loop.
