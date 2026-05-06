# Solution Rankings

1. `solution.py`
   - Method: dynamic programming with a direct formula for each group cost
   - Time: `O(N^2)`
   - Best choice for `N <= 4000`

2. `solution_slow.py`
   - Method: dynamic programming, but simulates each possible group of boats
   - Time: roughly `O(N^3)`
   - Easier to compare against the statement, but not good enough for large input
