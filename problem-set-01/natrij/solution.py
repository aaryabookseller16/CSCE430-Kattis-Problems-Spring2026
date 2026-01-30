current_time = list(map(int, input().split(":")))
detonation_time = list(map(int, input().split(":")))


current_time_in_seconds = 3600*current_time[0] + 60*current_time[1] + current_time[2]
detonation_time_in_seconds = 3600*detonation_time[0] + 60*detonation_time[1] + detonation_time[2]

if current_time[0] < detonation_time[0]: # if detonation is on the same
    difference_in_time = detonation_time_in_seconds - current_time_in_seconds
else: # if detonation is on the next day, add 24hours
    difference_in_time = (detonation_time_in_seconds + 24*3600) - current_time_in_seconds
    
difference_in_hours = difference_in_time//3600
if difference_in_hours < 12:
    difference_in_hours = "0" + str(difference_in_hours)
difference_in_time = difference_in_time % 3600 # whatever remains after taking out hours


difference_in_minutes = difference_in_time//60
if difference_in_minutes < 10:
    difference_in_minutes = "0" + str(difference_in_minutes)
difference_in_time = difference_in_time % 60 # whatever remains after taking out minutes

difference_in_seconds = difference_in_time
if difference_in_seconds < 10:
    difference_in_seconds = "0" + str(difference_in_seconds)

print(f"{difference_in_hours}:{difference_in_minutes}:{difference_in_seconds}")