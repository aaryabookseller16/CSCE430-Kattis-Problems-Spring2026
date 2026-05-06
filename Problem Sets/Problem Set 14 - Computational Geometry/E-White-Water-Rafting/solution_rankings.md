# Solution Rankings

1. `solution.py`
   - Method: check every vertex against every edge of the other polygon
   - Time: `O(ni * no)`
   - Best one to submit because it avoids some repeated endpoint checks

2. `solution_slow.py`
   - Method: check every inner edge against every outer edge, trying all endpoint-to-segment distances
   - Time: `O(ni * no)`
   - Same big-O, but more repeated work
