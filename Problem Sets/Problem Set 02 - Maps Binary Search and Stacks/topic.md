# Problem Set 2 Topics

Maps, binary search, simulated data structures, and monotonic stacks.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Adding Words** (`adding-words`): dictionary simulation. Complexity: O(L + V) per calc, where L is expression length and V is number of defined words; memory O(V).
- **Distributing Ballot Boxes** (`distributing-ballot-boxes`): binary search on maximum load. Complexity: O(N log max_population) per case; memory O(N).
- **Guess the Data Structure** (`guess-the-data-structure`): parallel simulation of stack, queue, and max-heap. Complexity: O(n log n) because priority queue operations use a heap; memory O(n).
- **Terrace Hill** (`terrace-hill`): monotonic stack. Complexity: O(n) time and O(n) memory.

## Main concepts covered
- dictionary simulation
- binary search on maximum load
- parallel simulation of stack, queue, and max-heap
- monotonic stack

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
