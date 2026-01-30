t = int(input()) # number of cases we need to evaluate

# repeat logic for  t cases
for case_num in range(1, t + 1):
    alien_number, source, target = input().split()

    # base is defined by the number of symbols in the source language
    base = len(source)

    # source -> decimal
    key_idx = {}
    for i, character in enumerate(source):
        key_idx[character] = i
        
    # evaluate the value by breaking down the input into parts
    value = 0
    for character in alien_number:
        value = value * base + key_idx[character]
        
    target_base = len(target) # this is the base of the target language
    digits = []
    while value > 0:
        digits.append(target[value % target_base])
        value //= target_base # remove evaluated value from the number
        
    if value == 0: # edge case 
        result = target[0]
        

    result = "".join(reversed(digits))
    print(f"Case #{case_num}: {result}")