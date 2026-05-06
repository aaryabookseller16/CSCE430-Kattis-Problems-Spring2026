# Just for Sidekicks

There are `N` gems in a row, each of type `1..6`. Type `t` has value `V_t`. You must handle `Q` queries of three kinds:
1) `1 K P` — change the type of gem `K` to `P`.  
2) `2 P V` — change the value of type `P` to `V`.  
3) `3 L R` — report the total value of gems in `[L, R]`.

## Input
`N Q`  
`V1 V2 ... V6`  
string of `N` digits (initial types)  
`Q` query lines as above.

## Output
For each type-3 query, print the total value on its own line.
