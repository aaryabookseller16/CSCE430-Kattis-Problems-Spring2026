# Solution: Magic Checkerboard

## Goal
Solve the problem with constraint propagation, parity components, and greedy filling. The implementation's main job is: The code enforces row/column increasing limits from bottom-right, assigns parity constraints from diagonal components, then greedily fills smallest valid values.

## Key idea
The solution is built around constraint propagation, parity components, and greedy filling. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code enforces row/column increasing limits from bottom-right, assigns parity constraints from diagonal components, then greedily fills smallest valid values.

## Step-by-step algorithm
1. Handle one-row or one-column grids as a simpler increasing-sequence case.
2. For full grids, connect diagonally adjacent cells into parity components.
3. Color each component with two colors so diagonal neighbors have opposite parity.
4. Use fixed numbers to determine each component base parity, rejecting contradictions.
5. From bottom-right to top-left, compute the maximum allowed value for every cell from fixed values and increasing constraints.
6. For every possible assignment of still-free component parities, greedily fill the grid with the smallest value that is large enough and has the required parity.
7. Keep the minimum valid total sum, or print -1 if no assignment works.

## Example walkthrough
If a cell must be odd and the minimum increasing value is 4, it uses 5.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(2^F * n*m) where F is the number of free parity components; memory O(n*m).

## Important details
Fixed numbers can force or contradict a component parity.
