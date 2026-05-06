def build_suffix_array(text):
    """
    Build suffix array - indices sorted by suffix.
    
    Simple but slow version: O(n² log n)
    """
    n = len(text)
    
    # Step 1: Create list of (suffix_string, original_index)
    suffixes = []
    for i in range(n):
        suffix = text[i:]
        suffixes.append((suffix, i))
    
    # Step 2: Sort by the suffix strings
    suffixes.sort()  # Sorts alphabetically
    
    # Step 3: Extract just the indices
    sa = [index for suffix_str, index in suffixes]
    
    return sa


# Test with "BANANA"
text = "BANANA"
sa = build_suffix_array(text)
print(f"Text: {text}")
print(f"Suffix Array: {sa}")
print("\nSorted Suffixes:")
for idx in sa:
    print(f"  Position {idx}: {text[idx:]}")

def build_lcp_array(text, sa):
    """
    Build the LCP (Longest Common Prefix) array.
    
    LCP[i] = length of common prefix between 
             suffix at sa[i] and suffix at sa[i+1]
    
    Time: O(n), Space: O(n)
    """
    n = len(text)
    lcp = [0] * n
    rank = [0] * n
    
    # Step 1: Build rank array (inverse of suffix array)
    # rank[i] tells us the position of suffix starting at i in the sorted order
    for i in range(n):
        rank[sa[i]] = i
    
    # Step 2: Calculate LCP values using the rank array
    h = 0
    for i in range(n):
        if rank[i] > 0:
            # Find the suffix that comes before current suffix in sorted order
            j = sa[rank[i] - 1]
            
            # Count matching characters
            while i + h < n and j + h < n and text[i + h] == text[j + h]:
                h += 1
            
            lcp[rank[i]] = h
            
            # Decrease h for next iteration
            if h > 0:
                h -= 1
    
    return lcp


def longest_repeated_substring(text):
    """
    Find the longest substring that appears at least twice.
    
    The longest repeated substring is the character(s) with 
    the maximum LCP value!
    
    Time: O(n log n), Space: O(n)
    """
    
    # Step 1: Build suffix array
    sa = build_suffix_array(text)
    
    # Step 2: Build LCP array
    lcp = build_lcp_array(text, sa)
    
    # Step 3: Find maximum LCP value
    max_lcp = max(lcp) if lcp else 0
    
    if max_lcp == 0:
        return "", 0
    
    # Step 4: Find which suffix has the maximum LCP
    max_idx = lcp.index(max_lcp)
    
    # Step 5: Extract the substring
    # The longest repeated substring starts at position sa[max_idx]
    # and has length max_lcp
    substring = text[sa[max_idx]:sa[max_idx] + max_lcp]
    
    return substring, max_lcp


# Complete example
print("=== SUFFIX ARRAY ===")
text = "BANANA"
sa = build_suffix_array(text)
print(f"Text: {text}")
print(f"Suffix Array: {sa}\n")

print("=== LCP ARRAY ===")
lcp = build_lcp_array(text, sa)
print(f"LCP: {lcp}\n")

print("=== INTERPRETATION ===")
for i in range(len(lcp)):
    if i == 0:
        print(f"LCP[{i}] = {lcp[i]} (first suffix, no comparison)")
    else:
        suffix1 = text[sa[i-1]:]
        suffix2 = text[sa[i]:]
        print(f"LCP[{i}] = {lcp[i]} ('{suffix1}' vs '{suffix2}')")

print("\n=== LONGEST REPEATED SUBSTRING ===")
text2 = "ABABA"
sa2 = build_suffix_array(text2)
substring, length = longest_repeated_substring(text2)
print(f"Text: {text2}")
print(f"Suffix Array: {sa2}")
print(f"Longest repeated: '{substring}' (length {length})")

# More test cases
print("\n=== MORE EXAMPLES ===")
examples = ["MISSISSIPPI", "ABCABCAB", "GEEKSFORGEEKS"]
for ex in examples:
    sub, length = longest_repeated_substring(ex)
    print(f"Text: {ex} → Longest repeated: '{sub}' (length {length})")