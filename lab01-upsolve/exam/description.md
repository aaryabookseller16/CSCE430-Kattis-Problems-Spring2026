
# Exam

Your friend and you took the same true/false exam. You know your own answers, your friend's answers, and how many of your friend's answers were correct.

Compute the maximum possible score you could have gotten.

---

## Input

- The first line contains an integer k, the number of correct answers on your friend's exam.
- The second line contains a string of characters, your answers.
- The third line contains a string of characters, your friend's answers.

Each character is either `T` or `F`. The length of the strings is the number of questions n.

Bounds: 1 <= n <= 1000 and 0 <= k <= n.

---

## Output

Output a single integer: the maximum number of questions you could have gotten correct.

---

## Example 1

### Input
```
3
FTFFF
TFTTT
```

### Output
```
2
```

## Example 2

### Input
```
6
TTFTFFTFTFF
TTTTFFTTTTT
```

### Output
```
9
```
