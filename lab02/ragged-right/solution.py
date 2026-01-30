import sys

def penalty(n,m):
    return (n-m)**2

paragraph = [line.rstrip('\n') for line in sys.stdin]
#print(paragraph)

n = 0
size_of_lines = []
for line in paragraph:
    current_size = len(line)
    n = max(n, current_size)
    
total_penalty = 0

for i in range(len(paragraph)-1):
    line = paragraph[i]
    current_size = len(line)
    total_penalty += penalty(n,current_size)
    
print(total_penalty)
    

     