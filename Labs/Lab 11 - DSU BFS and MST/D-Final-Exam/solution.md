# Solution: Final Exam

## Goal
Solve the problem with one-position shift comparison. The implementation's main job is: Hanh wrote answer i+1 on line i, so the score is the number of adjacent equal answers.

## Key idea
The solution is built around one-position shift comparison. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Hanh wrote answer i+1 on line i, so the score is the number of adjacent equal answers.

## Step-by-step algorithm
1. Read all correct answers.
2. Hanh wrote each answer one line too early, so line i contains the answer for i+1.
3. Compare answer[i] with answer[i+1] for every i before the last question.
4. Each equality means Hanh accidentally got that line correct.
5. The last line is blank and cannot score.
6. Print the count.

## Example walkthrough
If true answers are A B B, the shifted sheet has B B blank, so only line 2 matches.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(n) memory for the answer list.

## Important details
The final blank line can never score.
