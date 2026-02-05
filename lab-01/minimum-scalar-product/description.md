
# Minimum Scalar Product

You are given two vectors v1 = (x1, x2, ..., xn) and v2 = (y1, y2, ..., yn).
The scalar product of these vectors is a single number:

x1*y1 + x2*y2 + ... + xn*yn

You may permute (reorder) the coordinates of each vector independently.
Choose two permutations so that the scalar product is as small as possible, and output that minimum scalar product.

---

## Input

- The first line contains an integer T (T <= 10), the number of test cases.
- For each test case:
  - The first line contains an integer n (1 <= n <= 800).
  - The next line contains n integers, the coordinates of v1.
  - The next line contains n integers, the coordinates of v2.
- Each coordinate is in the range -100000 to 100000.

---

## Output

For each test case, output a line:

Case #X: Y

- X is the test case number, starting from 1.
- Y is the minimum scalar product of the two vectors after reordering.

---

## Example

### Input
```
2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1
```

### Output
```
Case #1: -25
Case #2: 6
```
