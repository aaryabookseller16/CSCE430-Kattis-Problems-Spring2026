# Fractional Lotion

Given a concentration `1/n`, split it into two flasks so the concentrations are `1/x` and `1/y` and both flasks together keep the same volume. We need the number of unordered pairs `{x, y}` of positive integers such that:
```
1/x + 1/y = 1/n
```

Input: each line is `1/n` with `1 <= n <= 10000`.

Output: for each line, print the number of distinct pairs `{x, y}`.

Sample:
```
1/2
1/4
1/1
1/5000
```
gives
```
2
3
1
32
```
