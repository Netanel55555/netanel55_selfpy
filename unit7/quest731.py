def show_hidden_word(secret_word, old_letters_guessed):
    print_string = ""

    for char in secret_word:
        if char in old_letters_guessed:
            print_string += char
        else:
            print_string += "_"

    print(print_string)