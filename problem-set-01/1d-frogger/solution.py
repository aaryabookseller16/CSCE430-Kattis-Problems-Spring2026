#accept input line 1
n, s, m = map(int, input().split())

# create a board
board = [int(i) for i in input().split()]

#variables
len_board = len(board)
visited = set()
h = 0
curr_pos = s-1

#logic    
while True:
    #if frog goes out of bounds (on the right)
    if curr_pos >= n:
        print(f"right \n {h}")
        break
    #if frog goes out of bounds (on the left)
    if curr_pos < 0:
        print(f"left \n {h}")
        break   

    k = board[curr_pos] # current element
    
    #found magic
    if k == m:
        print(f"magic \n {h}")
        break
    
    #cycle condition
    if  curr_pos in visited:
        print(f"cycle \n {h}")
        break
    
    visited.add(curr_pos)
    
    next_pos = curr_pos + k
    h += 1 # count hops
    
    #check if next position is valid
    if next_pos < 0:
        print(f"left \n {h}")
        break
    if next_pos >= n:
        print(f"right \n {h}")
        break
    
    curr_pos = next_pos