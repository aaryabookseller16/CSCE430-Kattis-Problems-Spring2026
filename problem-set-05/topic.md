# Problem Set 5 Topics

Greedy methods, number theory, constraint filling, and exponential search for small combinatorial spaces.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Classrooms** (`classrooms`): greedy interval scheduling with multiple rooms. Complexity: Conceptually O(n log k); this Python list implementation has O(k) deletion cost in the worst case.
- **Fractional Lotion** (`fractional-lotion`): number theory using divisor counts. Complexity: O(sqrt n) per input line; memory O(1).
- **Magic Checkerboard** (`magic-checkerboard`): constraint propagation, parity components, and greedy filling. Complexity: O(2^F * n*m) where F is the number of free parity components; memory O(n*m).
- **Mini Battleship** (`mini-battleship`): backtracking search. Complexity: Exponential in the number of ships and possible placements; memory O(n^2).
- **Watering Grass** (`watering-grass`): interval conversion and greedy covering. Complexity: O(n log n) per case for sorting; memory O(n).

## Main concepts covered
- greedy interval scheduling with multiple rooms
- number theory using divisor counts
- constraint propagation, parity components, and greedy filling
- backtracking search
- interval conversion and greedy covering

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
