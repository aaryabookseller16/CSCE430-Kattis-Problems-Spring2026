def build_lps_array(pattern):
    """Build the LPS (Longest Proper Prefix which is also Suffix) array."""
    m = len(pattern)
    lps = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        
        lps[i] = j
    
    return lps


def kmp_search(text, pattern):
    """Find all occurrences of pattern in text using KMP algorithm."""
    n = len(text)
    m = len(pattern)
    
    if m == 0 or m > n:
        return []
    
    lps = build_lps_array(pattern)
    matches = []
    j = 0
    
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == m:
            matches.append(i - m + 1)
            j = lps[j - 1]
    
    return matches