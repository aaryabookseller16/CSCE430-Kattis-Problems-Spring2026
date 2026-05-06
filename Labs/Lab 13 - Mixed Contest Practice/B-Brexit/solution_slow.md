# Slow Solution: Brexit

## What this version changes
This markdown explains `solution_slow.py`. The approach is repeated full graph scan. This version repeatedly scans all countries until one full pass causes no new country to leave.

## Step-by-step algorithm
1. Read the graph and mark the first country as left.
2. Set changed to true.
3. While changed is true, reset it to false and scan every country.
4. For each country still in the union, count how many of its partners have left.
5. If at least half are gone, mark the country as left and set changed true.
6. After the cascade stops, print whether the home country left.

## Example walkthrough
If country 4 needs two lost partners, it may not leave in the first pass but can leave in a later pass after neighbors leave.

## Complexity
O(C*P) in the worst case because many full scans can be needed; memory O(C+P).

## Important details
The queue-based main solution is faster because it only revisits neighbors of newly leaving countries.
