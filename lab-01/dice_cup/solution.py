import sys

data = sys.stdin.read().strip().split()
n = int(data[0])
m = int(data[1])
total_outcomes = n * m

bigger_die = max(n, m)
smaller_die = min(n, m)

sums_of_possibilites = {} # store all sums
probability = {} # store the probability of all sums

n_data = [] # get all possible numbers for the n-sided die
for i in range(1, n + 1):
    n_data.append(i)
    
m_data = [] # get all possible numbers for the m-sided die
for i in range(1, m + 1):
    m_data.append(i)
    
for x in n_data:
    for y in m_data:
        current_sum = x + y
        ways = max(0, min(current_sum - 1, smaller_die) - max(1, current_sum - bigger_die) + 1) # number of ways to get a given sum

        sums_of_possibilites[current_sum] = ways 
        probability[current_sum] = ways / total_outcomes # probability of that sum
        
        
max_probability = max(probability.values())

# find most likely sums
most_likely_sums = []
for current_sum in probability:
    if probability[current_sum] == max_probability:
        most_likely_sums.append(current_sum)

most_likely_sums.sort()

for s in most_likely_sums:
    print(s)
