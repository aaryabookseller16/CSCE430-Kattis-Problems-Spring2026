# Solution Rankings

1. `solution.py`
   - Method: monotonic chain convex hull
   - Time: `O(p log p)`, where `p = 4n` corner points
   - Best choice for submission

2. `solution_slow.py`
   - Method: gift wrapping / Jarvis march convex hull
   - Time: `O(p * h)`, where `h` is the number of points on the hull
   - Easier to follow, but can be slower if many corners are on the hull
