

# Problem F — Pivot

## Overview

An **O(n) partition algorithm** partitions an array `A` around a pivot element (where the pivot is a member of `A`) into three parts:

- A left subarray containing elements that are **≤ pivot**
- The **pivot** itself
- A right subarray containing elements that are **> pivot**

Partition algorithms are an integral part of the popular sorting algorithm **Quicksort**. Usually, the choice of pivot is randomized so that Quicksort has an expected running time of **O(n log n)**.

---

## Problem Description

In this problem, you are given an array `A` with `n` **distinct integers**. The array is partitioned using **one of its elements as the pivot**, producing a transformed array `A'`.

Given the transformed array `A'`, your task is to determine **how many integers could have been the chosen pivot**.

An element `x` in `A'` can be a valid pivot if:
- All elements **to the left** of `x` are **less than or equal to** `x`
- All elements **to the right** of `x` are **greater than** `x`

---

## Example

If:

```
A' = {2, 1, 3, 4, 7, 5, 6, 8}
```

Then **3 integers** — `{3, 4, 8}` — could have been the pivot.

For example, `4` could be the pivot because:
- `{2, 1, 3}` to the left of `4` are all smaller than `4`
- `{7, 5, 6, 8}` to the right of `4` are all greater than `4`

Other integers cannot be pivots. For instance, `7` cannot be the pivot because `{5, 6}` to its right are smaller than `7`.

---

## Input

- The input consists of **two lines**:
  1. An integer `n` (`3 ≤ n ≤ 100000`)
  2. A line containing `n` **distinct 32-bit signed integers**, representing the transformed array `A'`

---

## Output

- Output the required answer as a **single integer** on one line.

---

## Sample Input 1

```
8
2 1 3 4 7 5 6 8
```

## Sample Output 1

```
3
```

---

## Sample Input 2

```
7
1 2 3 4 5 7 6
```

## Sample Output 2

```
5
```

---

## Notes

- All integers in the array are **distinct**.
- The solution must run in **O(n)** time.
- Prefix maximums and suffix minimums are useful for solving this problem efficiently.