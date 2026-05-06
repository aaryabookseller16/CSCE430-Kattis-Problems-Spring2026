# Solution: Tomography

## Goal
Solve the problem with greedy Havel-Hakimi/Gale-Ryser style check. The implementation's main job is: Rows are processed from largest demand to smallest. For each row, the code subtracts 1 from the currently largest column sums.

## Key idea
The solution is built around greedy Havel-Hakimi/Gale-Ryser style check. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Rows are processed from largest demand to smallest. For each row, the code subtracts 1 from the currently largest column sums.

## Step-by-step algorithm
1. First check that total row demand equals total column demand.
2. Sort row sums descending so the hardest rows are handled first.
3. For each row demand r, sort column sums descending.
4. Subtract 1 from the r columns with the most remaining capacity.
5. If any chosen column goes negative, the matrix is impossible.
6. Continue until all rows are processed.
7. Print Yes only if every column sum ends at zero.

## Example walkthrough
A row needing 3 ones is assigned to the three columns with the most remaining capacity.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(m*n log n) due to sorting column sums for each row; memory O(m+n).

## Important details
The total row sum must equal the total column sum first.

## Other implementations in this folder
- `solution_gale_ryser.md` has its own markdown explanation.
