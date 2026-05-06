# Gopher II

The gopher family, having averted the canine threat, must now face a new predator.

There are `n` gophers and `m` gopher holes, each at distinct `(x, y)` coordinates. A hawk arrives, and any gopher that does not reach a hole within `s` seconds is vulnerable to being eaten. Each hole can save at most one gopher. All gophers run at the same speed `v`.

Find an escape plan that minimizes the number of vulnerable gophers.

## Input

The input contains several test cases and ends at EOF.

Each test case begins with four positive integers, each less than `100`:

- `n`: the number of gophers
- `m`: the number of holes
- `s`: the number of seconds before the hawk arrives
- `v`: the running speed in metres per second

The next `n` lines contain the coordinates of the gophers.

The following `m` lines contain the coordinates of the gopher holes.

All coordinates are decimal numbers between `0` and `100` with one digit after the decimal point. All distances are in metres, all times are in seconds, and all velocities are in metres per second.

## Output

For each test case, print one line containing the number of vulnerable gophers.

## Sample Input

```text
2 2 5 10
1.0 1.0
2.0 2.0
100.0 100.0
20.0 20.0
```

## Sample Output

```text
1
```
