

# Problem C — Kindergarten Excursion

## Overview

The kindergarten teachers had finally managed to get all the kids in a line for the walk to the bus station and the weekly excursion. What they hadn’t thought of was the fact that today different kids were supposed to go to different excursions. They should walk as one line to the bus station, but to avoid total chaos when they arrive there:

- Kids going to the **zoo** should be at the **beginning** of the line
- Kids going to the **lake** should be in the **middle**
- The rest, going to the **science museum**, should be at the **end**

Since it takes a lot of time to get all the kids to stand in a line, **no kid may step out of the line**. To get the line organized after excursion group, **kids standing next to each other can swap places**.

The kindergarten teachers now wonder if they will have time to do this and still catch their bus.

---

## Task

You are given a sequence of numbers `0`, `1`, and `2`, denoting the excursion destination of each kid from **first to last** in the line. Pairs of adjacent kids may swap positions, and the line should be organized by destination number, starting with `0` and ending with `2`.

What is the **minimum number of swaps** required to organize the line?

---

## Input

- The input consists of **one line** containing a string of characters `0`, `1`, and `2`, denoting the destinations of the kids.
- The length of the string is at most **1,000,000** characters.

---

## Output

- Output **one line** with one integer — the minimum number of swaps needed to get the kids in order.

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

- Only **adjacent swaps** are allowed.
- The problem must be solved efficiently due to the large input size.
- Conceptually, this is a minimum-adjacent-swaps sorting problem for three distinct values.