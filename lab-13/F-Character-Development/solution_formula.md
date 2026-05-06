# Formula Solution: Character Development

## What this version changes
This markdown explains `solution_formula.py`. The approach is direct power-set formula. The answer is exactly all subsets minus the empty subset and the N one-character subsets.

## Step-by-step algorithm
1. Read N.
2. Compute 2**N, the number of all subsets.
3. Subtract N singleton subsets.
4. Subtract 1 empty subset.
5. Print the result.

## Example walkthrough
For N=3, 2**3 - 3 - 1 = 4 relationships.

## Complexity
O(log N) style big-integer exponentiation as handled by Python; memory is the output integer size.

## Important details
The main solution multiplies by 2 in a loop; this version uses Python exponentiation directly.
