from curses.ascii import isalpha


def numbers_letters_count(my_str):
    number_count = 0

    for char in my_str:
        if char.isdigit():
            number_count += 1

    alphabet_count = len(my_str) - number_count

    return [number_count, alphabet_count]


print(numbers_letters_count("Python 3.6.3"))
