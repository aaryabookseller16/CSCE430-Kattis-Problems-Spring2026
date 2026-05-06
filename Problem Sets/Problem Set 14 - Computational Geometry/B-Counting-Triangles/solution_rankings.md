# Solution Rankings

1. `solution_precompute.py`
   - Method: first precompute every pair of intersecting segments, then count triples
   - Time: `O(n^2 + n^3)`
   - Faster in practice because each pair intersection is computed once

2. `solution.py`
   - Method: try every triple and recompute the three segment intersections each time
   - Time: `O(n^3)`
   - Still fine for `n <= 50`, just more repeated work
