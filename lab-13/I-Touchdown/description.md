# Problem I: Touchdown!

In this simplified football drive, a team starts at its own 20 yard line on a
100 yard field.

Each play moves the team forward or backward by some number of yards:

- positive yards move toward the opponent's endzone
- negative yards move toward the team's own endzone

The team has up to four plays to gain 10 yards. If they gain those 10 yards,
they get a first down and receive another up to four plays from the new position.

If the team's position reaches at least `100`, they score a touchdown and the
drive ends.

If the team's position reaches `0` or below, they suffer a safety and the drive
ends.

If the team uses four plays without getting a first down, the drive ends with
`Nothing`. If neither event happens after all recorded plays, the result is also
`Nothing`.

## Input

The first line contains one integer `N`, where:

```text
1 <= N <= 15
```

This is the number of plays in the drive.

The next line contains `N` integers, the yard gains or losses for the plays.
Each value is between `-100` and `100`, exclusive.

## Output

Print one word:

- `Touchdown` if the team scores a touchdown
- `Safety` if the team suffers a safety
- `Nothing` if neither happens

Once the result is known, ignore the rest of the plays.

## Sample Input 1

```text
9
10 3 8 22 -4 16 8 3 14
```

## Sample Output 1

```text
Touchdown
```

## Sample Input 2

```text
10
9 15 2 -5 3 8 18 3 25 2
```

## Sample Output 2

```text
Nothing
```

## Idea

Start at yard line `20`, with the first first-down marker at yard line `30`.

After each play:

- check for touchdown or safety
- check whether the first-down marker was reached
- otherwise count the play as one of the four attempts
