
no_of_worlds = int(input())
population = list(map(int, input().split()))

people_to_kill = 0

# Traverse from right to left
for i in range(no_of_worlds - 2, -1, -1):
    # population[i] must be strictly less than population[i + 1]
    if population[i] >= population[i + 1]:
        target = population[i + 1] - 1

        # If population becomes negative, impossible
        if target < 0:
            print(1)
            exit()

        people_to_kill += population[i] - target
        population[i] = target

# If no one was killed, output 1 per problem statement
if people_to_kill == 0:
    print(1)
else:
    print(people_to_kill)