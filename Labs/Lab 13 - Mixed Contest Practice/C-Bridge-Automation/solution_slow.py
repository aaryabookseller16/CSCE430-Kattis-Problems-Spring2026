boat_count = int(input())
arrival_times = []
for boat_number in range(boat_count):
    arrival_times.append(int(input()))
best_time = [10 ** 18] * (boat_count + 1)
best_time[0] = 0

for last_boat in range(1, boat_count + 1):
    for first_boat in range(1, last_boat + 1):
        bridge_fully_up_time = arrival_times[first_boat - 1] + 1800
        current_time = bridge_fully_up_time
        for boat_number in range(first_boat, last_boat + 1):
            if current_time < arrival_times[boat_number - 1]:
                current_time = arrival_times[boat_number - 1]
            current_time = current_time + 20
        opening_cost = 60 + (current_time - bridge_fully_up_time) + 60
        maybe_answer = best_time[first_boat - 1] + opening_cost
        if maybe_answer < best_time[last_boat]:
            best_time[last_boat] = maybe_answer
        # print("slow group", first_boat, last_boat, opening_cost)

print(best_time[boat_count])
