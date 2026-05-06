# Solution: A1 Paper

## Goal
Solve the problem with greedy paper assembly. The implementation's main job is: Starting from one needed A1 sheet, each smaller size doubles the needed count. Tape is added for each join level until enough sheets exist.

## Key idea
The solution is built around greedy paper assembly. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Starting from one needed A1 sheet, each smaller size doubles the needed count. Tape is added for each join level until enough sheets exist.

## Step-by-step algorithm
1. Read how many sheets of each A-size are available.
2. Start with needing one A1 sheet.
3. Move from A2 downward to smaller sizes.
4. At size Ai, add the tape length needed for the joins at that level.
5. Check whether the available Ai sheets can satisfy the current need.
6. If not, double the unmet need for the next smaller size.
7. Print the tape length once enough paper exists, or impossible if all sizes run out.

## Example walkthrough
If one A2 sheet is missing, two A3 sheets can replace it with one strip of tape.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(n) memory for counts.

## Important details
The long side formula comes from ISO paper dimensions.
