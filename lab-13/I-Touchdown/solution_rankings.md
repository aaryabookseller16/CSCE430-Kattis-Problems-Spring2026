# Solution Rankings

1. `solution.py`
   - Method: simulate plays and stop immediately once a result is known
   - Time: `O(N)`
   - Best version

2. `solution_prefix.py`
   - Method: build all positions first, then scan them
   - Time: `O(N)`
   - Does a little unnecessary work, but still fine for `N <= 15`
