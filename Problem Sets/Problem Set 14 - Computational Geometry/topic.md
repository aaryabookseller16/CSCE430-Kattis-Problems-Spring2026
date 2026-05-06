# Problem Set 14 Topics

Computational geometry: convex hulls, polygon area, segment intersections, point-to-segment distance, and priority queues for geometric simplification.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Board Wrapping** (`A-Board-Wrapping`): computational geometry: rotated rectangles, convex hull, shoelace area. Complexity: O(B log B) per test case for B corner points; memory O(B).
  - Alternate: `solution_slow.md` - Slow Solution: Board Wrapping. Complexity: O(P*H) time, where P is the number of unique corner points and H is the number of hull points; memory O(P).
- **Counting Triangles** (`B-Counting-Triangles`): segment intersection with orientation tests. Complexity: O(n^3) triples, with constant-time intersection checks; memory O(n).
  - Alternate: `solution_precompute.md` - Precompute Solution: Counting Triangles. Complexity: O(n^2) precomputation plus O(n^3) triple counting; memory O(n^2).
- **Cutting Corners** (`C-Cutting-Corners`): polygon angle computation and iterative simulation. Complexity: O(n^3) in the small input limit, because each possible cut recomputes all angles; memory O(n).
  - Alternate: `solution_cos.md` - Cosine Solution: Cutting Corners. Complexity: O(n^3) in the small input limit; memory O(n).
- **Polyline Simplification** (`D-Polyline-Simplification`): priority queue with lazy updates and a linked list. Complexity: O((n-m) log n) time and O(n) memory.
  - Alternate: `solution_slow.md` - Slow Solution: Polyline Simplification. Complexity: O((n-m)*n) time in the worst case; memory O(n).
- **White Water Rafting** (`E-White-Water-Rafting`): point-to-segment distance between two polygons. Complexity: O(I*O) per test case, where I and O are polygon vertex counts; memory O(I+O).
  - Alternate: `solution_slow.md` - Slow Solution: White Water Rafting. Complexity: O(I*O) edge pairs with constant work per pair; memory O(I+O).

## Main concepts covered
- computational geometry: rotated rectangles, convex hull, shoelace area
- segment intersection with orientation tests
- polygon angle computation and iterative simulation
- priority queue with lazy updates and a linked list
- point-to-segment distance between two polygons

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
