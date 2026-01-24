

# Bus Numbers

Your favourite public transport company LS (we cannot use their real name here, so we permuted the letters) wants to change signs on all bus stops. Some bus stops have quite a few buses that stop there, and listing all the buses individually takes space.

If, for example, buses `141 142 143` stop at a bus stop, we can write `141-143` instead, which saves space. Note that for **only two buses**, this does **not** save space, so they should still be written individually.

You are given a list of bus numbers that stop at a bus stop. Your task is to output the **shortest possible representation** of this list.

---

## Input

- The first line contains an integer `N` (`1 ≤ N ≤ 1000`), the number of buses that stop at the bus stop.
- The second line contains `N` **distinct** space-separated integers between `1` and `1000`, representing the bus numbers.

---

## Output

Print the shortest representation of the bus numbers:

- Output the numbers in **sorted order**
- Use **single spaces** to separate entries
- Represent **three or more consecutive numbers** as `a-b`
- Do **not** compress sequences of length 1 or 2

---

## Example

### Input
```
6
180 141 174 143 142 175
```

### Output
```
141-143 174 175 180
```