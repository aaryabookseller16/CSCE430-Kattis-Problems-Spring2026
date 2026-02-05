import sys

lines = [line.strip() for line in sys.stdin if line.strip() != ""]

if len(lines) >= 3:
    correct_for_friend = int(lines[0])
    my_answers = lines[1]
    friend_answers = lines[2]

    # print("k:", correct_for_friend)
    # print("me:", my_answers)
    # print("friend:", friend_answers)

    total_questions = len(my_answers)
    same_count = 0

    for i in range(total_questions):
        if my_answers[i] == friend_answers[i]:
            same_count += 1

    different_count = total_questions - same_count

    # best we can do from the matching spots + from the differing spots
    best_from_same = min(same_count, correct_for_friend)
    best_from_diff = min(different_count, total_questions - correct_for_friend)

    max_score = best_from_same + best_from_diff
    print(max_score)