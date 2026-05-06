# Problem E — Path Tracing

## Overview

Billy likes to wander around. Each day he follows a sequence of **up**, **down**, **left**, and **right** moves. At the end of the day, he would like to know where he’s been.

Your task is to help by writing a program that reads a sequence of moves Billy makes on a given day and produces a **map showing the path he traveled**.

---

## Input

- Input consists of a sequence of **up to 500 moves**, one move per line, until **end of file**.
- Each move is one of:
  - `left`
  - `right`
  - `up`
  - `down`

---

## Output

Print a map of the path described by the sequence of moves, following these rules:

- Mark the **start location** with `S`
- Mark the **end location** with `E`
- Mark all other visited locations with `*`
- Use **spaces** to indicate parts of the map that were **not visited** by the path
- Outline the entire map with a rectangle made of the `#` character

Additional constraints:
- The map must be the **smallest rectangle** that contains the entire path
- The path will **never start and end at the same location**
- Do **not** print any extra spaces outside the map outline

---

## Sample Input

```
down
down
left
left
up
up
up
left
left
```

## Sample Output

```
#######
#E**  #
#  * S#
#  * *#
#  ***#
#######
```

---

## Notes

- Input is read until **EOF**, so standard input handling is required.
- Tracking the minimum and maximum visited coordinates is necessary to determine the map bounds.
- Care must be taken to format output **exactly**, as extra spaces will cause incorrect results.
