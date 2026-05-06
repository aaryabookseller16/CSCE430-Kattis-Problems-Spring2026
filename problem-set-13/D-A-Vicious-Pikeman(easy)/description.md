# Problem C: Semi-prime H-numbers

An H-number is a positive number that is one more than a multiple of four:

```text
1, 5, 9, 13, 17, 21, ...
```

The H-numbers are closed under multiplication. For example:

```text
5 * 9 = 45
```

Among the H-numbers:

- `1` is the only unit
- an H-prime is an H-number that is not `1` and cannot be written as the product
  of two smaller H-numbers
- all other H-numbers are H-composite

An H-semi-prime is an H-number that can be written as the product of exactly two
H-primes. The two H-primes may be the same or different.

Your task is to count how many H-semi-primes are less than or equal to each input
number.

## Input

Each line contains one H-number `h`, where:

```text
h < 1000001
```

The last line contains `0`, and should not be processed.

There are at most 10000 test cases.

## Output

For each input value `h`, print one line containing `h`, then one space, then the
number of H-semi-primes between `1` and `h`, inclusive.

## Sample Input

```text
21
85
789
0
```

## Sample Output

```text
21 0
85 5
789 62
```

## Idea

First build a sieve over numbers of the form `4k + 1` to find the H-primes.
Then mark every product of two H-primes as an H-semi-prime. A prefix count array
lets us answer each query quickly.
