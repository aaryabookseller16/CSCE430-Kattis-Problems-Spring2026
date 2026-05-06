# Solution Rankings

1. `solution_cos.py`
   - Method: simulate cuts, but compare corner sharpness with cosine values
   - Time: about `O(n^3)` in the worst case because it recomputes angles after each cut
   - Slightly faster in practice because it avoids `acos`

2. `solution.py`
   - Method: simulate cuts and compute actual angles with `acos`
   - Time: about `O(n^3)` in the worst case
   - Easier to read and the one I would submit for this small input size
