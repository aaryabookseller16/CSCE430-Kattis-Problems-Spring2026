# Solution: Alien Numbers

## Goal
Solve the problem with base conversion through decimal. The implementation's main job is: The source digit alphabet maps each symbol to a value. The code evaluates the source number in base len(source), then repeatedly divides by the target base.

## Key idea
The solution is built around base conversion through decimal. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The source digit alphabet maps each symbol to a value. The code evaluates the source number in base len(source), then repeatedly divides by the target base.

## Step-by-step algorithm
1. Map every source digit symbol to its numeric value.
2. Evaluate the alien number from left to right in the source base.
3. Repeatedly divide the decimal value by the target base.
4. Use each remainder as a target digit.
5. Reverse the collected target digits.
6. Print the converted number with the case label.

## Example walkthrough
With source digits oF8, symbol F has value 1 and 8 has value 2.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(length of number + number of target digits); memory O(number of target digits).

## Important details
The checked-in code may print an empty string for a true zero value because the zero case is overwritten after conversion.
