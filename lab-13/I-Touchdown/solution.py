play_count = int(input())
plays = list(map(int, input().split()))
field_position = 20
first_down_line = 30
plays_since_first_down = 0
result = "Nothing"

for play_number in range(play_count):
    field_position = field_position + plays[play_number]
    # print("after play", play_number, field_position, first_down_line, plays_since_first_down)
    if field_position >= 100:
        result = "Touchdown"
        break
    if field_position <= 0:
        result = "Safety"
        break
    plays_since_first_down = plays_since_first_down + 1
    if field_position >= first_down_line:
        first_down_line = field_position + 10
        plays_since_first_down = 0
    elif plays_since_first_down == 4:
        result = "Nothing"
        break

print(result)
