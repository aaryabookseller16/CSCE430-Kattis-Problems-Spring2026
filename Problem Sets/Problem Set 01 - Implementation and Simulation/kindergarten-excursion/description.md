

# Problem C — Kindergarten Excursion

## Overview

The kindergarten teachers have finally managed to line up all the kids for their walk to the bus station and the weekly excursion. However, today different kids are going to different destinations. To avoid chaos when they arrive at the bus station, the kids must be organized while staying in a single line:

- Kids going to the **zoo** should be at the **beginning** of the line
- Kids going to the **lake** should be in the **middle**
- Kids going to the **science museum** should be at the **end**

Since it takes a lot of time to line up the kids, **no kid may step out of the line**. The only allowed operation is that **two adjacent kids may swap places**.

The teachers want to know whether they can organize the line in time — and if so, what the **minimum number of swaps** required is.

---

## Task

You are given a sequence of numbers consisting only of `0`, `1`, and `2`, representing the excursion destination of each kid from **first to last** in the line:

- `0` — zoo
- `1` — lake
- `2` — science museum

The line should be rearranged so that:

- All `0`s come first
- Followed by all `1`s
- Ending with all `2`s

Only **adjacent swaps** are allowed.

Determine the **minimum number of swaps** needed to organize the line correctly.

---

## Input

- The input consists of a **single line** containing a string of characters `0`, `1`, and `2`.
- The length of the string is at most **1,000,000** characters.

---

## Output

- Output **one integer**: the minimum number of swaps required to arrange the kids in the correct order.

---

## Sample Input

```
10210
```

## Sample Output

```
5
```

---

## Notes

- The order must be achieved using **only adjacent swaps**.
- Efficient algorithms are required due to the large input size.
- The problem is equivalent to counting the minimum number of inversions needed to sort the sequence into `0`s, then `1`s, then `2`s.