# Problem G: An Industrial Spy

You found a paper snippet containing some digits. From those digits, you can make
numbers by using one or more of the digits, in any order. Each digit from the
snippet can be used at most once in a number.

Count how many different prime numbers can be made.

Numbers with leading zeroes are allowed while forming them, but the final integer
is read normally. For example, `011` represents the number `11`.

## Input

The first line contains an integer `C`, the number of test cases.

Each test case contains one string of digits. The string has at most 7 digits.

## Output

For each test case, print one integer: the number of different primes that can be
formed from the given digits.

## Sample Input

```text
4
17
1276543
9999999
011
```

## Sample Output

```text
3
1336
0
2
```

## Idea

Generate all permutations of length `1` through `n`, convert each one to an
integer, and put it in a set so duplicates are only counted once. Then count how
many of those numbers are prime.
