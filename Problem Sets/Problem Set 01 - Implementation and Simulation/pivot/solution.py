n = int(input())
input_list = list(map(int, input().split()))
no_of_pivots = 0

# keep track of the max at ith index
left_max_at_idx = [float("inf")]*n
left_max = float("-inf")
for i in range(n):
    left_max_at_idx[i] = left_max
    left_max = max(left_max, input_list[i])
    
# keep track of the min at the ith index
right_min_at_idx = [float("inf")]*n
right_min = float("inf")
for i in range(n-1, -1, -1):
    right_min_at_idx[i] = right_min
    right_min = min(right_min, input_list[i])
    
# now for every element satisfy; left_max < element < right_min
for i in range(n):
    if left_max_at_idx[i] < input_list[i] < right_min_at_idx[i]:
        no_of_pivots += 1
                
print(no_of_pivots)