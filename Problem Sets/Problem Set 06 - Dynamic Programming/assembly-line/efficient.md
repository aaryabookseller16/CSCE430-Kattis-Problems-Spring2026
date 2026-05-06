# Efficient Solution: Assembly Line

## What this version changes
This markdown explains `efficient.py`. The approach is interval DP with reachable-result pruning. This keeps the same interval DP as solution.py, but only loops over component types that are actually reachable for each substring.

## Step-by-step algorithm
1. Parse the component symbols and assembly table.
2. For each query string, initialize dp[l][r][type] to infinity.
3. For each single character, set its own type cost to 0 and mark that type reachable.
4. For longer intervals, try every split point.
5. Loop only over reachable left types and reachable right types.
6. Combine those types using the table, update the result type cost, and record newly reachable types.
7. Pick the cheapest final type, using symbol order as tie-breaker.

## Example walkthrough
If substring ab can only become type c, future intervals involving ab only try c instead of all k possible types.

## Complexity
Still O(L^3*K^2) in the worst case, but often much faster when few result types are reachable; memory O(L^2*K).

## Important details
This is a performance-oriented variant of the main solution, not a different recurrence.
