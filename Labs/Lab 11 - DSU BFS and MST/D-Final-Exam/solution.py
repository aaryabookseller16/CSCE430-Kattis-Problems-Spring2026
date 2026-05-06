number_of_questions = int(input())
answers = []

for question_number in range(number_of_questions):
    answers.append(input().strip())

score = 0
spot = 0
# he wrote every answer one line too early
while spot + 1 < number_of_questions:
    if answers[spot] == answers[spot+1]:
        score = score + 1
    spot = spot + 1

print(score)