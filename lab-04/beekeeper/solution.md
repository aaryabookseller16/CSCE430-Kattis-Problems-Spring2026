# Solution: Beekeeper

## Goal
Solve the problem with string scanning. The implementation's main job is: Each word is scanned for adjacent double-vowel pairs. The word with the largest count is printed.

## Key idea
The solution is built around string scanning. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Each word is scanned for adjacent double-vowel pairs. The word with the largest count is printed.

## Step-by-step algorithm
1. Read the number of words in the case.
2. For each word, scan adjacent two-letter windows.
3. Count windows equal to aa, ee, ii, oo, uu, or yy.
4. Keep the word with the highest double-vowel count.
5. If later words have the same count, keep the earlier best word.
6. Print the best word for the case.

## Example walkthrough
bookkeeper has oo and ee, so it scores at least 2.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(total characters) per case; memory O(1) besides input tokens.

## Important details
The counted pairs are aa, ee, ii, oo, uu, and yy.
