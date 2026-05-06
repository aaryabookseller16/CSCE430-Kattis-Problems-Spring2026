# Solution: Classrooms

## Goal
Solve the problem with greedy interval scheduling with multiple rooms. The implementation's main job is: Activities are considered by earliest finish time. The code assigns each activity to the room whose last activity ends latest but still before this start.

## Key idea
The solution is built around greedy interval scheduling with multiple rooms. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Activities are considered by earliest finish time. The code assigns each activity to the room whose last activity ends latest but still before this start.

## Step-by-step algorithm
1. Read all activities and sort them by finish time, then start time.
2. Keep a sorted list of end times for rooms currently holding a scheduled activity.
3. For the next activity, find the room ending latest at or before the activity start.
4. If such a room exists, replace that room end time with the new finish time.
5. Otherwise, if fewer than k rooms are in use, open another room for this activity.
6. If neither is possible, skip the activity.
7. Count and print the scheduled activities.

## Example walkthrough
If a class ends at 4 and another starts at 4, the same room can be reused.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Conceptually O(n log k); this Python list implementation has O(k) deletion cost in the worst case.

## Important details
Sorting by finish time is the key greedy choice.
