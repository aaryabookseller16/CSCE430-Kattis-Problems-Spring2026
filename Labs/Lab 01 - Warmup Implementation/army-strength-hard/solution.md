# Solution: Army Strength Hard

## Goal
Solve the problem with maximum comparison. The implementation's main job is: In this battle rule, the army with the strongest monster wins; ties favor Godzilla. The code reads only the maximum strength from each army.

## Key idea
The solution is built around maximum comparison. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: In this battle rule, the army with the strongest monster wins; ties favor Godzilla. The code reads only the maximum strength from each army.

## Step-by-step algorithm
1. Read the number of test cases.
2. For each test case, read both army sizes.
3. Scan Godzilla strengths and keep only the maximum value.
4. Scan MechaGodzilla strengths and keep only the maximum value.
5. If Godzilla maximum is at least MechaGodzilla maximum, Godzilla wins because ties eliminate MechaGodzilla first.
6. Otherwise MechaGodzilla has the stronger surviving monster and wins.
7. Print one winner per test case.

## Example walkthrough
If Godzilla max is 10 and MechaGodzilla max is 10, Godzilla wins the tie.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(NG+NM) per test case; memory O(1).

## Important details
Blank lines are ignored by token-based input.
