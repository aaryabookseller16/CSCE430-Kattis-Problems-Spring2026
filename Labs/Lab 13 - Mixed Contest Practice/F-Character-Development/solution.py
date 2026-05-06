character_count = int(input())
all_groups = 1
for character_number in range(character_count):
    all_groups = all_groups * 2
relationships = all_groups - character_count - 1

print(relationships)
