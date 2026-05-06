# Problem D: Final Exam

## Problem

Hanh took a multiple-choice final exam with `n` questions.

Each question has one correct answer: `A`, `B`, `C`, or `D`.

Hanh knew all the answers, but he made a mistake while filling out the answer
sheet. He wrote the answer for question `2` on line `1`, the answer for question
`3` on line `2`, and so on.

That means:

- line `1` got the answer meant for question `2`
- line `2` got the answer meant for question `3`
- ...
- line `n - 1` got the answer meant for question `n`
- line `n` was left blank

Every question is worth one point. A question is correct only if the written
answer on that line matches the true correct answer for that question.

Find Hanh's final score.

## Input

The first line contains an integer:

```text
n
```

where `1 <= n <= 1000`.

The next `n` lines each contain one character:

```text
A
B
C
D
```

The `i`th of these lines is the correct answer for question `i`.

## Output

Print one integer: Hanh's final score.

## Sample Input 1

```text
4
A
A
A
A
```

## Sample Output 1

```text
3
```

## Sample Input 2

```text
6
A
D
B
B
C
A
```

## Sample Output 2

```text
1
```

## Notes

Hanh gets question `i` correct if the correct answer for question `i + 1` equals
the correct answer for question `i`.

The last question cannot be correct because it was left blank.
