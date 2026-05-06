width, height = map(int,input().split())
game_map = []
start_row = 0
start_col = 0

for row_number in range(height):
    row_text = input()
    game_map.append(list(row_text))
    if "P" in row_text:
        start_row = row_number
        start_col = row_text.index("P")

seen = []
for row_number in range(height):
    seen.append([False] * width)

places_to_check = []
places_to_check.append((start_row,start_col))
seen[start_row][start_col] = True
gold_found = 0

while len(places_to_check) > 0:
    row,col = places_to_check.pop()

    if game_map[row][col] == "G":
        gold_found = gold_found + 1
        # print(row, col)
    near_trap = False
    if game_map[row-1][col] == "T":
        near_trap = True
    if game_map[row+1][col] == "T":
        near_trap = True
    if game_map[row][col-1] == "T":
        near_trap = True
    if game_map[row][col+1] == "T":
        near_trap = True
    if near_trap == False:
        next_spots = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        for next_row,next_col in next_spots:
            if seen[next_row][next_col] == False:
                if game_map[next_row][next_col] != "#":
                    if game_map[next_row][next_col] != "T":
                        seen[next_row][next_col] = True
                        places_to_check.append((next_row,next_col))

print(gold_found)
