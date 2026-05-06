play_count = int(input())
plays = list(map(int, input().split()))

positions = []
current_position = 20

for play_number in range(play_count):
    current_position = current_position + plays[play_number]
    positions.append(current_position)

answer = "Nothing"
first_down_line = 30
plays_since_first_down = 0

for position in positions:
    # print("checking", position, first_down_line, plays_since_first_down)
    if position >= 100:
        answer = "Touchdown"
        break
    if position <= 0:
        answer = "Safety"
        break

    plays_since_first_down = plays_since_first_down + 1

    if position >= first_down_line:
        first_down_line = position + 10
        plays_since_first_down = 0

    elif plays_since_first_down == 4:
        answer = "Nothing"
        break

print(answer)
