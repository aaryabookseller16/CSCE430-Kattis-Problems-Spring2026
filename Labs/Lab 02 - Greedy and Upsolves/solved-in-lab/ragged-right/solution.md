# Solution: Ragged Right

## Goal
Solve the problem with line length penalty sum. The implementation's main job is: The longest line length is the target. Every line except the last contributes the square of its unused width.

## Key idea
The solution is built around line length penalty sum. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The longest line length is the target. Every line except the last contributes the square of its unused width.

## Step-by-step algorithm
1. Read every input line as part of the paragraph.
2. Find the maximum line length.
3. Ignore the final line for scoring.
4. For every earlier line, compute max_length - current_length.
5. Square that difference and add it to the total raggedness.
6. Print the total.

## Example walkthrough
If max length is 10 and a non-last line has length 7, it adds 9.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(number of lines) time and O(number of lines) memory.

## Important details
The final line is ignored by definition.
