# Solution Rankings

1. `solution_gale_ryser.py`
   - Method: Gale-Ryser theorem inequality check
   - Time: about `O(mn)` after sorting
   - More mathematical and usually faster

2. `solution.py`
   - Method: greedy row filling by repeatedly sorting column needs
   - Time: about `O(m * n log n)`
   - Simpler and still fine for `m, n <= 1000`
