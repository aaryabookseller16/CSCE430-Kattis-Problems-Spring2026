female_color = input().strip()
male_color = input().strip()

female_black_choices = []
female_dilution_choices = []
female_red_choices = []

male_black_choices = []
male_dilution_choices = []
male_red_choices = []

if female_color == "Black":
    female_black_choices = [("BB", 0.5), ("Bb", 0.5)]
    female_dilution_choices = [("DD", 0.5), ("Dd", 0.5)]
    female_red_choices = [("oo", 1.0)]
elif female_color == "Blue":
    female_black_choices = [("BB", 0.5), ("Bb", 0.5)]
    female_dilution_choices = [("dd", 1.0)]
    female_red_choices = [("oo", 1.0)]
elif female_color == "Chocolate":
    female_black_choices = [("bb", 1.0)]
    female_dilution_choices = [("DD", 0.5), ("Dd", 0.5)]
    female_red_choices = [("oo", 1.0)]
elif female_color == "Lilac":
    female_black_choices = [("bb", 1.0)]
    female_dilution_choices = [("dd", 1.0)]
    female_red_choices = [("oo", 1.0)]
elif female_color == "Red":
    female_black_choices = [("BB", 0.25), ("Bb", 0.5), ("bb", 0.25)]
    female_dilution_choices = [("DD", 0.5), ("Dd", 0.5)]
    female_red_choices = [("OO", 1.0)]
elif female_color == "Cream":
    female_black_choices = [("BB", 0.25), ("Bb", 0.5), ("bb", 0.25)]
    female_dilution_choices = [("dd", 1.0)]
    female_red_choices = [("OO", 1.0)]
elif female_color == "Black-Red Tortie":
    female_black_choices = [("BB", 0.5), ("Bb", 0.5)]
    female_dilution_choices = [("DD", 0.5), ("Dd", 0.5)]
    female_red_choices = [("Oo", 1.0)]
elif female_color == "Blue-Cream Tortie":
    female_black_choices = [("BB", 0.5), ("Bb", 0.5)]
    female_dilution_choices = [("dd", 1.0)]
    female_red_choices = [("Oo", 1.0)]
elif female_color == "Chocolate-Red Tortie":
    female_black_choices = [("bb", 1.0)]
    female_dilution_choices = [("DD", 0.5), ("Dd", 0.5)]
    female_red_choices = [("Oo", 1.0)]
else:
    female_black_choices = [("bb", 1.0)]
    female_dilution_choices = [("dd", 1.0)]
    female_red_choices = [("Oo", 1.0)]

if male_color == "Black":
    male_black_choices = [("BB", 0.5), ("Bb", 0.5)]
    male_dilution_choices = [("DD", 0.5), ("Dd", 0.5)]
    male_red_choices = [("o", 1.0)]
elif male_color == "Blue":
    male_black_choices = [("BB", 0.5), ("Bb", 0.5)]
    male_dilution_choices = [("dd", 1.0)]
    male_red_choices = [("o", 1.0)]
elif male_color == "Chocolate":
    male_black_choices = [("bb", 1.0)]
    male_dilution_choices = [("DD", 0.5), ("Dd", 0.5)]
    male_red_choices = [("o", 1.0)]
elif male_color == "Lilac":
    male_black_choices = [("bb", 1.0)]
    male_dilution_choices = [("dd", 1.0)]
    male_red_choices = [("o", 1.0)]
elif male_color == "Red":
    male_black_choices = [("BB", 0.25), ("Bb", 0.5), ("bb", 0.25)]
    male_dilution_choices = [("DD", 0.5), ("Dd", 0.5)]
    male_red_choices = [("O", 1.0)]
else:
    male_black_choices = [("BB", 0.25), ("Bb", 0.5), ("bb", 0.25)]
    male_dilution_choices = [("dd", 1.0)]
    male_red_choices = [("O", 1.0)]

answer = {}

for female_black, female_black_chance in female_black_choices:
  for female_dilution, female_dilution_chance in female_dilution_choices:
   for female_red, female_red_chance in female_red_choices:
    for male_black, male_black_chance in male_black_choices:
     for male_dilution, male_dilution_chance in male_dilution_choices:
      for male_red, male_red_chance in male_red_choices:

       female_black_gametes = []
       if female_black == "BB":
           female_black_gametes = [("B", 1.0)]
       elif female_black == "bb":
           female_black_gametes = [("b", 1.0)]
       else:
           female_black_gametes = [("B", 0.5), ("b", 0.5)]

       male_black_gametes = []
       if male_black == "BB":
           male_black_gametes = [("B", 1.0)]
       elif male_black == "bb":
           male_black_gametes = [("b", 1.0)]
       else:
           male_black_gametes = [("B", 0.5), ("b", 0.5)]

       female_dilution_gametes = []
       if female_dilution == "DD":
           female_dilution_gametes = [("D", 1.0)]
       elif female_dilution == "dd":
           female_dilution_gametes = [("d", 1.0)]
       else:
           female_dilution_gametes = [("D", 0.5), ("d", 0.5)]

       male_dilution_gametes = []
       if male_dilution == "DD":
           male_dilution_gametes = [("D", 1.0)]
       elif male_dilution == "dd":
           male_dilution_gametes = [("d", 1.0)]
       else:
           male_dilution_gametes = [("D", 0.5), ("d", 0.5)]

       female_red_gametes = []
       if female_red == "OO":
           female_red_gametes = [("O", 1.0)]
       elif female_red == "oo":
           female_red_gametes = [("o", 1.0)]
       else:
           female_red_gametes = [("O", 0.5), ("o", 0.5)]

       base_chance = female_black_chance * female_dilution_chance * female_red_chance * male_black_chance * male_dilution_chance * male_red_chance

       for mother_black, mother_black_chance in female_black_gametes:
        for father_black, father_black_chance in male_black_gametes:
         for mother_dilution, mother_dilution_chance in female_dilution_gametes:
          for father_dilution, father_dilution_chance in male_dilution_gametes:
           for mother_red, mother_red_chance in female_red_gametes:
            for kitten_sex in ["girl", "boy"]:
             chance = base_chance * mother_black_chance * father_black_chance * mother_dilution_chance * father_dilution_chance * mother_red_chance * 0.5

             has_black = mother_black == "B" or father_black == "B"
             is_dilute = mother_dilution == "d" and father_dilution == "d"

             if kitten_sex == "boy":
                 if mother_red == "O":
                     kitten_color = "Cream" if is_dilute else "Red"
                 else:
                     if has_black:
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
                     if has_black:
                         kitten_color = "Blue-Cream Tortie" if is_dilute else "Black-Red Tortie"
                     else:
                         kitten_color = "Lilac-Cream Tortie" if is_dilute else "Chocolate-Red Tortie"

             if kitten_color not in answer:
                 answer[kitten_color] = 0.0
             answer[kitten_color] = answer[kitten_color] + chance
             # print("kitten", kitten_color, chance)

items = []
for color in answer:
    if answer[color] > 0:
        items.append((color, answer[color]))

items.sort(key=lambda thing: (-thing[1], thing[0]))

for color, probability in items:
    print(color, format(probability, ".9f"))
