# Problem Set 7 Topics

Optimization by search: binary search, ternary search, matrix exponentiation, and interactive interval narrowing.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Freight Train** (`freight-train`): binary search with greedy feasibility. Complexity: O(W log N) per test case; memory O(W).
- **Going to Seed** (`going-to-seed`): interactive interval splitting. Complexity: At most 16 queries; memory O(1).
- **Reconnaissance** (`reconnaissance`): ternary search on a convex function. Complexity: O(n * iterations), with 200 fixed iterations; memory O(n).
- **Screamers in the Storm** (`screamers-in-the-storm`): matrix exponentiation over allowed adjacent heights. Complexity: O(K^3 log N) time and O(K^2) memory.
- **Travelling Monk** (`travelling-monk`): binary search on meeting time. Complexity: O((a+d) + iterations * pointer movement) time; memory O(a+d).

## Main concepts covered
- binary search with greedy feasibility
- interactive interval splitting
- ternary search on a convex function
- matrix exponentiation over allowed adjacent heights
- binary search on meeting time

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
