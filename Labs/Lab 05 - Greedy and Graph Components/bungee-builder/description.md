# Bungee Builder

There are `N` mountains with heights `H1..HN` in order. You may build a horizontal bridge between any two different mountains at a height strictly below both peaks; the maximum jump distance for that bridge is the vertical drop to the lower of the two mountains. Find the largest jump distance achievable; if no bridge is possible, the answer is 0.

## Input
`N` (`1 <= N <= 1e6`)  
`N` integers `H_i` (`0 <= H_i <= 1e6`)

## Output
One integer: the maximum possible jump distance, or 0 if none.

## Notes
Pick the two mountains that maximize `min(max_left, max_right) - H[i]`, where `max_left/right` are tallest seen to each side. A single pass from both sides is enough.
