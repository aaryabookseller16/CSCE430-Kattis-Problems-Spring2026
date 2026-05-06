def edit_distance(s1, s2):
    """
    Calculate the minimum edit distance between two strings.
    
    dp[i][j] = minimum edits to transform first i chars of s1 
               into first j chars of s2
    
    Time: O(m * n), Space: O(m * n)
    """
    
    m = len(s1)
    n = len(s2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: transforming to/from empty string
    for i in range(m + 1):
        dp[i][0] = i  # Delete all i characters
    
    for j in range(n + 1):
        dp[0][j] = j  # Insert all j characters
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, no edit needed
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            
            # If they don't match, take minimum of three operations
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # Delete from s1
                    dp[i][j-1],      # Insert into s1
                    dp[i-1][j-1]     # Replace character
                )
    
    return dp[m][n]


# Test cases
print(edit_distance("kitten", "sitting"))      # 3
print(edit_distance("cat", "bat"))             # 1
print(edit_distance("", "abc"))                # 3
print(edit_distance("saturday", "sunday"))    # 3