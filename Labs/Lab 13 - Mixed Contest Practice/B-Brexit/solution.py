country_count, partnership_count, home_country, first_leaver = map(int, input().split())

partners = []
for country in range(country_count + 1):
    partners.append([])
for partnership_number in range(partnership_count):
    country_a, country_b = map(int, input().split())
    partners[country_a].append(country_b)
    partners[country_b].append(country_a)
original_partner_count = [0] * (country_count + 1)
for country in range(1, country_count + 1):
    original_partner_count[country] = len(partners[country])

lost_partners = [0] * (country_count + 1)
has_left = [False] * (country_count + 1)
line = [first_leaver]
has_left[first_leaver] = True
front = 0
while front < len(line):
    country_leaving = line[front]
    front = front + 1

    # print("leaving", country_leaving)

    for neighbor_country in partners[country_leaving]:
        if has_left[neighbor_country] == False:
            lost_partners[neighbor_country] = lost_partners[neighbor_country] + 1

            if lost_partners[neighbor_country] * 2 >= original_partner_count[neighbor_country]:
                has_left[neighbor_country] = True
                line.append(neighbor_country)

if has_left[home_country]:
    print("leave")
else:
    print("stay")
