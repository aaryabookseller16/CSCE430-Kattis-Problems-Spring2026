# Solution: Cat Coat Colors

## Goal
Solve the problem with probability enumeration over genotypes and gametes. The implementation's main job is: The code expands each visible parent color into possible hidden genotypes with probabilities, enumerates gametes and kitten sex, then totals coat-color probabilities.

## Key idea
The solution is built around probability enumeration over genotypes and gametes. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code expands each visible parent color into possible hidden genotypes with probabilities, enumerates gametes and kitten sex, then totals coat-color probabilities.

## Step-by-step algorithm
1. List every hidden case that can produce the visible input.
2. Attach the correct probability to each hidden case.
3. Enumerate every possible child/event outcome from those cases.
4. Multiply probabilities along the chosen path.
5. Add the probability into the bucket for the visible result.
6. Sort or format the buckets as required.
7. Print each nonzero result.

## Example walkthrough
A tortie mother can pass O or o, so daughters may become tortie depending on the father red gene.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Constant time for the fixed gene model; memory O(number of colors).

## Important details
Results are sorted by descending probability, then alphabetically.

## Other implementations in this folder
- `solution_table.md` has its own markdown explanation.
