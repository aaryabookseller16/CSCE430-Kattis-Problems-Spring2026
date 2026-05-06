# Problem B: Inverse Factorial

## Problem

The factorial of a positive integer `n`, written as `n!`, is the product of all
positive integers from `1` through `n`.

For example:

```text
5! = 1 * 2 * 3 * 4 * 5 = 120
```

In this problem, you are given the value of `n!`. Your job is to recover the
original value of `n`.

The factorial can be extremely large, so the input may have up to `10^6` digits.

## Input

The input contains one integer: the value of `n!`.

The number of digits is at most `10^6`.

## Output

Print the value of `n`.

## Sample Input 1

```text
120
```

## Sample Output 1

```text
5
```

## Sample Input 2

```text
51090942171709440000
```

## Sample Output 2

```text
21
```

## Sample Input 3

```text
10888869450418352160768000000
```

## Sample Output 3

```text
27
```

## Notes

For small inputs, the factorial value can be checked directly.

For large inputs, storing the full factorial is unnecessary. The number of digits
of `n!` is:

```text
floor(log10(1) + log10(2) + ... + log10(n)) + 1
```

So we can keep adding logarithms until the digit count matches the length of the
given input.
