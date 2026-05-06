# Gale-Ryser Solution: Tomography

## What this version changes
This markdown explains `solution_gale_ryser.py`. The approach is Gale-Ryser inequality check. A binary matrix exists exactly when the row sums and column sums satisfy the Gale-Ryser conditions.

## Step-by-step algorithm
1. Read row sums and column sums.
2. Reject immediately if their totals differ.
3. Sort both lists in descending order.
4. For k from 1 to the number of rows, compute the sum of the largest k row sums.
5. Compute the matching right side: sum min(column_sum, k) over all columns.
6. If any left side is larger than the right side, reject.
7. If all checks pass, print Yes.

## Example walkthrough
If the first two rows require 7 ones total but the columns can provide at most 6 ones across two rows, no matrix exists.

## Complexity
O(m*n) after sorting; memory O(m+n).

## Important details
The main solution is constructive greedy; this variant is theorem-based.
