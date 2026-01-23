# Problem B — Alien Numbers

## Overview

The decimal numeral system is composed of ten digits, represented as:

```
0123456789
```

Digits in a numeral system are written from **lowest to highest value**. Now imagine that you have discovered an **alien numeral system** composed of some number of digits, which may or may not be the same as those used in decimal.

For example, if the alien numeral system were represented as:

```
oF8
```

Then the numbers one through ten would be represented as:

```
F, 8, Fo, FF, F8, 8o, 8F, 88, Foo, FoF
```

We would like to work with numbers in **arbitrary alien systems**. More generally, the goal is to convert a number written in one alien system into a number written in another alien system.

---

## Input

- The first line of input gives the number of test cases `T` (`T ≤ 100`).
- `T` test cases follow.

Each test case consists of a single line formatted as:

```
alien_number source_language target_language
```

Where:
- `alien_number` is a number written in the source alien numeral system
- `source_language` is a string listing the digits of the source system, ordered from **lowest to highest value**
- `target_language` is a string listing the digits of the target system, ordered from **lowest to highest value**

Additional guarantees:
- No digit is repeated in any language representation
- All digits in `alien_number` appear in the source language
- The first digit of `alien_number` is **not** the lowest-valued digit of the source language (i.e., no leading zero)
- Each digit is either:
  - A number `0–9`
  - An uppercase or lowercase letter
  - One of the following symbols:

```
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

You may assume:
- The number in decimal is **positive** and at most `1,000,000,000`
- All languages have at most **94 digits**

---

## Output

For each test case, output one line in the following format:

```
Case #x: result
```

Where:
- `x` is the test case number (starting from 1)
- `result` is the alien number translated from the source language to the target language

---

## Sample Input

```
4
9 0123456789 oF8
Foo oF8 0123456789
13 0123456789abcdef 01
CODE O!CDE? A?JM!.
```

## Sample Output

```
Case #1: Foo
Case #2: 9
Case #3: 10011
Case #4: JAM!
```

---

## Notes

- This problem reduces to converting a number from an arbitrary base to decimal, then converting from decimal to another arbitrary base.
- Care must be taken to handle large bases and non-numeric digit symbols.
