boat_count = int(input())
arrival_times = []
for boat_number in range(boat_count):
    arrival_times.append(int(input()))
best_time = [10 ** 18] * (boat_count + 1)
best_time[0] = 0

for last_boat in range(1, boat_count + 1):
    first_boat = last_boat
    while first_boat >= 1:
        boats_in_this_opening = last_boat - first_boat + 1
        first_arrival = arrival_times[first_boat - 1]
        last_arrival = arrival_times[last_boat - 1]
        time_while_bridge_is_up = max(20 * boats_in_this_opening, last_arrival - first_arrival - 1780)
        opening_cost = 120 + time_while_bridge_is_up
        maybe_answer = best_time[first_boat - 1] + opening_cost
        if maybe_answer < best_time[last_boat]:
            best_time[last_boat] = maybe_answer
        # print("group", first_boat, last_boat, opening_cost, maybe_answer)

        first_boat = first_boat - 1

print(best_time[boat_count])
