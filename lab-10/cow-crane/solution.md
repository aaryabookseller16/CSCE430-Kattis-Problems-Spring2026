# Solution: Cow Crane

## Goal
Solve the problem with case analysis on two delivery orders. The implementation's main job is: The code tries finishing Monica first and Lydia first. For each order it checks direct delivery and a version where the second cow is moved partway early.

## Key idea
The solution is built around case analysis on two delivery orders. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code tries finishing Monica first and Lydia first. For each order it checks direct delivery and a version where the second cow is moved partway early.

## Step-by-step algorithm
1. Read current cow positions, target positions, and deadlines.
2. Try both orders: finish cow A first or cow B first.
3. First test the simple route where the crane fully moves one cow, then the other.
4. If that misses a deadline, test whether carrying the second cow partway before finishing the first can help.
5. Use the first cow deadline to compute the allowed temporary-drop interval for the second cow.
6. Choose the best temporary point by clamping a median-like point to that interval.
7. If either order meets both deadlines, print possible; otherwise print impossible.

## Example walkthrough
If the first deadline is tight, the crane may have to place that cow before doing anything else.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(1) time and memory.

## Important details
The doubled-coordinate math avoids half-position rounding issues.
