# Planetaris

Ali has `s` ships to allocate over `n` solar systems. Finn sends `c_i` ships to system `i`. If Ali sends more ships than Finn to a system, he wins it; if fewer, he loses; if equal, nobody wins. Ships are spent either way. What is the maximum number of systems Ali can win?

## Input
- `n s` with `1 <= n <= 1e5`, `0 <= s <= 1e9`
- Line with `n` integers `c_i` (`0 <= c_i <= 1e9`)

## Output
Maximum systems Ali can win with best play.

## Hint
Sort `c_i`; greedily beat the cheapest systems first while you have ships left.
