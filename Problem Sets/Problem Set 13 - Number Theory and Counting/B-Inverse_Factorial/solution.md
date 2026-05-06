# Solution: Inverse Factorial

## Goal
Solve the problem with factorial digit counting with logarithms. The implementation's main job is: Small factorials are recognized directly. For large inputs, the code adds log10(2), log10(3), and so on until the digit count matches the input length.

## Key idea
The solution is built around factorial digit counting with logarithms. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Small factorials are recognized directly. For large inputs, the code adds log10(2), log10(3), and so on until the digit count matches the input length.

## Step-by-step algorithm
1. Read the factorial value as a string so huge numbers do not overflow.
2. Check the small factorials directly because several have short digit lengths.
3. For larger inputs, keep a running sum of log10(i).
4. After each i, the digit count of i! is floor(sum)+1.
5. Stop when that digit count equals the input length.
6. Print the corresponding i.

## Example walkthrough
120 is matched directly as 5!. A huge input with 1000 digits is handled by finding when n! first reaches 1000 digits.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) where n is the recovered factorial argument; memory O(1) after reading the input string.

## Important details
The actual factorial value is never built for large cases.
