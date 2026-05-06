# Solution Rankings

1. `solution.py`
   - Method: queue of countries as they leave, updating only neighbors
   - Time: `O(C + P)`
   - Best choice for the constraints

2. `solution_slow.py`
   - Method: repeatedly scan every country and recount how many partners have left
   - Time: can be much worse, roughly `O(C * P)` in bad cases
   - Easier to read, but too slow for large inputs
