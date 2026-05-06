# Money Matters

There are `n` people, each with a net balance (positive = owed to them, negative = they owe). Friendships form groups where money can be moved around freely inside the group. Determine if every group’s balances can sum to zero; if yes print `POSSIBLE`, else `IMPOSSIBLE`.

## Input
`n m` (`1 <= n <= 1e4`, `0 <= m <= 5e4`)  
`n` integers: balances for persons `0..n-1`  
`m` lines: `u v` friendships (undirected)

## Output
`POSSIBLE` if every connected component sums to zero, otherwise `IMPOSSIBLE`.
