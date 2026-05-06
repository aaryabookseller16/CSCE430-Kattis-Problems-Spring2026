# Solution: Fractional Lotion

## Goal
Solve the problem with number theory using divisor counts. The implementation's main job is: The equation 1/x + 1/y = 1/n transforms so the number of unordered solutions is based on the divisor count of n^2.

## Key idea
The solution is built around number theory using divisor counts. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The equation 1/x + 1/y = 1/n transforms so the number of unordered solutions is based on the divisor count of n^2.

## Step-by-step algorithm
1. Read n from the input text 1/n.
2. Factor n into prime powers.
3. For n^2, each exponent doubles, so its divisor count multiplies by 2*exponent+1.
4. The number of ordered factor choices equals the divisor count of n^2.
5. Convert ordered pairs to unordered pairs with (divisor_count + 1) / 2.
6. Print that value.

## Example walkthrough
For n=2, the valid unordered pairs are (3,6) and (4,4), so the answer is 2.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(sqrt n) per input line; memory O(1).

## Important details
The formula is (d(n^2)+1)/2 for unordered pairs.
