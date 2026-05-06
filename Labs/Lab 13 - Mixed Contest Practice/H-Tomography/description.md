# Problem H: Tomography

Binary tomography asks whether a binary matrix can be built from its row sums and
column sums.

You are given `m` row sums and `n` column sums. Decide whether there exists an
`m` by `n` matrix where every entry is either `0` or `1`, each row has the given
sum, and each column has the given sum.

## Input

The first line contains two integers:

```text
m n
```

where `1 <= m, n <= 1000`.

The second line contains `m` integers, the row sums.

The third line contains `n` integers, the column sums.

Each row sum is between `0` and `n`, and each column sum is between `0` and `m`.

## Output

Print `Yes` if such a binary matrix exists.

Otherwise print `No`.

## Sample Input 1

```text
3 4
2 3 2
1 1 3 2
```

## Sample Output 1

```text
Yes
```

## Sample Input 2

```text
3 3
0 0 3
0 0 3
```

## Sample Output 2

```text
No
```

## Idea

The total row sum must equal the total column sum.

After that, one way to check feasibility is greedy: handle rows from largest to
smallest, and for each row place its `1`s into the columns that still need the
most `1`s. If this process finishes exactly, the answer is `Yes`.
