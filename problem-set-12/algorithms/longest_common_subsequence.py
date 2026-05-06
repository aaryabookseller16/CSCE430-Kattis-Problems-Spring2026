def longest_common_subsequence(s1, s2):
    """
    Find the length of LCS between two strings.
    
    dp[i][j] = length of LCS for first i chars of s1 
               and first j chars of s2
    """
    
    m = len(s1)
    n = len(s2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, extend the LCS
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            # If they don't match, take the longer LCS 
            # from either removing from s1 or removing from s2
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


def longest_common_subsequence_with_string(s1, s2):
    """
    Find both the length AND the actual LCS string.
    """
    
    m = len(s1)
    n = len(s2)
    
    # Build DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the actual LCS by backtracking
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        # If characters match, this character is part of LCS
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        
        # If they don't match, go to whichever cell is larger
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Reverse because we built it backwards
    return ''.join(reversed(lcs)), dp[m][n]


# Test cases
print(longest_common_subsequence("ABCDGH", "AEDFHR"))  # 3
print(longest_common_subsequence_with_string("ABCDGH", "AEDFHR"))  # ("ADH", 3)
print(longest_common_subsequence("AGGTAB", "GXTXAYB"))  # 4