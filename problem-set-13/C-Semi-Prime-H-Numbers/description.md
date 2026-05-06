# Problem C: Semi-prime H-numbers

## Problem

An H-number is a positive number that is one more than a multiple of four:

```text
1, 5, 9, 13, 17, 21, ...
```

For this problem, only H-numbers are considered.

The number `1` is the only H-unit. An H-number greater than `1` is called an
H-prime if it cannot be written as the product of two smaller H-numbers greater
than `1`.

Every other H-number is H-composite.

An H-semi-prime is an H-number that can be written as the product of exactly two
H-primes. The two H-primes may be the same or different.

Examples:

```text
25 = 5 * 5
45 = 5 * 9
65 = 5 * 13
81 = 9 * 9
85 = 5 * 17
```

These are all H-semi-primes.

However:

```text
125 = 5 * 5 * 5
```

is not an H-semi-prime, because it uses three H-primes.

Your task is to count how many H-semi-primes are between `1` and each given
H-number `h`, inclusive.

## Input

Each input line contains one H-number `h`.

The last line contains `0`, which should not be processed.

Constraints:

- `h <= 1000001`
- There are at most `10000` test cases.

## Output

For each input value `h`, print:

```text
h answer
```

where `answer` is the number of H-semi-primes from `1` through `h`, inclusive.

## Sample Input 1

```text
21
85
789
0
```

## Sample Output 1

```text
21 0
85 5
789 62
```

## Notes

A normal prime is not the same thing as an H-prime.

For example, `9` is not a regular prime, but it is an H-prime here because it
cannot be made by multiplying two smaller H-numbers greater than `1`.

The useful precomputation is:

1. Mark every H-number that can be made as a product of two H-numbers.
2. The unmarked H-numbers greater than `1` are H-primes.
3. Multiply pairs of H-primes and mark the products as H-semi-primes.
4. Build prefix counts so each query can be answered quickly.
