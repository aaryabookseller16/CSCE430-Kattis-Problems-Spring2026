
# Working at the Restaurant

Tom is helping at a restaurant. Plates arrive from the waiter and must be passed to the dishwasher in the same order they arrived. Tom uses a single table with space for exactly two piles of plates, called pile 1 and pile 2. He always drops incoming plates onto the top of a pile, and he can only take plates from the top of a pile.

You are given a sequence of commands. For each command, output a valid transcript of operations that processes the plates in order and follows all the constraints.

---

## Input

The input contains multiple test cases (at most 50). Each test case begins with a line containing an integer N (1 <= N <= 1000), followed by N lines. Each of those lines is one of:

- DROP m
- TAKE m

Here m > 0 is the number of plates to drop or take. The sum M of all values of m from DROP commands in a test case does not exceed 100000. You may assume a TAKE m command is never given when there are fewer than m plates on the table.

The input ends with a line containing N = 0, which should not be processed.

---

## Output

For every test case, output a series of lines describing the operations Tom performs. Each line must be one of:

- DROP 1 m or DROP 2 m
- TAKE 1 m or TAKE 2 m
- MOVE 1->2 m or MOVE 2->1 m

These mean:

- DROP p m: repeat m times, take a plate from the waiter and drop it on top of pile p.
- TAKE p m: repeat m times, take a plate from the top of pile p and pass it to the dishwasher.
- MOVE a->b m: repeat m times, move a plate from the top of pile a to the top of pile b.

You must obey the commands in order. That means when you receive a TAKE m command, the total number of plates taken in your output for that command must be exactly m before you move on to the next command. Similarly, for a DROP m command, the total number of plates dropped must be exactly m before you move on.

Additional limits:

- Output at most 6N lines per test case.
- The total number of moved plates (the sum of all m values printed in your output) must be at most 6M.
- Print a blank line between outputs of different test cases.

Any output satisfying these conditions is accepted.

---

## Example

### Input
```
3
DROP 100
TAKE 50
TAKE 20
3
DROP 3
DROP 5
TAKE 8
0
```

### Output
```
DROP 2 100
MOVE 2->1 100
TAKE 1 50
TAKE 1 20

DROP 2 3
DROP 2 5
MOVE 2->1 8
TAKE 1 8
```
