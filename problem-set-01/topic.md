# Problem Set 1 Topics

Introductory implementation: simulation, base conversion, counting inversions, time arithmetic, and prefix/suffix scans.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **1-D Frogger** (`1d-frogger`): direct simulation with cycle detection. Complexity: O(number of visited squares), at most O(n); memory O(n).
- **Alien Numbers** (`alien-numbers`): base conversion through decimal. Complexity: O(length of number + number of target digits); memory O(number of target digits).
- **Kindergarten Excursion** (`kindergarten-excursion`): inversion counting for three symbols. Complexity: O(n) time and O(1) memory.
- **Natrij** (`natrij`): time arithmetic in seconds. Complexity: O(1) time and memory.
- **Path Tracing** (`path-tracing`): grid simulation and bounding box output. Complexity: O(M + A), where M is number of moves and A is printed area; memory uses a fixed 1000x1000 array.
- **Pivot** (`pivot`): prefix maxima and suffix minima. Complexity: O(n) time and O(n) memory.

## Main concepts covered
- direct simulation with cycle detection
- base conversion through decimal
- inversion counting for three symbols
- time arithmetic in seconds
- grid simulation and bounding box output
- prefix maxima and suffix minima

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
