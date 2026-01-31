# Railway Runner

## Problem
You are given a railway pattern with **3 columns** and **N rows**. Each cell is one of:
- `.` rail (ground)
- `*` train (roof)
- `/` ladder to a train roof

You start on **row 1** (top) on any **rail** cell (`.`). Your goal is to reach **row N** (bottom) in any column.

Movement rules:
- You may move left/right within the same row **only** between two rails (`.`) or two trains (`*`) that are adjacent.
- You may move forward (down). You can never move backward (up), and no diagonal moves are allowed.
- You can only get onto a train from another adjacent train or by climbing a ladder (`/`).
- From a train roof you may jump down to the rail **below** in the same column.
- While on a ladder, you must move forward to the corresponding train roof (the ladder row is forced).
- Input is valid: each ladder is preceded by a rail and followed by a train.

Determine if it is possible to reach the last row.

## Input
- The first line contains an integer `N` (`1 <= N <= 100000`).
- The next `N` lines each contain exactly 3 characters from `{'.', '*', '/'}`.

## Output
Print `YES` if you can reach the last row, otherwise print `NO`.

## Sample Input 1
```text
10
*.*
*..
**/
..*
.**
.**
/**
***
*..
.**
```

## Sample Output 1
```text
YES
```

## Sample Input 2
```text
16
...
///
***
...
*.*
./.
.*.
.*.
.*.
.*.
...
./.
***
***
***
...
```

## Sample Output 2
```text
NO
```
