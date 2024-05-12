import re

from ordered_set import OrderedSet

HANGMAN_ASCII_ART = """
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\\\ / _' | '_ ' _ \\\\ / _' | '_ \\\\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\\\\__, |_| |_| |_|\\\\__,_|_| |_|
                        __/ |
                        |___/
6
"""

HANGMAN_PHOTOS = {
    1: "x-------x",
    2: """
        x-------x
        |
        |
        |
        |
        |
    """,
    3: """
        x-------x
        |       |
        |       0
        |
        |
        |
    """,
    4: """
        x-------x
        |       |
        |       0
        |       |
        |
        |
    """,
    5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
    """,
    6: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
    """,
    7: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
    """
}

MAX_TRIES = 6


def print_hangman(num_of_tries, hangman_dict) -> None:
    print(hangman_dict[num_of_tries])


def check_win(secret_word, old_letters_guessed) -> bool:
    length = len(secret_word)

    for char in old_letters_guessed:
        if char in secret_word:
            length -= 1

    return length == 0


def show_hidden_word(secret_word, old_letters_guessed) -> None:
    print_string = ""

    for char in secret_word:
        if char in old_letters_guessed:
            print_string += char
        else:
            print_string += "_"

    print(print_string)


def check_valid_input(letter_guessed, old_letters_guessed) -> bool:
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed) -> bool:
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print("->".join(old_letters_guessed))
        return False


def choose_word(file_path, index) -> tuple:
    with open(file_path, "r") as file:
        file_data = file.read()
    lines = file_data.split("\n")

    file_list = []
    for line in lines:
        file_list.extend(line.split())

    unique_words = list(set(file_list))  
    count = len(unique_words)

    if not (0 <= index < count):
        raise IndexError(f"Index {index} out of range for {count} unique words")

    chosen_word = unique_words[index] 
    return (count, chosen_word)


def game_main():
    print(HANGMAN_ASCII_ART)

    # define variables
    secret_word = str()
    guessed_letters = list()
    num_of_tries = 0

    file_path = input("Please enter a file: ")
    index = input("Please enter index: ")

    print("Let's start!")

    secret_word = choose_word(file_path, int(index))[1]
    print(secret_word)
    print_hangman(1, HANGMAN_PHOTOS)

    # Game main loop
    while 1:

        # enter a guess
        letter = input("Guess a letter:")

        if not try_update_letter_guessed(letter, guessed_letters):
            continue

        if letter in secret_word:

            if check_win(secret_word, guessed_letters):
                print("WIN")
                break

            show_hidden_word(secret_word, guessed_letters)

        else:
            num_of_tries += 1
            print_hangman(num_of_tries + 1, HANGMAN_PHOTOS)
            show_hidden_word(secret_word, guessed_letters)

            if num_of_tries == MAX_TRIES:
                print("LOST")
                break


game_main()


