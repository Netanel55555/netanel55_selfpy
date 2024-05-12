def check_win(secret_word, old_letters_guessed):
    length = len(secret_word)

    for char in old_letters_guessed:
        if char in secret_word:
            length -= 1

    return length == 0


word = "friends"
letters = ['m', 'p', 'j', 'i', 's', 'k']
print(check_win(word, letters))
