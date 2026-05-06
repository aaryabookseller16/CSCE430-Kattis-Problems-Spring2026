# Solution Rankings

1. `solution.py`
   - Method: heap of current triangle areas, plus previous/next arrays
   - Time: `O((n - m) log n)`
   - Best choice for the real constraints

2. `solution_slow.py`
   - Method: rescan all current interior points after every cut
   - Time: about `O((n - m) * n)`
   - Easier to read, but not good enough for the largest cases
