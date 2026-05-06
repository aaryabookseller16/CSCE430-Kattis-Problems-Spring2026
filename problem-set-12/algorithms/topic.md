# Algorithm Snippets

This folder contains standalone reference implementations, not individual problem submissions.

## Topics
- **KMP:** prefix-function string matching. Example: after matching a partial pattern, KMP reuses the longest prefix that is also a suffix instead of restarting. Complexity: O(n+m).
- **Longest common subsequence:** dynamic programming over two strings. Example: LCS of ABCD and ACBD has length 3. Complexity: O(nm).
- **Edit distance:** dynamic programming for insert, delete, and replace operations. Example: changing cat to cut costs 1 replacement. Complexity: O(nm).
- **LCP array:** suffix-array-related longest-common-prefix processing. Example: adjacent suffixes in sorted order share a prefix length stored in the LCP array. Complexity depends on the implementation in the file.

These files support the string-algorithm topics used in Problem Set 12.
