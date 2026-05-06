# Proving Equivalences

Consider a set of mathematical statements. Some implications between statements have already been proved. Your goal is to determine the minimum number of additional implications that must be proved so that all statements become equivalent.

Two statements are equivalent if each implies the other, possibly through a chain of already known implications.

## Input

The first line contains the number of test cases, at most `100`.

For each test case:

- One line with two integers `n` and `m` (`1 <= n <= 20000`, `0 <= m <= 50000`), where:
  - `n` is the number of statements
  - `m` is the number of implications already proved
- `m` lines follow, each containing two integers `s1` and `s2` (`1 <= s1, s2 <= n`, `s1 != s2`), meaning that statement `s1` implies statement `s2`

## Output

For each test case, print one line containing the minimum number of additional implications that must be proved so that all statements are equivalent.

## Sample Input

```text
2
4 0
3 2
1 2
1 3
```

## Sample Output

```text
4
2
```
