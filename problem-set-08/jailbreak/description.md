# Problem E - Jailbreak

John is on a mission to get two people out of prison. This particular prison is a one-story building, and John has managed to get hold of a detailed floor plan showing all walls, doors, and the locations of the two prisoners he needs to free.

Doors are the main issue. Every door is normally opened remotely from a control room, but John can force doors open by other means. Once a door is opened, it stays open. However, opening a door takes time, so John wants to minimize how many doors need to be opened in total.

John can move freely around the outside of the building. The two prisoners can move through the prison as well. Your task is to determine the minimum number of doors that must be opened so that both prisoners can escape.

## Input

The first line contains a single integer `t` (`1 <= t <= 100`), the number of test cases.

Each test case starts with a line containing two integers `h` and `w` (`2 <= h, w <= 100`), the height and width of the map.

Then follow `h` lines of length `w`, describing the prison:

- `.` means an empty space
- `*` means a wall
- `#` means a door
- `$` means one of the two prisoners

John may move freely outside the building. There are always exactly two prisoners on the map, and for each prisoner there is guaranteed to be at least one path from that prisoner to the outside.

## Output

For each test case, print one integer: the minimum number of doors that must be opened so that both prisoners can escape.

## Sample Input 1

```text
3
5 9
****#****
*..#.#..*
****.****
*$#.#.#$*
*********
5 11
*#*********
*$*...*...*
*$*.*.*.*.*
*...*...*.*
*********.*
9 9
*#**#**#*
*#**#**#*
*#**#**#*
*#**.**#*
*#*#.#*#*
*$##*##$*
*#*****#*
*.#.#.#.*
*********
```

## Sample Output 1

```text
4
0
9
```
