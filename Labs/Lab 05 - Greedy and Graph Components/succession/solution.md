# Solution: Succession

## Goal
Solve the problem with topological propagation of blood fractions. The implementation's main job is: The founder has blood value 1. Each child receives half from each parent, and people are processed after both parents are known.

## Key idea
The solution is built around topological propagation of blood fractions. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The founder has blood value 1. Each child receives half from each parent, and people are processed after both parents are known.

## Step-by-step algorithm
1. Read the factorial value as a string so huge numbers do not overflow.
2. Check the small factorials directly because several have short digit lengths.
3. For larger inputs, keep a running sum of log10(i).
4. After each i, the digit count of i! is floor(sum)+1.
5. Stop when that digit count equals the input length.
6. Print the corresponding i.

## Example walkthrough
If Alice has founder blood 1 and Bob has 0, their child has 0.5.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n+m) time and memory over family records and claimants.

## Important details
The claimant with maximum founder blood is printed.
