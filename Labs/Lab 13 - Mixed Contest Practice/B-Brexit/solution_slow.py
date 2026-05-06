country_count, partnership_count, home_country, first_leaver = map(int, input().split())
partners = []
for country in range(country_count + 1):
    partners.append([])
for partnership_number in range(partnership_count):
    country_a, country_b = map(int, input().split())
    partners[country_a].append(country_b)
    partners[country_b].append(country_a)

has_left = [False] * (country_count + 1)
has_left[first_leaver] = True
changed = True
while changed:
    changed = False
    for country in range(1, country_count + 1):
        if has_left[country] == False:
            gone = 0
            for partner_country in partners[country]:
                if has_left[partner_country]:
                    gone = gone + 1
            # print("country", country, "lost", gone, "out of", len(partners[country]))

            if gone * 2 >= len(partners[country]):
                has_left[country] = True
                changed = True

if has_left[home_country]:
    print("leave")
else:
    print("stay")
