

# Problem A — 1-D Frogger (Easy)

## Overview

*Frogger* is a classic 2‑D video game that challenges the player to move a frog safely across a traffic‑filled road and a hazardous river. Less well known is that Frogger actually began as a prototype board game based on a **1‑D concept** at a now‑defunct toy company. After spending millions of dollars following the advice of consultants, company executives realized that the resulting game was almost completely deterministic, and therefore not much fun to play. They sold the Frogger rights to a video game company in an attempt to recoup some of the development costs. The rest, as they say, is video game history.

The original 1‑D Frogger design, however, makes for an excellent programming problem.

---

## Game Description

The board consists of a single row of **n** squares, indexed `1` through `n` from left to right. Each square contains a **non‑zero integer**.

To start the game:
- The frog is placed on square `s`.
- A **magic number** `m` is selected. The magic number is guaranteed to appear on at least one board square.

The player repeatedly applies the following rule until the game ends:

- If the frog is on a square containing a **positive integer** `k`, the frog hops **right** by `k` squares.
- If the frog is on a square containing a **negative integer** `k`, the frog hops **left** by `|k|` squares.

Hop distance is measured in board squares.

---

## Game End Conditions

The game ends immediately when the frog encounters **one** of the following four fates:

1. **magic** — The frog lands on a square containing the magic number `m` (this is the only winning outcome).
   - If the frog starts on a square containing `m`, the player wins immediately (after `0` hops).
2. **left** — The frog falls off the **left end** of the board.
3. **right** — The frog falls off the **right end** of the board.
4. **cycle** — The frog lands on a square it has visited before, becoming trapped in a cycle.

Let `h ≥ 0` be the number of hops the frog makes before the game ends.

Your task is to determine **the frog’s fate** and the corresponding value of `h`.

---

## Input

- The first line contains three space‑separated integers:
  - `n` — number of board squares (`1 ≤ n ≤ 200`)
  - `s` — starting square index (`1 ≤ s ≤ n`)
  - `m` — the magic number
- The second line contains `n` space‑separated **non‑zero integers**, representing the board squares from left to right.
  - Each integer is in the range `[-200, 200]`
  - The magic number `m` is guaranteed to appear at least once

---

## Output

Output **two lines**:

1. A single word describing the frog’s fate, one of:
   - `magic`
   - `left`
   - `right`
   - `cycle`
2. An integer `h`, the number of hops made before the game ends.

---

## Sample Input 1

```
6 4 42
-9 1 42 -2 -3 -3
```

## Sample Output 1

```
magic
2
```

---

## Sample Input 2

```
8 2 13
7 5 4 2 13 -2 -3 6
```

## Sample Output 2

```
cycle
4
```

---

## Notes

- The game is deterministic.
- Tracking visited positions is necessary to detect cycles.
- The maximum board size is small, so a direct simulation is sufficient.

---

## Footnotes

1. This story might be apocryphal.
2. Deterministic games can still be fun — just not this one.