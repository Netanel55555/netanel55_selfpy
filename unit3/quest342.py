from collections import Counter

input_string = input("Please enter a string:")

first_letter = input_string[0]
THE_LETTER_E = 'e'

count = Counter(input_string)

print(first_letter + input_string[1:].replace(first_letter,THE_LETTER_E, count[first_letter]))