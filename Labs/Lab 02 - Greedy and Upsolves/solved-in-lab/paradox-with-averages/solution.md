# Solution: Paradox With Averages

## Goal
Solve the problem with average inequality test. The implementation's main job is: A CS student works if their IQ is below the CS average and above the Economics average. The code checks those two inequalities without recomputing averages.

## Key idea
The solution is built around average inequality test. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: A CS student works if their IQ is below the CS average and above the Economics average. The code checks those two inequalities without recomputing averages.

## Step-by-step algorithm
1. Read the CS and Economics student counts and IQ values.
2. Compute the total IQ of each group.
3. For each CS student, test whether removing that IQ increases the CS average.
4. The inequality for that is iq * N_CS < total_CS.
5. Test whether adding that IQ increases the Economics average: iq * N_E > total_Econ.
6. Count students satisfying both inequalities.
7. Print that count.

## Example walkthrough
A student with IQ 100 can raise both averages if CS average is 105 and Econ average is 95.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N_CS + N_E) per case; memory O(total students).

## Important details
Multiplication avoids floating-point division.
