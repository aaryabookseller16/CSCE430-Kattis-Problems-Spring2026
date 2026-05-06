female_color = input().strip()
male_color = input().strip()
all_colors = [
    "Black", "Blue", "Chocolate", "Lilac", "Red", "Cream",
    "Black-Red Tortie", "Blue-Cream Tortie", "Chocolate-Red Tortie", "Lilac-Cream Tortie"
]
female_options = []
male_options = []

for cat_color in all_colors:
    if cat_color == female_color:
        if cat_color == "Black":
            female_options = [("BB", "DD", "oo", 0.25), ("BB", "Dd", "oo", 0.25), ("Bb", "DD", "oo", 0.25), ("Bb", "Dd", "oo", 0.25)]
        if cat_color == "Blue":
            female_options = [("BB", "dd", "oo", 0.5), ("Bb", "dd", "oo", 0.5)]
        if cat_color == "Chocolate":
            female_options = [("bb", "DD", "oo", 0.5), ("bb", "Dd", "oo", 0.5)]
        if cat_color == "Lilac":
            female_options = [("bb", "dd", "oo", 1.0)]
        if cat_color == "Red":
            female_options = [("BB", "DD", "OO", 0.125), ("BB", "Dd", "OO", 0.125), ("Bb", "DD", "OO", 0.25), ("Bb", "Dd", "OO", 0.25), ("bb", "DD", "OO", 0.125), ("bb", "Dd", "OO", 0.125)]
        if cat_color == "Cream":
            female_options = [("BB", "dd", "OO", 0.25), ("Bb", "dd", "OO", 0.5), ("bb", "dd", "OO", 0.25)]
        if cat_color == "Black-Red Tortie":
            female_options = [("BB", "DD", "Oo", 0.25), ("BB", "Dd", "Oo", 0.25), ("Bb", "DD", "Oo", 0.25), ("Bb", "Dd", "Oo", 0.25)]
        if cat_color == "Blue-Cream Tortie":
            female_options = [("BB", "dd", "Oo", 0.5), ("Bb", "dd", "Oo", 0.5)]
        if cat_color == "Chocolate-Red Tortie":
            female_options = [("bb", "DD", "Oo", 0.5), ("bb", "Dd", "Oo", 0.5)]
        if cat_color == "Lilac-Cream Tortie":
            female_options = [("bb", "dd", "Oo", 1.0)]
    if cat_color == male_color:
        if cat_color == "Black":
            male_options = [("BB", "DD", "o", 0.25), ("BB", "Dd", "o", 0.25), ("Bb", "DD", "o", 0.25), ("Bb", "Dd", "o", 0.25)]
        if cat_color == "Blue":
            male_options = [("BB", "dd", "o", 0.5), ("Bb", "dd", "o", 0.5)]
        if cat_color == "Chocolate":
            male_options = [("bb", "DD", "o", 0.5), ("bb", "Dd", "o", 0.5)]
        if cat_color == "Lilac":
            male_options = [("bb", "dd", "o", 1.0)]
        if cat_color == "Red":
            male_options = [("BB", "DD", "O", 0.125), ("BB", "Dd", "O", 0.125), ("Bb", "DD", "O", 0.25), ("Bb", "Dd", "O", 0.25), ("bb", "DD", "O", 0.125), ("bb", "Dd", "O", 0.125)]
        if cat_color == "Cream":
            male_options = [("BB", "dd", "O", 0.25), ("Bb", "dd", "O", 0.5), ("bb", "dd", "O", 0.25)]

answer = {}

for female_black, female_dilution, female_red, female_chance in female_options:
    for male_black, male_dilution, male_red, male_chance in male_options:
        female_black_gametes = [("B", 1.0)] if female_black == "BB" else [("b", 1.0)] if female_black == "bb" else [("B", 0.5), ("b", 0.5)]
        male_black_gametes = [("B", 1.0)] if male_black == "BB" else [("b", 1.0)] if male_black == "bb" else [("B", 0.5), ("b", 0.5)]
        female_dilution_gametes = [("D", 1.0)] if female_dilution == "DD" else [("d", 1.0)] if female_dilution == "dd" else [("D", 0.5), ("d", 0.5)]
        male_dilution_gametes = [("D", 1.0)] if male_dilution == "DD" else [("d", 1.0)] if male_dilution == "dd" else [("D", 0.5), ("d", 0.5)]
        female_red_gametes = [("O", 1.0)] if female_red == "OO" else [("o", 1.0)] if female_red == "oo" else [("O", 0.5), ("o", 0.5)]
        for mother_black, mother_black_chance in female_black_gametes:
            for father_black, father_black_chance in male_black_gametes:
                for mother_dilution, mother_dilution_chance in female_dilution_gametes:
                    for father_dilution, father_dilution_chance in male_dilution_gametes:
                        for mother_red, mother_red_chance in female_red_gametes:
                            for kitten_sex in ["girl", "boy"]:
                                probability = female_chance * male_chance * mother_black_chance * father_black_chance * mother_dilution_chance * father_dilution_chance * mother_red_chance * 0.5
                                has_black = mother_black == "B" or father_black == "B"
                                is_dilute = mother_dilution == "d" and father_dilution == "d"
                                if kitten_sex == "boy":
                                    if mother_red == "O":
                                        kitten_color = "Cream" if is_dilute else "Red"
                                    elif has_black:
                                        kitten_color = "Blue" if is_dilute else "Black"
                                    else:
                                        kitten_color = "Lilac" if is_dilute else "Chocolate"
                                else:
                                    if mother_red == "O" and male_red == "O":
                                        kitten_color = "Cream" if is_dilute else "Red"
                                    elif mother_red == "o" and male_red == "o":
                                        if has_black:
                                            kitten_color = "Blue" if is_dilute else "Black"
                                        else:
                                            kitten_color = "Lilac" if is_dilute else "Chocolate"
                                    else:
                                        kitten_color = "Blue-Cream Tortie" if is_dilute and has_black else "Black-Red Tortie" if has_black else "Lilac-Cream Tortie" if is_dilute else "Chocolate-Red Tortie"

                                answer[kitten_color] = answer.get(kitten_color, 0.0) + probability
                                # print(kitten_color, probability)
items = sorted(answer.items(), key=lambda thing: (-thing[1], thing[0]))
for color, probability in items:
    print(color, format(probability, ".9f"))
