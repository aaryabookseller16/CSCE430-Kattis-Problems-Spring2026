import sys

input_tokens = sys.stdin.read().split()

if not input_tokens:
    sys.exit(0)

#make a set of the voweel pairs
double_vowel_pairs = {"aa", "ee", "ii", "oo", "uu", "yy"}

current_token_index = 0
favorite_words_output = []

while True:
    words_in_this_case = int(input_tokens[current_token_index])
    current_token_index += 1

    
    if words_in_this_case == 0: # stop reading
        break

    best_word_for_bill = "" # this will be our best word
    highest_double_vowel_count = -1 #this will keep track of the word(s) with the highest vowels

    for _ in range(words_in_this_case):
        # input_tokens is our array of words
        current_word = input_tokens[current_token_index]
        current_token_index += 1 #nexet word for next iter

        current_word_double_count = 0

        # do a fixed sliding window approach inside the word we got
        for letter_index in range(len(current_word) - 1):
            two_letter_piece = current_word[letter_index:letter_index + 2]
            if two_letter_piece in double_vowel_pairs:
                current_word_double_count += 1

        # keep the word with highest double-vowel count
        if current_word_double_count > highest_double_vowel_count:
            highest_double_vowel_count = current_word_double_count
            best_word_for_bill = current_word

    favorite_words_output.append(best_word_for_bill)

sys.stdout.write("\n".join(favorite_words_output))
