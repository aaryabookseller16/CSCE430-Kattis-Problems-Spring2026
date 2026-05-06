# Lab 11 Topics

Reverse graph processing, DSU, BFS, DFS, MSTs, and direct simulations. A couple of folders have empty solutions.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Artwork** (`A-Artwork`): reverse processing with union-find. Complexity: O(nm + total stroke length * alpha(nm)) time; memory O(nm).
- **Collatz Conjecture** (`B-Collatz-Conjecture`): hash map of one sequence. Complexity: O(length of both sequences until meeting); memory O(length of A sequence).
- **Family Visits** (`C-Family-Visits`): No implemented primary solution. no implemented solution. Complexity: N/A for the checked-in file.
- **Final Exam** (`D-Final-Exam`): one-position shift comparison. Complexity: O(n) time and O(n) memory for the answer list.
- **Firefly** (`E-Firefly`): No implemented primary solution. no implemented solution. Complexity: N/A for the checked-in file.
- **Getting Gold** (`F-Getting-Cold`): DFS with trap-adjacency stopping rule. Complexity: O(WH) time and memory.
- **Knights in Fen** (`G-Knights-In-Gen`): precomputed BFS from the target board. Complexity: Precomputation is bounded by all states within depth 10; each query is O(1) lookup after reading 25 cells.
- **Treehouses** (`H-Treehouses`): Prim MST with zero-cost existing edges. Complexity: O(n^2) time and O(n+p) memory.

## Main concepts covered
- reverse processing with union-find
- hash map of one sequence
- no implemented solution
- one-position shift comparison
- DFS with trap-adjacency stopping rule
- precomputed BFS from the target board
- Prim MST with zero-cost existing edges

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
