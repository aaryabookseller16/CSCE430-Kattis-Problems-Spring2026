
# Army Strength (Hard)

This is the harder version of the problem **armystrengtheasy**.

MechaGodzilla is invading again. Godzilla and friends are preparing for war. Each army has many monsters, each with a positive integer strength. The war is a series of battles. In each battle, the weakest monsters still alive are compared. If the weakest monsters are in the same army, one of them is killed at random. If both armies have a weakest monster of the same strength, the weakest monster from MechaGodzilla's army is killed. The war ends when one army has no monsters left. The remaining army wins.

Given the strengths of all monsters in both armies, determine who wins the war.

---

## Input

- The first line contains an integer T (T <= 50), the number of test cases.
- Each test case is preceded by a blank line.
- Each test case starts with two integers NG and NM, the number of monsters in Godzilla's and MechaGodzilla's army. (1 <= NG, NM <= 100000)
- The next line contains NG integers, the strengths of Godzilla's monsters.
- The next line contains NM integers, the strengths of MechaGodzilla's monsters.
- All strengths are at most 1,000,000,000.

---

## Output

For each test case, output one line:

- `Godzilla` if Godzilla's army is guaranteed to win.
- `MechaGodzilla` if MechaGodzilla's army is guaranteed to win.
- `uncertain` otherwise.

---

## Example

### Input
```
2

1 1
1
1

3 2
1 3 2
5 5
```

### Output
```
Godzilla
MechaGodzilla
```
