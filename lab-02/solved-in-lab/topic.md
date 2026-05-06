# Solved In Lab Topics

This folder groups the Lab 2 problems that were solved during lab. The covered topics are greedy balancing, paper-size construction, digit-sum brute force, average inequalities, raggedness scoring, and right-to-left greedy adjustment.

## Problems
- **Ljutnja:** evenly distribute missing candies to minimize squared anger. Example: missing amounts 2,2,1 are better than 5,0,0. Complexity: O(n log n).
- **A1 Paper:** greedily combine smaller sheets until an A1 sheet can be formed. Example: two A3 sheets can replace one missing A2 sheet. Complexity: O(n).
- **The Easiest Problem Is This One:** try multipliers until digit sums match. Example: 3029 works with multiplier 37. Complexity depends on the found multiplier.
- **Paradox With Averages:** count CS students below the CS average and above the Economics average. Example: IQ 100 works if CS average is 105 and Econ average is 95. Complexity: O(n).
- **Ragged Right:** square the unused width of every non-last line. Example: max length 10 and line length 7 adds 9. Complexity: O(lines).
- **Thanos the Hero:** scan from right to left and reduce populations just enough to make them strictly ordered. Example: 5,2,3 becomes 1,2,3. Complexity: O(n).
