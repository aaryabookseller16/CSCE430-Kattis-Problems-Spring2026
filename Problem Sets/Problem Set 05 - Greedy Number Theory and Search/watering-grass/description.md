# Watering Grass

You have a strip of grass of length `l` and width `w`. There are `n` sprinklers on the center line; sprinkler `i` is at position `x_i` (0..l) with radius `r_i`. A sprinkler covers a circular area; it waters the strip wherever the circle intersects the rectangle.

For each test case, find the minimum number of sprinklers to turn on so that the whole strip `[0, l]` is watered. If impossible, print `-1`.

## Input
- Multiple test cases (≤ 35).
- Each case: `n l w`
- Then `n` lines: `x_i r_i`

## Output
One line per case: the minimum number of sprinklers, or `-1` if not possible.

## Hint
Convert each sprinkler to a 1D interval on the x-axis using `dx = sqrt(r_i^2 - (w/2)^2)`, giving `[x_i - dx, x_i + dx]` if `r_i > w/2`. Then do a greedy interval cover from 0 to `l`.
