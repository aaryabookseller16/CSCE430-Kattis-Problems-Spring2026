# read input
# store input as an array
s = input().strip()
user_input_list = [int(ch) for ch in s]
n = len(user_input_list)

swaps = 0
no_of_1s = 0
no_of_2s = 0

for element in user_input_list:
    if element == 0: # it has to move from all 1s and 2s
        swaps += no_of_1s + no_of_2s
    elif element == 1: # it must move past all 2s
        swaps += no_of_2s
        no_of_1s +=1
    else: # no need to increment swaps as 2 is the max element
        no_of_2s += 1

print(swaps)