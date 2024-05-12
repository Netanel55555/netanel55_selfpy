hangman_stages = {
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


def print_hangman(num_of_tries, hangman_dict):
    print(hangman_dict[num_of_tries])


print_hangman(7, hangman_stages)
